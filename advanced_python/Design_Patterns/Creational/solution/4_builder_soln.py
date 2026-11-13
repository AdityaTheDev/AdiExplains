"""
BUILDER  -  "Build your own pizza, one choice at a time"
--------------------------------------------------------
At a pizza counter you don't shout 8 things in one breath.
You choose step by step: size, crust, toppings, extra cheese.
In code: when an object has many OPTIONS, build it step by step.

Without it you get monsters like:
    Pizza("large", "thin", True, False, ["corn"], None, True)   # what is True??
"""


class Pizza:
    def __init__(self):
        self.size = "medium"
        self.crust = "regular"
        self.toppings = []
        self.extra_cheese = False

    def __str__(self):
        cheese = " + extra cheese" if self.extra_cheese else ""
        toppings = ", ".join(self.toppings) or "no toppings"
        return f"{self.size} {self.crust}-crust pizza with {toppings}{cheese}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def size(self, size):
        self.pizza.size = size
        return self                         # returning self lets us chain calls

    def crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def extra_cheese(self):
        self.pizza.extra_cheese = True
        return self

    def build(self):
        return self.pizza


# ---------------- Using it: reads like English ----------------
my_pizza = (
    PizzaBuilder()
    .size("large")
    .crust("thin")
    .add_topping("paneer")
    .add_topping("capsicum")
    .extra_cheese()
    .build()
)
print("Order 1:", my_pizza)

plain_pizza = PizzaBuilder().build()        # skip everything = sensible defaults
print("Order 2:", plain_pizza)
