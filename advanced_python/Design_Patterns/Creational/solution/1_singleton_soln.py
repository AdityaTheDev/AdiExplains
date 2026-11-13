"""
SINGLETON  -  "One school, one principal"
-----------------------------------------
A school can't have two principals giving different orders.
In code: some things must exist only ONCE. A Logger is the classic case:
every part of your app should write to the SAME log, not its own copy.
"""


class Logger:
    _instance = None        #remembers the one and only object

    def __new__(cls):
        if cls._instance is None:        #first time? create it
            print("Creating the Logger (happens only once)")
            cls._instance = super().__new__(cls)
            cls._instance.messages = []
        return cls._instance              # every other time? return the same one

    def log(self, text):
        self.messages.append(text)


# ---------------- Using it ----------------
login_module = Logger()
payment_module = Logger()

login_module.log("User Selvam logged in")
payment_module.log("Payment of Rs.499 received")

print("Same object?", login_module is payment_module)      # True
print("Everything in ONE place:", login_module.messages)
# Both messages appear together, because both modules use the same Logger.
