from products.models import Category, Brand


def category_brand(request):
    categories = Category.objects.all().order_by('name')
    brands = Brand.objects.all().order_by('name')

    context = {
        'categories': categories,
        'brands': brands,
    }

    return context