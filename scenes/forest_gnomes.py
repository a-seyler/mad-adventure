"""
=====================================================================
  Scenes / Forest Gnomes
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register
def forest_gnomes_scene():
    
    print(f"\nI can see some strange shadows...")
    sleep(2.0)
    print("They look like people, but very small...", end=' ', flush=True)
    sleep(2.0)
    print("are they FOREST GNOMES?")
    sleep(1.0)
    print("\nThey are dancing!")
    sleep(1.0)

    next_scene = choose_option([
        ('join the dance', dance_scene),
        ('ignore them and keep walking', None)
    ])

    return next_scene

# -----------------------------------------------

def dance_scene():
    
    print(f"\nThis music is so funky!")
    sleep(3.0)
    print(f"These forest gnomes are my new best friends!")
    sleep(2.0)
    print(f"\nHahaha well this is fun, but I would like to stop now")
    sleep(1.0)

    dance_fever = chance_roll(25)
    
    if dance_fever:
        print(f"What is happening?? I CAN'T STOP!")
        sleep(1.0)
        print(f"I CANNOT STOP DANCING!")
        sleep(1.0)     
        print(f"I CANNOT STOP DANCING!")
        sleep(1.0)   
        print(f"I CANNOT STOP DANCING!")
        sleep(1.0)  
        print(f"Oh finally... I better leave these gnomes before they cast another spell")
        sleep(1.0)

        return None
    
    else:

        return None