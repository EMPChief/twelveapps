
class SceneRouter:
    def __init__(self):
        self._scenes = {}
        
    def register_scene(self, scene_name, scene_function):
        """Register a scene function with a given name."""
        self._scenes[scene_name] = scene_function
        
    def go_to_scene(self, scene_name):
        """Navigate to a registered scene."""
        if scene_name in self._scenes:
            self._scenes[scene_name]()
        else:
            print(f"Error: Scene '{scene_name}' not found")

# Create global router instance
router = SceneRouter()

# Convenience functions for backward compatibility
def go_to_town():
    router.go_to_scene("town")

def go_to_shop():
    router.go_to_scene("shop")
    
def go_to_tavern():
    router.go_to_scene("tavern")

def go_to_spaceship():
    router.go_to_scene("spaceship")

def register_town_function(func):
    router.register_scene("town", func)

def register_shop_function(func):
    router.register_scene("shop", func)

def register_tavern_function(func):
    router.register_scene("tavern", func)

# Generic scene registration
def register_scene(scene_name, func):
    router.register_scene(scene_name, func)