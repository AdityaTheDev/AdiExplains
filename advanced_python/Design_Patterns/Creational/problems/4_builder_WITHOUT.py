"""
WITHOUT BUILDER  -  what goes wrong
-----------------------------------
Two common (bad) ways to create an object with many options.
"""


# ---------- Bad way 1: the giant constructor ("telescoping constructor") ----------
class Pizza:
    def __init__(self, size="medium", crust="regular", toppings=None,
                 extra_cheese=False, extra_sauce=False, stuffed_crust=False,
                 gluten_free=False):
        self.size = size
        self.crust = crust
        self.toppings = toppings or []
        self.extra_cheese = extra_cheese
        self.extra_sauce = extra_sauce
        self.stuffed_crust = stuffed_crust
        self.gluten_free = gluten_free


# Can you tell what each True/False means? Neither can your teammate.
p = Pizza("large", "thin", ["paneer", "capsicum"], True, False, True, False)
print("Order 1 (unreadable):", vars(p))

# Swap two booleans by mistake - Python won't warn you:
wrong = Pizza("large", "thin", ["paneer"], False, True)   # wanted extra CHEESE
print("Order 2 (silent bug):", "extra_cheese =", wrong.extra_cheese)


# ---------- Bad way 2: create empty, then set things one by one ----------
class Pizza2:
    pass


half = Pizza2()
half.size = "large"
# ...developer got interrupted, forgot crust and toppings...
try:
    print(half.crust)
except AttributeError as e:
    print("\nHalf-built object crashes later:", e)

# PROBLEMS
# 1. Unreadable calls, easy to put arguments in the wrong order.
# 2. Adding one more option changes every call that follows the position.
# 3. Half-built objects can slip into the program and crash far from the cause.
