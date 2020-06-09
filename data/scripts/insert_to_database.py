
from django.core.wsgi import get_wsgi_application
import os
import json

# this script was used only once to add existing data to the database and create fixtures

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colour_perfect.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
application = get_wsgi_application()

from products.models import Category, Colour, Product, Brand

if __name__ == '__main__':

    product_types_with_colours = [
        "blush", "bronzer", "eyeshadow", "lip_liner", "lipstick", "nail_polish"]

    def import_data(obj):
        ''' creates category, product and colour categories using products.json file in a way 
        that product objects have foreign keys of category and colour objects'''
        category = Category.objects.get_or_create(
            name=obj['product_type'], display_name=obj['product_type'].replace('_', ' ').capitalize())
        brand = Brand.objects.get_or_create(name=obj['brand'], display_name=obj['brand'].replace('_', ' ').capitalize())
        product = Product.objects.get_or_create(name=obj["name"], price=obj['price'], image_link=obj['image_link'], description=obj['description'])
        product[0].category.add(category[0])
        product[0].brand.add(brand[0])
        for season in obj['product_colors'][0]:

            for col_obj in obj['product_colors'][0][season]:
                colour = Colour.objects.get_or_create(
                    hex_value=col_obj['hex_value'], name=col_obj['colour_name'], season=season)
                product[0].product_colors.add(colour[0])

    filepath = 'data/products.json'
    with open(filepath, 'r', encoding='utf-8',
              errors='ignore') as fp:
        products = json.load(fp)

    for product in products:
        if product["product_type"] in product_types_with_colours:
            import_data(product)
