def get_names(spicy_foods):
    """
    Returns a list of strings with the names of each spicy food.
    """
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of dictionaries where the heat level of the food is greater than 5.
    """
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """
    Outputs to the terminal each spicy food in the specified format.
    """
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary for the spicy food whose cuisine matches the input cuisine.
    """
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    """
    Outputs to the terminal only the spicy foods that have a heat level greater than 5.
    """
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    """
    Returns an integer representing the average heat level of all the spicy foods in the array.
    """
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy_food to the original list and returns the updated list.
    """
    spicy_foods.append(spicy_food)
    return spicy_foods

