"""
=====================================================================
  Scenes / Fountain Scene
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    
def exploring_path_scene():
    
    print("\nOh, what is that noise?")
    sleep(3.0)
    print("I stop and close my eyes to concentrate on the sound...")
    sleep(3.0)
    print("It's coming from a little side path which leads through ...", end=' ', flush=True)
    sleep(3.0)
    print("some bushes and ...")
    sleep(3.0)
    print("I follow the path and force my way through thick shrubs and ...")
    sleep(3.0)
    print("I arrive at a clearing and see a fountain, with water sparkling in the sun")
    sleep(3.0)

    next_scene = choose_option([
        ('step closer to fountain', fountain_scene), 
        ('stay safe at a distance', growling_scene)   
    ])

    return next_scene

# -----------------------------------------------

def growling_scene():
    print("\nI hear a loud and scary growling noise behind me and ...", end=' ', flush=True)
    sleep(3.0)
    print("step closer to the fountain...")
    sleep(2.0)
    return fountain_scene()

def fountain_scene():
    print("\nThe water looks cool and refreshing...")
    sleep(2.0)
    next_scene = choose_option([
        ('drink from the fountain', refreshed_scene), 
        ('throw a coin in for good luck', coin_scene)  
    ])
    return next_scene

def refreshed_scene():
    print("\nI feel so refreshed... ", end=' ', flush=True)
    sleep(2.0)
    print("I am returning to the road and continue my walk...")
    sleep(2.0)
    next_scene = None
    
    return next_scene

def coin_scene():
    
    print("\nI am throwing a coin into the well")
    sleep(1.0)

    coin_roll = chance_roll(20) 
    
    if coin_roll:
        
        print("\n'Hey!", end=' ', flush=True)
        sleep(1.0)
        print("'You hit my eye' says...", end=' ', flush=True)
        sleep(2.0)
        print("a big green frog.")
        sleep(2.0)
        print("\nHe throws the coin back at you... ", end=' ', flush=True)
        sleep(2.0)
        print("And hits your head!")
        sleep(5.0)
        print("\nAfter awaking from blackout I return to the road...")

        return None
    
    else:
        
        print("\nI feel like I might have more luck on my journey ahead")
        sleep(2.0)
        next_scene = choose_option([
            ('throw another coin', coin_scene), 
            ('return to the road', None)   
        ])

        return next_scene