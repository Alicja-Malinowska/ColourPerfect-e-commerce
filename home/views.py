from django.shortcuts import render
from products.models import Category, Brand, Product
from helpers.get_products_and_colours import get_products
from helpers.seasons import SEASONS

# Create your views here.


def home(request):
    ''' home view displays 3 suggested products for each beauty types, including the matching colour '''
    suggestions = {}
    
    
    # create a suggestions dictionary, where keys are 4 seasons and values are lists of tuples 
    # (product object, matching colour object)
    for season in SEASONS:
        
        suggestions[season] = get_products(season, '?')
    
    
    context = {
        'seasons': SEASONS,
        'suggestions': suggestions,
        
    }
    return render(request, 'index.html', context)
