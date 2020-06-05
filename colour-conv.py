from colour import Color


def colour_match(hex_val):
''' takes a hex colour value as a string and returns the 
beauty type (season) based on different tresholds of saturation 
and lightness and thair combinations'''

    c = Color(hex_val)
    s = c.hsl[1]
    l = c.hsl[2]
    
    if s <= 0.25:
        if l > 0.3 :
            return "summer"
        else:
            return "winter"
    elif s >= 0.75:
        if l <= 0.30 :
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

print(colour_match("#ffcc00"))
    
    