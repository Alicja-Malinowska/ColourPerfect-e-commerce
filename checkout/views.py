import stripe
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from checkout.forms import OrderForm
from basket.models import BasketItem, Basket
from basket.contexts import basket_content


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.user.is_authenticated:
        if BasketItem.objects.filter(basket__owner=request.user).exists():
            basket = Basket.objects.get(owner=request.user)
        else:
            basket = None
    else: 
        basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('basket'))

    current_basket = basket_content(request)
    total = current_basket['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )


    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout.html', context)
