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

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def exploring_path_scene():
    
    print("\nOh, what is that noise?")
    sleep(3.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
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
    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('step closer to fountain', fountain_scene), # If you want option 1 to lead to a continuation_scene
        ('stay safe at a distance', growling_scene)   # If you want option 2 to exit this scene and continue the game
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
        ('drink from the fountain', refreshed_scene), # If you want option 1 to lead to a continuation_scene
        ('throw a coin in for good luck', coin_scene)   # If you want option 2 to exit this scene and continue the game
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

    coin_roll = chance_roll(25) # You can use a chance roll like this, where 25 is the probability of success
    
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
        # When you are ready to end the scene, return:
        #   None:  to continue the game
        #   True:  to win the game
        #   False: to lose the game
    
    else:
        
        print("\nI feel like I might have more luck on my journey ahead")
        sleep(2.0)
        next_scene = choose_option([
            ('throw another coin', coin_scene), # If you want option 1 to lead to a continuation_scene
            ('return to the road', None)   # If you want option 2 to exit this scene and continue the game
        ])

        return next_scene