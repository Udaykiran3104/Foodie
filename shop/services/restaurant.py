  
from shop.models import Restaurant, Food
from rich.console import Console
from rich.table import Table

console = Console()


class RestaurantService:
    def add_restaurant(self, name: str):
        restaurant = Restaurant.create(name=name)
        print(f"Restaurant '{restaurant.name}' added successfully.")
        



    def remove_restaurant(self, name: str):
        try:
            restaurant = Restaurant.get(name=name)
            restaurant.delete_instance()
            print(f"Restaurant '{restaurant.name}' has been removed from the restaurant list.")
        except Restaurant.DoesNotExist:
            print(f"Restaurant '{name}' does not exist.")

    def display_restaurants(self):
        restaurants = Restaurant.select()

        table = Table("sl.No.", "Name", "Restaurant-id")
        for i, restaurant in enumerate(restaurants):
            table.add_row(
                f"{i + 1}",
                restaurant.name,
                str(restaurant.id),
            )

        console.print(table)

    def list_foods(self, restaurant_name: str):
        try:
            restaurant = Restaurant.get(name=restaurant_name)
            foods = Food.select().where(Food.restaurant == restaurant)

            if foods.count() == 0:
                print(f"No food items found for restaurant '{restaurant_name}'.")
                return

            table = Table("sl.No.", "Name", "Price", "Is Veg", "Food-id")
            for i, food in enumerate(foods):
                table.add_row(
                    f"{i + 1}",
                    food.name,
                    str(food.price),
                    "Yes" if food.is_veg else "No",
                    str(food.id),
                )

            console.print(f"Food items for restaurant '{restaurant_name}':")
            console.print(table)
        except Restaurant.DoesNotExist:
            print(f"Restaurant '{restaurant_name}' does not exist.")