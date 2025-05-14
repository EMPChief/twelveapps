"""Player management and state."""
from utils.printing import typewriter_print
from collections import Counter
from config import (
    PLAYER_MAX_HEALTH,
    PLAYER_STARTING_GOLD,
    PLAYER_STARTING_INVENTORY
)
import time

class Player:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset player to initial state."""
        self.name = ""
        self.health = PLAYER_MAX_HEALTH
        self.gold = PLAYER_STARTING_GOLD
        self.inventory = PLAYER_STARTING_INVENTORY.copy()
        self.progress = {
            "level": 1,
            "quests_completed": [],
            "locations_discovered": ["town"],
            "shop_tier": 1,
            "milestones": []
        }
    
    def heal(self, amount):
        """Heal the player by a certain amount."""
        self.health = min(PLAYER_MAX_HEALTH, self.health + amount)
        return self.health
    
    def damage(self, amount):
        """Damage the player by a certain amount."""
        self.health = max(0, self.health - amount)
        return self.health
    
    def poison_damage(self, amount, duration):
        """Damage the player over time with minimal spam."""
        for second in range(duration):
            self.health = max(0, self.health - amount)
            print(
                f"Poison damage... {amount} taken ({second + 1}/{duration}) | Health: {self.health}",
                end='\r'
            )
            time.sleep(1)
            if self.health <= 0:
                print()
                typewriter_print("You died from poison!")
                return False
        print()
        typewriter_print(f"You survived the poison. Health: {self.health}")
        return True
    
    def set_name(self, name):
        """Set the player's name."""
        self.name = name
    
    def unlock_milestone(self, milestone_id):
        """Add a milestone to track player progress."""
        if milestone_id not in self.progress["milestones"]:
            self.progress["milestones"].append(milestone_id)
            return True
        return False
    
    def get_level(self):
        """Get the player's current level."""
        return self.progress["level"]
    
    def level_up(self):
        """Increase the player's level."""
        self.progress["level"] += 1
        return self.progress["level"]
    
    def set_shop_tier(self, tier):
        """Set the shop tier level."""
        self.progress["shop_tier"] = tier
        return tier
    
    def get_shop_tier(self):
        """Get the current shop tier."""
        return self.progress["shop_tier"]
    
    def complete_quest(self, quest_id):
        """Mark a quest as completed."""
        if quest_id not in self.progress["quests_completed"]:
            self.progress["quests_completed"].append(quest_id)
            return True
        return False
    
    def discover_location(self, location):
        """Add a location to discovered locations."""
        if location not in self.progress["locations_discovered"]:
            self.progress["locations_discovered"].append(location)
            return True
        return False
    
    def display_status(self):
        """Display player status including health, gold and inventory."""
        typewriter_print("=======================================")
        typewriter_print(
            f"Name: {self.name} | Health: {self.health} | Gold: {self.gold}"
        )
        
        if self.inventory:
            inventory_counts = Counter(self.inventory)
            formatted_inventory = [
                f"{item} x{count}" if count > 1 else item
                for item, count in inventory_counts.items()
            ]
            typewriter_print(f"Inventory: {', '.join(formatted_inventory)}")
        
        typewriter_print("=======================================")


player = Player()


def set_player_name(name):
    player.set_name(name)

def health_gold_name():
    player.display_status()

def player_heal(amount):
    return player.heal(amount)

def player_damage(amount):
    return player.damage(amount)

def poison_damage(amount, duration):
    return player.poison_damage(amount, duration)
