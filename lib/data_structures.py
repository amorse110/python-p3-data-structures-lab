spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spicy_list = [food for food in spicy_foods if food["heat_level"] > 5]
    return spicy_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spicy_string = "{} ({}) | Heat Level: {}".format(food["name"], food["cuisine"], food["heat_level"] * "🌶")
        print(spicy_string)
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
# food_cuisine = [food for food in spicy_foods if food["cuisine"] == cuisine]
    #return food_cuisine[0]

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    spice_levels = [food["heat_level"] for food in spicy_foods]
    return (sum(spice_levels)/len(spice_levels))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
