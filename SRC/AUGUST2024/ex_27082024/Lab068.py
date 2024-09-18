def make_pizza(*topping, base):
    print(topping, base)

def make_pizza2(*topping, base):
    print(base,topping)

make_pizza("mushroom","tomato","cheese",base="thin crust")
make_pizza2("dsfads","dfdgfg","asfdgghh",base="crust")