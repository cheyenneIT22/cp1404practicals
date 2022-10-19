COLOUR_to_CODE = {"AliceBlue:""#f0f8ff", "Alizarin crimson:""#e32636","Amethyst:""#9966cc","Baby pink:""#f4c2c2",
               "Banana Mania:""#fae7b5"}
# remember to put colour before I finish
colour = input("Colour: ")
while colour != "":
    print(f"the code for \"{colour}\" is {COLOUR_to_CODE.get(colour)}")
    colour = input("Colour: ")

