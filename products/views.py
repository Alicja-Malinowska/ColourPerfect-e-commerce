from django.shortcuts import render, get_object_or_404
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
    
    #if there are any colours assigned to the product
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