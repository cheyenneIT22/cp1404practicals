"""Hex colours program"""
COLOUR_to_CODE = {"AliceBlue:""#f0f8ff", "Alizarin crimson:""#e32636", "Amethyst:""#9966cc", "Baby pink:""#f4c2c2",
                  "Banana Mania:""#fae7b5", "Absolute Zero:" "#0048ba", "Bitter sweet shimmer:""bf4f51",
                  "Black Coffee:""3b2f2f"}
colour = input("Colour: ")
while colour != "":
    print(f"the code for \"{colour}\" is {COLOUR_to_CODE.get(colour)}")
    colour = input("Colour: ")
