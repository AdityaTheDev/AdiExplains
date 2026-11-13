"""
WITHOUT FACTORY  -  what goes wrong
-----------------------------------
The "which class?" decision is copy-pasted everywhere it is needed.
"""


class EmailNotification:
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SMSNotification:
    def send(self, message):
        print(f"Sending SMS: {message}")


class WhatsAppNotification:
    def send(self, message):
        print(f"Sending WHATSAPP: {message}")

class TelegramNotification:
    def send(self, message):
        print(f"Sending TELEGRAM: {message}")


# ---- orders.py ----
def notify_order_shipped(user_choice):
    if user_choice == "email":
        n = EmailNotification()
    elif user_choice == "sms":
        n = SMSNotification()
    elif user_choice == "whatsapp":
        n = WhatsAppNotification()
    elif user_choice == "telegram":
        n = TelegramNotification()
    n.send("Your order has shipped!")


# ---- payments.py ---- (same if/else, copy-pasted)
def notify_payment_received(user_choice):
    if user_choice == "email":
        n = EmailNotification()
    elif user_choice == "sms":
        n = SMSNotification()
    elif user_choice == "whatsapp":
        n = WhatsAppNotification()
    elif user_choice == "telegram":
            n = TelegramNotification()
    
    n.send("Payment received!")


# ---- offers.py ---- (and again... and a developer forgot "whatsapp")
def notify_new_offer(user_choice):
    if user_choice == "email":
        n = EmailNotification()
    elif user_choice == "sms":
        n = SMSNotification()
    elif user_choice == "telegram":
            n = TelegramNotification()
    n.send("50% off today!")


notify_order_shipped("sms")
notify_payment_received("whatsapp")

try:
    notify_new_offer("whatsapp")
except UnboundLocalError as e:
    print("\nBUG in offers.py:", e)

# PROBLEMS
# 1. Boss says: "Add Telegram." You must edit EVERY function and hope you
#    find them all. Miss one = a bug in production (like offers.py above).
# 2. Every module is tied to every concrete class.
# 3. Unknown choice? Each copy handles it differently (or crashes).
