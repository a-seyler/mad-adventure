"""
=====================================================================
  Scenes / Wake up
=====================================================================

Starting scene for the game
"""

from engine import choose_option
from utils import sleep

# ===================================================================

def wake_up_scene():
    print("\nI open my eyes...", end=' ', flush=True)
    sleep(2.0)
    print("why am I lying on the ground?")
    sleep(2.0)
    print("there seems to be nothing around...", end=' ', flush=True)
    sleep(2.0)
    print("an empty road... where should I go?")

    choose_option([
        ("Go left" , None),
        ("Go right", None)
    ])

    print("\nLet's see what adventure awaits!")

    return None