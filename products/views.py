from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.models import Product, Category, Brand
from wishlist.models import WishlistItem
from helpers.seasons import SEASONS

# Create your views here.


def product(request, id):
    '''displays a single product, together with its colours sorted according to season they belong to'''

    product = get_object_or_404(Product, pk=id)
    all_colours = product.product_colors.all()
    product_brand = product.brand
    product_categories = product.category.all()

    colours = {}

    # if there are any colours assigned to the product
    if all_colours:
        for season in SEASONS:
            season_colours = []
            for colour in all_colours:
                if colour.season == season.lower():
                    season_colours.append(colour)
            colours[season] = season_colours

    # check if colours dictionary is not empty
    has_colours = bool(colours)

    context = {
        'product': product,
        'colours': colours,
        'product_brand': product_brand,
        'product_categories': product_categories,
        'seasons': SEASONS,
        'has_colours': has_colours,
        

    }

    return render(request, 'product.html', context)


def search(request, q_type, query):
    '''get requested products by search term, category or brand'''

    searched_products = None

    if q_type == 'category':
        if Category.objects.filter(name=query).exists():
            searched_products = Product.objects.filter(category__name=query)
        else:
            q_type = "none"
            messages.error(request,
                           ("This category does not exist."))
    elif q_type == 'brand':
        if Brand.objects.filter(name=query).exists():
            searched_products = Product.objects.filter(brand__name=query)
        else:
            q_type = "none"
            messages.error(request,
                           ("Currently we don't sell this brand's products."))

    elif q_type == 'search':
        query = request.GET['phrase'].strip()
        if not query:
            messages.error(request,
                           ("Please type a phrase you want to search for"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        searched_products = Product.objects.filter(queries)
    
    products = []
    if searched_products:
        for product in searched_products:
            on_wishlist = False
            if request.user.is_authenticated: 
                on_wishlist = WishlistItem.objects.filter(wishlist__owner=request.user, product=product).exists()
            products.append((product, on_wishlist))

    

    if not q_type == 'search':
        query = query.replace('_', ' ')
    
    context = {
        
        'products': products,
        'searched': q_type,
        'query': query

    }

    return render(request, 'search.html', context)
