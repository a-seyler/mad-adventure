"""
=====================================================================
  Scenes / Registry
=====================================================================

Provides the registry of available scenes, and a register to
automatically add them to the registry when imported.
"""

SCENES_POOL = []

def register(scene):
    """Add a scene to the registry"""
    SCENES_POOL.append(scene)
    return scene
