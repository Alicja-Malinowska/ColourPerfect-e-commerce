from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from basket.models import Basket, BasketItem
from products.models import Product
from helpers.validators import is_hex_color, correct_quantity


# Create your views here.

def basket(request):

    return render(request, 'basket.html')


def add_to_basket(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    all_colours = product.product_colors.all()
    redirect_url = request.POST.get('redirect_url')
    colour = request.POST.get('colour')
    

    # validate if colour should have been chosen for the producst or not
    # and if the colour value is correct
    if request.POST.get('has_colours') == 'True':
        if colour == None:
            messages.error(request,
                           ("Please choose a colour first."))
        elif not is_hex_color(colour):
            messages.error(request,
                           ("Invalid colour, please select a colour from the displayed ones"))
        elif not all_colours.filter(hex_value=colour).exists():
            messages.error(request,
                           ("This product is not available in this colour, please select a colour from the displayed ones"))

    elif request.POST.get('has_colours') == 'False' and not colour == None:
            messages.error(request,
                           ("There are no colour options for this product."))

    #valdidate quantity
    try:
        quantity = int(request.POST.get('quantity'))

        if not correct_quantity(quantity):
            messages.error(request,
                           ("You can add 1-99 products to the basket."))
    except:
        messages.error(request,
                           ("Quantity must be an integer."))

    if request.user.is_authenticated:
        basket = Basket.objects.get_or_create(owner=request.user)[0]
        product = get_object_or_404(Product, pk=product_id)
        basket_items = BasketItem.objects.filter(basket=basket)

        

        
            
    
        

    else: 

        print('dupa')

    return redirect(redirect_url)
   

