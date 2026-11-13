"""
WITHOUT PROTOTYPE  -  what goes wrong
-------------------------------------
Every copy is built from scratch, and "copying by hand" is fragile.
"""
import time


class Invitation:
    def __init__(self, guest, events):
        print("  (slow setup: loading design, fonts, images...)")
        time.sleep(0.5)      #this is expensive work say creation of images, loading fonts, etc
        self.guest = guest
        self.events = events

    def __str__(self):
        return f"Dear {self.guest}, join us for: {', '.join(self.events)}"


# ---------- Problem 1: repeat the expensive work for every guest ----------
print("Creating 3 invitations from scratch:")
start = time.perf_counter()
guests = ["Selvam", "Priya", "Karthik"]
cards = [Invitation(g, ["Engagement", "Wedding", "Reception"]) for g in guests]
print(f"Took {time.perf_counter() - start:.1f}s for 3 cards. For 500 guests? Minutes.\n")

# ---------- Problem 2: "just reuse the same object" ----------
card = Invitation("TEMPLATE", ["Engagement", "Wedding", "Reception"])
shared = [card, card, card]                 # 3 'cards' but ONE object
shared[0].guest = "Selvam"
shared[1].guest = "Priya"
print("All three are the same object:", [str(c) for c in shared])

# ---------- Problem 3: copying by hand ----------
def manual_copy(inv):
    new = Invitation.__new__(Invitation)    # skip slow setup
    new.guest = inv.guest
    new.events = inv.events                 # same list! not a real copy
    return new                              # and if we add a field later, we forget it here

a = card
b = manual_copy(card)
b.events.remove("Reception")
print("\nEdited b's events, but the original changed too:", a)

# PROBLEMS
# 1. Slow: expensive setup is repeated for every object.
# 2. Sharing one object means changing one changes all.
# 3. Hand-written copy code is easy to get wrong (shared lists, forgotten fields).
