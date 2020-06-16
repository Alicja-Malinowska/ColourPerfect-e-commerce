from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from products.models import Product
from helpers.seasons import SEASONS
from helpers.category_brand import categories, brands

# Create your views here.


def product(request, id):
    '''displays a single product, together with its colours sorted according to season they belong to'''

    product = get_object_or_404(Product, pk=id)
    all_colours = product.product_colors.all()
    brand = product.brand.all()
    category = product.category.all()

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
        'brand': brand,
        'category': category,
        'seasons': SEASONS,
        'has_colours': has_colours,
        'categories': categories,
        'brands': brands,

    }

    return render(request, 'product.html', context)


def search(request, q_type, query):
    '''get requested products by search term, category or brand'''

    products = None

    if q_type == 'category':
        products = Product.objects.filter(category__name=query)
    elif q_type == 'brand':
        products = Product.objects.filter(brand__name=query)
    elif q_type == 'search':
        query = request.GET['phrase'].strip()
        if not query:
            messages.error(request,
                           ("Please type a phrase you want to search for"))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = Product.objects.filter(queries)

    context = {
        'categories': categories,
        'brands': brands,
        'products': products,

    }

    return render(request, 'search.html', context)
