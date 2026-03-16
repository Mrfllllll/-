def product_integers(*args):
    product = 1
    found_int = False

    for x in args:
        if type(x) == int:
            product = product * x
            found_int = True

    if found_int:
        return product
    else:
        return None


print(product_integers(2, "a", 3, 1.5, 4))
print(product_integers("x", 2.2, True))
print(product_integers("x", 2.2))
