from products.models import Category, Brand

categories = Category.objects.all().order_by('name')
brands = Brand.objects.all().order_by('name')