# Step 1: Component Interface
class Meal:
    def get_description(self) -> str:
        pass

    def get_cost(self) -> float:
        pass


# Step 2: Concrete Component
class BasicMeal(Meal):
    def get_description(self) -> str:
        return "Basic Meal"

    def get_cost(self) -> float:
        return 5.00


# Step 3: Decorator (abstract)
class MealDecorator(Meal):
    def __init__(self, meal: Meal):
        self._meal = meal

    def get_description(self) -> str:
        return self._meal.get_description()

    def get_cost(self) -> float:
        return self._meal.get_cost()


# Step 4: Concrete Decorators
class Cheese(MealDecorator):
    def get_description(self) -> str:
        return self._meal.get_description() + ", with cheese"

    def get_cost(self) -> float:
        return self._meal.get_cost() + 1.25


class Soup(MealDecorator):
    def get_description(self) -> str:
        return self._meal.get_description() + ", plus soup"

    def get_cost(self) -> float:
        return self._meal.get_cost() + 2.00


class Dessert(MealDecorator):
    def get_description(self) -> str:
        return self._meal.get_description() + ", and dessert"

    def get_cost(self) -> float:
        return self._meal.get_cost() + 3.50


# Step 5: Client Code
if __name__ == "__main__":
    # Start with the base meal
    meal = BasicMeal()

    # Add cheese
    meal = Cheese(meal)

    # Add soup
    meal = Soup(meal)

    # Add dessert
    meal = Dessert(meal)

    print(f"Order: {meal.get_description()}")
    print(f"Total cost: ${meal.get_cost():.2f}")
