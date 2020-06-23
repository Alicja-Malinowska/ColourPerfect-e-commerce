from decimal import Decimal
from django.shortcuts import get_object_or_404
from basket.models import BasketItem, Colour
from products.models import Product
from helpers.validators import is_hex_color, correct_quantity

def basket_content(request):

    basket_products = []
    total = 0
   

    if request.user.is_authenticated:
        basket_items = BasketItem.objects.filter(basket__owner=request.user)
        
        for item in basket_items:
            basket_product = {}
            basket_product['prod_obj'] = item.product
            basket_product['colour'] = item.colour
            basket_product['quantity'] = item.quantity
            basket_product['item_id'] = item.id
            basket_products.append(basket_product)
            prod_sum = Decimal(item.product.price) * item.quantity
            total += prod_sum
    else:
        basket = request.session.get('basket', {})
        for item_id in basket:
            basket_product = {}
            prod_obj = get_object_or_404(Product, pk=basket[item_id]['product'])
            basket_product['prod_obj'] = prod_obj
            if basket[item_id]['colour']:
                basket_product['colour'] = get_object_or_404(
                    Colour, pk=basket[item_id]['colour'])
            basket_product['quantity'] = basket[item_id]['quantity']
            basket_product['item_id'] = item_id
            basket_products.append(basket_product)
            prod_sum = Decimal(prod_obj.price) * basket[item_id]['quantity']
            total += prod_sum

    context = {
        'products': basket_products,
        'total': total,
    }

    return context