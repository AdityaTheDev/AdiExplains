"""
WITHOUT SINGLETON  -  what goes wrong
-------------------------------------
Every module creates its own Logger. Looks harmless... until you read the log.
"""


class Logger:
    def __init__(self):
        self.messages = []

    def log(self, text):
        self.messages.append(text)


# login.py creates its own logger
login_logger = Logger()
login_logger.log("User Selvam logged in")

# payment.py creates ANOTHER one
payment_logger = Logger()
payment_logger.log("Payment of Rs.499 received")

print("Same object?        ", login_logger is payment_logger)   # False
print("Login's log file:   ", login_logger.messages)
print("Payment's log file: ", payment_logger.messages)

# PROBLEM: the story of one user is split across two loggers.
# Debugging "what happened before the payment?" is now impossible, because
# the login message is in a different place.
# Same issue with config (two modules see different settings) or a DB
# connection pool (100 modules = 100 pools = database crashes).
