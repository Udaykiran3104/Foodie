
from typing_extensions import Annotated
import typer
from shop.services.restaurant import RestaurantService

restaurant_service = RestaurantService()

app = typer.Typer()

@app.command()
def add_restaurant(
    name: Annotated[str, typer.Option(prompt=True)],
):
    restaurant_service.add_restaurant(name)

@app.command()
def remove_restaurant(
    name: Annotated[str, typer.Option(prompt=True)]
):
    restaurant_service.remove_restaurant(name)

@app.command()
def display_restaurants():
    restaurant_service.display_restaurants()

@app.command()
def list_foods(
    restaurant_name: Annotated[str, typer.Option(prompt=True)],
):
    restaurant_service.list_foods(restaurant_name)

if __name__ == "__main__":
    app()


