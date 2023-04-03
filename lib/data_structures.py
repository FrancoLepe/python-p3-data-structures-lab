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
       return [item["name"] for item in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [item for item in spicy_foods if item ["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        name = item["name"]
        cuisine = item["cuisine"]
        heat_level = "🌶" * item["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
  for item in spicy_foods:
      if item["heat_level"] > 5:
        name = item["name"]
        cuisine = item["cuisine"]
        heat_level = "🌶" * item["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    total_heat = sum([food["heat_level"] for food in spicy_foods])
    average_level = total_heat / len(spicy_foods)
    return average_level

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food) 
    return spicy_foods