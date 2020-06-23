from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from checkout.forms import OrderForm
from basket.models import BasketItem


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
    }

    return render(request, 'checkout.html', context)
