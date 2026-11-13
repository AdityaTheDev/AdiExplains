"""
ABSTRACT FACTORY  -  "Combo meals: everything matches"
------------------------------------------------------
Order a South Indian combo -> you get Idli + Filter Coffee.
Order a North Indian combo -> you get Paratha + Lassi.
Nobody wants Idli with Lassi! A factory gives a MATCHING SET of items.

Factory          = makes ONE thing (a notification).
Abstract Factory = makes a FAMILY of things that belong together.
"""


# ---------------- South Indian family ----------------
class Idli:
    def serve(self):
        return "Idli with sambar"


class FilterCoffee:
    def serve(self):
        return "Filter coffee"


class SouthIndianMeal:                      # factory #1
    def make_food(self):
        return Idli()

    def make_drink(self):
        return FilterCoffee()


# ---------------- North Indian family ----------------
class Paratha:
    def serve(self):
        return "Aloo paratha with curd"


class Lassi:
    def serve(self):
        return "Sweet lassi"


class NorthIndianMeal:                      # factory #2
    def make_food(self):
        return Paratha()

    def make_drink(self):
        return Lassi()


# ---------------- The customer code ----------------
def serve_breakfast(meal_factory):
    food = meal_factory.make_food()
    drink = meal_factory.make_drink()
    print(" -", food.serve())
    print(" -", drink.serve())


print("South Indian combo:")
serve_breakfast(SouthIndianMeal())

print("North Indian combo:")
serve_breakfast(NorthIndianMeal())

# serve_breakfast() doesn't know which cuisine it got.
# Add a "Chinese combo" later = new classes only. This function stays untouched.
