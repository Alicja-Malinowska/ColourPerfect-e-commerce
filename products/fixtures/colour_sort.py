
import os
import json
from colour_conv import match_colours


def adjust_colours(filepath):

    product_types_with_colours = ["blush", "bronzer", "eyeshadow", "lip_liner", "lipstick", "nail_polish"]
    
    with open(filepath, 'r', encoding='utf-8',
                 errors='ignore') as fp:
        products = json.load(fp)

    for product in products:
        if product["product_type"] in product_types_with_colours:
            product["product_colors"] = [match_colours(product)]


    with open(filepath, 'w') as fp:
        json.dump(products, fp, indent=2)

script_dir = os.path.dirname(__file__)
rel_path = "products.json"
abs_file_path = os.path.join(script_dir, rel_path)



adjust_colours(abs_file_path)