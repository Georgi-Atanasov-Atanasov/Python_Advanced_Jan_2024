def shopping_cart(*args):
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    result = ""

    for data in args:
        if data == "Stop":
            break
        else:
            meal, product = data
            if product not in cart[meal]:
                if meal == "Pizza":
                    if len(cart[meal]) < 4:
                        cart[meal].append(product)
                    else:
                        continue
                elif meal == "Soup":
                    if len(cart[meal]) < 3:
                        cart[meal].append(product)
                    else:
                        continue
                elif meal == "Dessert":
                    if len(cart[meal]) < 2:
                        cart[meal].append(product)
                    else:
                        continue

    sorted_cart = dict(sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])))
    if not any(sorted_cart.values()):
        return "No products in the cart!"

    for meal, products in sorted_cart.items():
        result += f"{meal}:\n"
        for product in sorted(list(products)):
            result += f" - {product}\n"
    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
