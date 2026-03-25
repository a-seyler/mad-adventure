"""
=====================================================================
  Scenes / Flower Seller
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option
from utils import sleep

# ===== Scene =======================================================

@register
def flower_seller_scene():

    print(f"\nOh! there is a distinctive smell, I love it...", end=' ')
    sleep(2.0)
    print("is that geranium?!")
    sleep(1.0)
    print("Seems like a FLOWER SELLER, huh")
    sleep(2.0)
    print('"Look what we have here, a brave traveller...', end=' ')
    sleep(1.0)
    print('would you like to buy some flowers?"')

    next_scene = choose_option([
        ('buy a flower', buy_flower),
        ('keep walking', None)
    ])

    return next_scene

# -----------------------------------------------

def buy_flower():
    print("\nI really like geraniums...", end=" ")
    sleep(1.0)
    print("I used to have one called Dani...")
    sleep(1.0)
    print("Thanks a lot! I will resume my journey now.")

    return None

# -----------------------------------------------
