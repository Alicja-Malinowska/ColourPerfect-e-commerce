from products.models import Product
from wishlist.models import WishlistItem


def get_products(season, order, request):
    '''gets 3 products for each season and then returns a list of tuples with product object and colour object'''
    season_products = Product.objects.filter(product_colors__season=season.lower(
    )).prefetch_related('product_colors').distinct().order_by(order)[:3]
    col_prod = []
    for product in season_products:
        colour = product.product_colors.filter(season=season.lower()).last()
        on_wishlist = False
        if request.user.is_authenticated: 
            on_wishlist = WishlistItem.objects.filter(wishlist__owner=request.user, product=product).exists()
        col_prod.append((product, colour, on_wishlist))
    return col_prod
