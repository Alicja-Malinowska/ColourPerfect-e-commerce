from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from products.models import Product, Colour
from wishlist.models import Wishlist, WishlistItem

# Create your views here.
@login_required
def wishlist(request):
    ''' show all the items added to wishlist by user'''

    wishlist_items = WishlistItem.objects.filter(wishlist__owner=request.user)

    context = {
        'wishlist_items': wishlist_items,
        
    }


    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    ''' add new item to the wishlist 
    or inform user that the item is already on the wishlist'''

    product = get_object_or_404(Product, pk=product_id)
    all_colours = product.product_colors.all()
    redirect_url = request.POST.get('redirect_url') or request.session['redirect_url']
    colour = request.POST.get('colour') or request.session['colour']
    colour_obj = None
    colour_name = 'no colour selected'
    colour_id = None
    if Colour.objects.filter(hex_value=colour).exists():
        colour_obj = Colour.objects.get(hex_value=colour)
        colour_name = colour_obj.name
        colour_id = colour_obj.id
    
    wishlist = Wishlist.objects.get_or_create(owner=request.user)[0]
    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)

    if wishlist_items.filter(product__id=product.id, colour__hex_value=colour).exists():
        messages.add_message(request,
                                settings.WISHLIST_MESSAGE,
                             (f"{product.name} in colour: {colour_name} is already on your wishlist."))
        
    else:
        wishlist_item = WishlistItem(
                wishlist=wishlist, product=product, colour=colour_obj)
        wishlist_item.save()
        messages.add_message(request,
                                settings.WISHLIST_MESSAGE,
                             (f"Added {product.name} in colour: {colour_name} to your wishlist."))
   
    return redirect(redirect_url)

@login_required
def delete_wishlist_item(request, item_id):
   
    item = get_object_or_404(WishlistItem, pk=item_id)
    messages.add_message(request,
                                settings.WISHLIST_MESSAGE, (f"Deleted { item.product.name } from your wishlist."))
    item.delete()
    
   
    return redirect('wishlist')