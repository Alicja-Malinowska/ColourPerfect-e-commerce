from django.shortcuts import render
from products.models import Category, Brand

# Create your views here.
def home(request):
    categories = Category.objects.all().order_by('name')
    brands = Brand.objects.all().order_by('name')


    context = {
        'categories': categories,
        'brands': brands
    }
    return render(request, 'index.html', context)