def get_ingredients(filepath = "ingredientList.txt"):
    with open(filepath, 'r') as file_local:
        ingredients_local = file_local.readlines()
    return ingredients_local

def write_ingredients(ingredients_arg, filepath = "ingredientList.txt"):
    with open(filepath, 'w') as file:
        file.writelines(ingredients_arg)