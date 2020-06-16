from django.shortcuts import render
from products.models import Category, Brand, Product
from helpers.get_products_and_colours import get_products

# Create your views here.


def home(request):
    ''' home view displays 3 suggested products for each beauty types, including the matching colour '''
    SEASONS = ['Spring', 'Summer', 'Autumn', 'Winter']
    suggestions = {}
    categories = Category.objects.all().order_by('name')
    brands = Brand.objects.all().order_by('name')
    
    # create a suggestions dictionary, where keys are 4 seasons and values are lists of tuples 
    # (product object, matching colour object)
    for season in SEASONS:
        
        suggestions[season] = get_products(season, 'description')
    
    
    context = {
        'categories': categories,
        'brands': brands,
        'seasons': SEASONS,
        'suggestions': suggestions,
        
    }
    return render(request, 'index.html', context)
