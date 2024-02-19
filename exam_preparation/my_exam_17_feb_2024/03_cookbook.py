def cookbook(*args):
    country = {}
    recipes = {}
    output = []

    for recipe_name, cuisine, ingredients in args:
        if cuisine not in country:
            country[cuisine] = [recipe_name]
        else:
            country[cuisine].append(recipe_name)

        recipes[recipe_name] = ingredients

    country_data = sorted(country.items(), key=lambda x: (-len(x[1]), x[0]))
    recipe_data = sorted(recipes.items(), key=lambda x: (x[0], x[1]))

    for cuisine, recipe_ in country_data:
        output.append(f"{cuisine} cuisine contains {len(recipe_)} recipes:")
        for recipe, ingredients in recipe_data:
            if recipe in recipe_:
              output.append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")
    return "\n".join(output)




print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
