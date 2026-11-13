"""
WITHOUT ABSTRACT FACTORY  -  what goes wrong
--------------------------------------------
The caller picks each item separately, so nothing stops a bad combination.
"""


class Idli:
    def serve(self):
        return "Idli with sambar"


class Paratha:
    def serve(self):
        return "Aloo paratha with curd"


class FilterCoffee:
    def serve(self):
        return "Filter coffee"


class Lassi:
    def serve(self):
        return "Sweet lassi"


def serve_breakfast(cuisine):
    # Developer must remember the right pairing for every cuisine, every time
    if cuisine == "south":
        food = Idli()
        drink = FilterCoffee()
    elif cuisine == "north":
        food = Paratha()
        drink = Lassi()
    print(" -", food.serve())
    print(" -", drink.serve())


print("Correct:")
serve_breakfast("south")

# Somewhere else, a tired developer builds the pieces by hand:
print("\nOther part of the app (mismatch!):")
food = Idli()          # south food...
drink = Lassi()        # ...north drink. Python doesn't complain.
print(" -", food.serve())
print(" -", drink.serve())

# PROBLEMS
# 1. Nothing enforces "these items belong together". The mistake is silent.
# 2. Add a "chinese" cuisine -> edit every if/elif in the whole codebase.
# 3. Real life: a Dark-theme button next to a Light-theme checkbox, or a
#    MySQL connection with a PostgreSQL query builder.
