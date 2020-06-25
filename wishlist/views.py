from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product, Colour
from wishlist.models import Wishlist, WishlistItem

# Create your views here.
@login_required
def wishlist(request):

    return render(request, 'wishlist.html')

@login_required
def add_to_wishlist(request, product_id):
#   THIS MIGHT NEED TO BE EXTRACTED AND USED HERE AND IN BASKET AS AN IMPORT 
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
    
    wishlist = Wishlist.objects.get_or_create(owner=request.user)[0]
    wishlist_items = WishlistItem.objects.filter(wishlist=wishlist)

    if wishlist_items.filter(product__id=product.id, colour__hex_value=colour).exists():
        wishlist_items.filter(product__id=product.id, colour__hex_value=colour).delete()
        messages.error(request,
                             (f"{product.name} in colour: {colour_name} has been removed from your wishlist."))
        
    else:
        wishlist_item = WishlistItem(
                wishlist=wishlist, product=product, colour=colour_obj)
        wishlist_item.save()
        messages.success(request,
                             (f"Added {product.name} in colour: {colour_name} to your wishlist."))
    
    return redirect(redirect_url)

@login_required
def delete_item(request, item_id):

    redirect_url = request.POST.get('redirect_url')
    WishlistItem.objects.get(pk=item_id).delete()
    
   
    return redirect(redirect_url)