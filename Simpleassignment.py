# All ran in pyhon3.10
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object
True
rgba.append("Alph")
rgb
["Red", "Green", "Blue", "Alph"]

