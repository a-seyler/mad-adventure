"""
=====================================================================
  Scenes / Fun Mushrooms
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option
from utils import sleep

# ===== Scene =======================================================

@register
def fun_mushrooms_scene():
    
    print(f"\nA MUSHROOM FIELD!")
    sleep(2.0)
    print("I was feeling a little bit hungry...")
    sleep(1.0)

    next_scene = choose_option([
        ('eat some mushrooms', dizzy_state),
        ('keep walking', None)
    ])

    return next_scene

# -----------------------------------------------

def dizzy_state():
    
    print(f"\nOooh oOhH")
    sleep(3.0)
    print(f"Hmmm... I don't feel so good...")
    sleep(3.0)
    print(f"woooaah the coloours!")
    sleep(2.0)
    print(f"everything is movinnng......")
    sleep(2.0)
    print(f"...............")
    sleep(3.0)
    print(f"\nWell that was not my smartest idea")
    sleep(1.0)
    print(f"But I think I feel better now... I can keep walking...")

    return None