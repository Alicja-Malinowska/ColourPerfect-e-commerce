from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import Http404
from django.conf import settings
from basket.models import Basket, BasketItem, Colour
from products.models import Product
from helpers.validators import is_hex_color, correct_quantity


# Create your views here.

def basket(request):
    ''' render basket page '''
    
    return render(request, 'basket.html')


def add_to_basket(request, product_id):
    ''' add item to the basket, if user is logged in, save it in the database, otherwise save it in session '''

    product = get_object_or_404(Product, pk=product_id)
    all_colours = product.product_colors.all()
    redirect_url = request.POST.get('redirect_url')
    colour = request.POST.get('colour')
    colour_obj = None
    colour_name = 'clear or standard'
    colour_id = None

    # if product has colour, get it
    if Colour.objects.filter(hex_value=colour).exists():
        colour_obj = Colour.objects.get(hex_value=colour)
        colour_name = colour_obj.name
        colour_id = colour_obj.id
   
    # if 'add to wishlist' button was clicked, redirect to add_to_wishlist view
    if 'wishlist' in request.POST:
        request.session['redirect_url'] = redirect_url
        request.session['colour'] = colour 
        return redirect(reverse('add_to_wishlist', args=[product_id]))
    else:

        # validate if colour should have been chosen for the product or not
        # and if the colour value is correct
        if request.POST.get('has_colours') == 'True':
            if not colour:
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
        elif request.POST.get('has_colours') == 'False' and colour:
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
                messages.add_message(request,
                                settings.BASKET_MESSAGE,
                                (f"{quantity} more {product.name} in colour: {colour_name} added to the basket."))

            else:
                basket_item = BasketItem(
                    basket=basket, product=product, quantity=quantity, colour=colour_obj)
                basket_item.save()
                messages.add_message(request,
                                settings.BASKET_MESSAGE,
                                (f"Added {quantity} {product.name} in colour: {colour_name} to the basket."))

        # if no user is logged in use session to store basket items
        else:
            basket = request.session.get('basket', {})
            item_id = str(product_id) + str(colour_id)
        

            if item_id in list(basket.keys()):
                basket[item_id]['quantity'] += quantity
                messages.add_message(request,
                                settings.BASKET_MESSAGE,
                                (f"{quantity} more {product.name} in colour: {colour_name} added to the basket."))
            else:
                basket[item_id] = {
                    'product': product_id,
                    'quantity': quantity,
                    'colour': colour_id
                }
                messages.add_message(request,
                                settings.BASKET_MESSAGE,
                                (f"Added {quantity} {product.name} in colour: {colour_name} to the basket."))

            request.session['basket'] = basket

    return redirect(redirect_url, product_id=product_id)

def adjust_quantity(request):
    ''' change quantity of the basket item '''

    quantity = int(request.POST.get('quantity'))
    item_id = request.POST.get('item_id')

    if request.user.is_authenticated:
        basket_item = BasketItem.objects.get(pk=item_id)
        if basket_item.quantity == quantity:
            return redirect(reverse('basket'))
        else:
            basket_item.quantity = quantity
            basket_item.save()
            product_name = basket_item.product.name
    else:
        basket = request.session.get('basket', {})
        if basket[item_id]['quantity'] == quantity:
             return redirect(reverse('basket'))
        else:
            basket[item_id]['quantity'] = quantity
            request.session['basket'] = basket
            product_name = Product.objects.get(pk=basket[item_id]['product'])
        
    messages.add_message(request,
                                settings.BASKET_MESSAGE, (f"Quantity of { product_name } changed to { quantity }"))
    return redirect(reverse('basket'))

def delete_item(request, item_id):

    if request.user.is_authenticated:
        
        item = get_object_or_404(BasketItem, pk=item_id)
        messages.add_message(request,
                                settings.BASKET_MESSAGE, (f"Deleted { item.product.name} from your basket."))
        item.delete()
    else:
        basket = request.session.get('basket', {})
        if item_id in basket.keys():
            product = Product.objects.get(id=basket[item_id]['product'])
            messages.add_message(request,
                                settings.BASKET_MESSAGE, (f"Deleted { product.name } from your basket."))
            basket.pop(item_id, None)
            request.session['basket'] = basket
        else:
            raise Http404()
    
    
    return redirect(reverse('basket'))






    
