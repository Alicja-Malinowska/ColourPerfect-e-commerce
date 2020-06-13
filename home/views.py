from django.shortcuts import render
from products.models import Category, Brand, Product

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
        season_products = Product.objects.filter(product_colors__season=season.lower()).prefetch_related('product_colors').distinct().order_by('description')[:3]
        col_prod = []
        for product in season_products:
            colour = product.product_colors.filter(season = season.lower()).last()
            col_prod.append((product, colour))
        suggestions[season] = col_prod
    
    
    context = {
        'categories': categories,
        'brands': brands,
        'seasons': SEASONS,
        'suggestions': suggestions,
        
    }
    return render(request, 'index.html', context)
