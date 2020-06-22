from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from basket.models import Basket, BasketItem, Colour
from products.models import Product
from helpers.validators import is_hex_color, correct_quantity


# Create your views here.

def basket(request):

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
            if not basket[item_id]['colour'] == None:
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
    return render(request, 'basket.html', context)


def add_to_basket(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    all_colours = product.product_colors.all()
    redirect_url = request.POST.get('redirect_url')
    colour = request.POST.get('colour')
    colour_obj = None
    colour_name = 'clear or standard'
    colour_id = None
    if Colour.objects.filter(hex_value=colour).exists():
        colour_obj = Colour.objects.get(hex_value=colour)
        colour_name = colour_obj.name
        colour_id = colour_obj.id

    # validate if colour should have been chosen for the producst or not
    # and if the colour value is correct
    if request.POST.get('has_colours') == 'True':
        if colour == None:
            messages.error(request,
                           ("Please choose a colour first."))
            return redirect(redirect_url)
        elif not is_hex_color(colour):
            messages.error(request,
                           ("Invalid colour, please select a colour from the displayed ones"))
            return redirect(redirect_url)
        elif not all_colours.filter(hex_value=colour).exists():
            messages.error(request,
                           ("This product is not available in this colour, please select a colour from the displayed ones"))
            return redirect(redirect_url)
    elif request.POST.get('has_colours') == 'False' and not colour == None:
        messages.error(request,
                       ("There are no colour options for this product."))
        return redirect(redirect_url)

    # valdidate quantity
    try:
        quantity = int(request.POST.get('quantity'))

        if not correct_quantity(quantity):
            messages.error(request,
                           ("You can add 1-99 products to the basket."))
            return redirect(redirect_url)
    except:
        messages.error(request,
                       ("Quantity must be an integer."))
        return redirect(redirect_url)

    # for logged-in users save basket in the database
    if request.user.is_authenticated:
        basket = Basket.objects.get_or_create(owner=request.user)[0]
        basket_items = BasketItem.objects.filter(basket=basket)

        if basket_items.filter(product__id=product.id, colour__hex_value=colour).exists():
            basket_item = BasketItem.objects.get(
                product__id=product.id, colour__hex_value=colour)
            basket_item.quantity += quantity
            basket_item.save()
            messages.success(request,
                             (f"{quantity} more {product.name} in colour: {colour_name} added to the basket."))

        else:
            basket_item = BasketItem(
                basket=basket, product=product, quantity=quantity, colour=colour_obj)
            basket_item.save()
            messages.success(request,
                             (f"Added {quantity} {product.name} in colour: {colour_name} to the basket."))

    # if no user is logged in use session to store basket items
    else:
        basket = request.session.get('basket', {})
        item_id = str(product_id) + str(colour_id)
       

        if item_id in list(basket.keys()):
            basket[item_id]['quantity'] += quantity
            messages.success(request,
                             (f"{quantity} more {product.name} in colour: {colour_name} added to the basket."))
        else:
            basket[item_id] = {
                'product': product_id,
                'quantity': quantity,
                'colour': colour_id
            }
            messages.success(request,
                             (f"Added {quantity} {product.name} in colour: {colour_name} to the basket."))

        request.session['basket'] = basket

    return redirect(redirect_url)

def adjust_quantity(request):

    quantity = int(request.POST.get('quantity'))
    item_id = request.POST.get('item_id')

    if request.user.is_authenticated:
        basket_item = BasketItem.objects.get(pk=item_id)
        basket_item.quantity = quantity
        basket_item.save()
    else:
        basket = request.session.get('basket', {})
        basket[item_id]['quantity'] = quantity
        request.session['basket'] = basket
        
    return redirect(reverse('basket'))




    
