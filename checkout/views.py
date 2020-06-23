from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from checkout.forms import OrderForm
from basket.models import BasketItem, Basket


def checkout(request):
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

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GxAydEp1b91VbQmNInfK1D24ng3hiRemTTYfTbRX6fupTqU9JnS3DgCyWJwDWVZqpOFbzZcvJzw6rWeLJmL187X00tXYGfZqb',
        'client_secret': 'test client secret',
    }

    return render(request, 'checkout.html', context)
