import re

def is_hex_color(string):

    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', string)

    return True if match else False
