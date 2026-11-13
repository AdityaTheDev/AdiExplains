"""
PROTOTYPE  -  "Photocopy the form instead of writing it again"
--------------------------------------------------------------
You have one wedding invitation designed perfectly.
For 100 guests you don't redesign it 100 times.
You COPY it and only change the guest's name.
In code: copy an existing object, then tweak the copy.
"""
import copy


class Invitation:
    def __init__(self, guest, events):
        self.guest = guest
        self.events = events                # a list (important in a moment!)

    def clone(self):
        return copy.deepcopy(self)          # a fully independent copy

    def __str__(self):
        return f"Dear {self.guest}, join us for: {', '.join(self.events)}"


# ---------------- Original template (built once) ----------------
template = Invitation("GUEST NAME", ["Engagement", "Wedding", "Reception"])

# ---------------- Make copies, change only what differs ----------------
for name in ["Selvam", "Priya", "Karthik"]:
    card = template.clone()
    card.guest = name
    print(card)

# One guest can't attend the reception. Edit THEIR card only.
priya = template.clone()
priya.guest = "Priya"
priya.events.remove("Reception")
print("\nPriya's card:  ", priya)
print("Template safe: ", template)          # still has Reception

# ---------------- The trap beginners fall into ----------------
bad_copy = copy.copy(template)              # SHALLOW copy: shares the same list!
bad_copy.events.remove("Engagement")
print("\nShallow copy damaged the template:", template)
# Rule: if your object contains lists or dicts, use deepcopy.
