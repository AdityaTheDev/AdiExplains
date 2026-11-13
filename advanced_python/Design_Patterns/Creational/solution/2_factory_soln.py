"""
FACTORY  -  "Tell the shop WHAT you want, not HOW to make it"
-------------------------------------------------------------
You order "a coffee" at a cafe. You don't go into the kitchen and
build it yourself. The cafe (factory) decides how to make it.
In code: you ask for "email" or "sms", the factory gives you the right object.
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


# ---------------- The Factory ----------------
def create_notification(kind):
    if kind == "email":
        return EmailNotification()
    if kind == "sms":
        return SMSNotification()
    if kind == "whatsapp":
        return WhatsAppNotification()
    raise ValueError(f"We don't support '{kind}' yet")



# ---------------- Using it ----------------
# The user's setting decides the type. Our code below never changes.
for user_choice in ["email", "sms", "whatsapp"]:
    notifier = create_notification(user_choice)    # we don't care HOW it's made
    notifier.send("Your order has shipped!")

# Without a factory you would write if/else everywhere in your app.
# With a factory, that decision lives in ONE place.
