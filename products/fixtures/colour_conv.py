from colour import Color
from validators import is_hex_color


def assign_season(hex_val):


    ''' takes a hex colour value as a string and returns the
    beauty type (season), also as a string,
    based on different tresholds of saturation
    and lightness and thair combinations'''

    if is_hex_color(hex_val):
        c = Color(hex_val)
        s = c.hsl[1]
        l = c.hsl[2]

        if s <= 0.25:
            if l > 0.3:
                return "summer"
            else:
                return "winter"
        elif s >= 0.75:
            if l <= 0.30:
                return "winter"
            elif l <= 0.60:
                return "autumn"
            elif l <= 0.90:
                return "spring"
            else:
                return "summer"
        else:
            if l <= 0.35:
                return "winter"
            elif l <= 0.5:
                return "autumn"
            elif l <= 0.7:
                return "spring"
            else:
                return "summer"


def match_colours(obj):
    ''' takes an object, goes through its colours, and
    sorts them, depending to which season they belong
    '''
    new_prod_colors = {
        "spring": [],
        "summer": [],
        "autumn": [],
        "winter": []
    }

    for colour in obj["product_colors"]:
        season = assign_season(colour["hex_value"])
        if season:
            new_prod_colors[season].append(colour)

    return new_prod_colors

