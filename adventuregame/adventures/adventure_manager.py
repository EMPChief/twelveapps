"""Space adventure management system."""
from utils.printing import typewriter_print, clear_screen
import time
import random
import json
import os

def get_data_path(filename):
    """Get absolute path to a data file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'data', filename)

def load_json_file(filepath):
    """Load and return JSON data from a file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find file {filepath}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {filepath}")
        raise

def get_available_adventures(player):
    """Get list of adventures available to the player based on level and completed milestones."""
    available = {}
    adventures = load_json_file(get_data_path('adventures.json'))
    milestones = load_json_file(get_data_path('milestones.json'))
    
    for adv_id, adventure in adventures.items():
        if player.get_level() < adventure["min_level"]:
            continue
            
        # Check if previous milestone is completed
        if adventure["min_level"] > 1:
            prev_milestone = None
            for milestone in milestones:
                if adv_id in milestones[milestone]["unlocks"]:
                    prev_milestone = milestone
                    break
            
            if prev_milestone and prev_milestone not in player.progress["milestones"]:
                continue
        
        available[adv_id] = adventure
            
    return available

def display_adventure_info(adventure):
    """Display detailed information about an adventure."""
    rewards = load_json_file(get_data_path('rewards.json'))
    reward_data = rewards[adventure['reward_id']]
    
    typewriter_print(f"=== {adventure['name']} ===")
    typewriter_print(adventure["description"])
    typewriter_print(f"Required Level: {adventure['min_level']}")
    typewriter_print("\nPotential Rewards:")
    typewriter_print(f"- Credits: {reward_data['gold']}")
    typewriter_print(f"- Experience: {reward_data['experience']}")
    typewriter_print("- Possible Items:")
    for item in reward_data["items"]:
        typewriter_print(f"  * {item}")
    typewriter_print("==================")

def process_scene_effects(player, scene, choice_data):
    """Process any effects from the scene or choice."""
    effects = []
    
    # Handle damage
    if "damage" in scene:
        player.damage(scene["damage"])
        effects.append(f"Took {scene['damage']} damage!")
    if "damage" in choice_data:
        player.damage(choice_data["damage"])
        effects.append(f"Took {choice_data['damage']} damage!")
    
    # Handle healing
    if "heal" in choice_data:
        player.heal(choice_data["heal"])
        effects.append(f"Healed for {choice_data['heal']} health!")
    
    # Handle loot
    if "loot" in choice_data:
        for item in choice_data["loot"]:
            player.inventory.append(item)
            effects.append(f"Found {item}!")
    
    # Handle bonus XP
    if "bonus_xp" in choice_data:
        for _ in range(choice_data["bonus_xp"] // 50):
            player.level_up()
        effects.append(f"Gained {choice_data['bonus_xp']} experience!")
    
    # Handle reveals
    if "reveals" in choice_data:
        effects.append(choice_data["reveals"])
    
    return effects

def handle_choice(player, scene, choice_data):
    """Process a player's choice and determine the outcome."""
    # Check if choice requires an item
    if "requires_item" in choice_data:
        if choice_data["requires_item"] not in player.inventory:
            typewriter_print(f"You need a {choice_data['requires_item']} for this action!")
            return None, []
    
    # Handle success rate checks
    if "success_rate" in choice_data:
        if random.random() < choice_data["success_rate"]:
            outcome = choice_data["success"]
            if isinstance(outcome, dict):
                effects = process_scene_effects(player, scene, outcome)
                return outcome["leads_to"], effects
            return outcome, []
        else:
            outcome = choice_data["failure"]
            if isinstance(outcome, dict):
                effects = process_scene_effects(player, scene, outcome)
                return outcome["leads_to"], effects
            return outcome, []
    
    # Handle direct transitions
    if "leads_to" in choice_data:
        effects = process_scene_effects(player, scene, choice_data)
        return choice_data["leads_to"], effects
    
    return None, []

def run_adventure(player, adventure_id):
    """Run an interactive adventure with choices and consequences."""
    adventures = load_json_file(get_data_path('adventures.json'))
    adventure = adventures[adventure_id]
    
    # Load adventure-specific scenes
    scenes_path = os.path.join(get_data_path(adventure_id), 'scenes.json')
    scenes = load_json_file(scenes_path)
    current_scene = adventure["starting_scene"]
    
    while True:
        clear_screen()
        player.display_status()
        
        scene = scenes[current_scene]
        typewriter_print(f"\n{scene['description']}")
        
        # Display choices
        typewriter_print("\nWhat would you like to do?")
        for num, choice in scene["choices"].items():
            typewriter_print(f"{num}. {choice['text']}")
        
        # Get player choice
        try:
            choice = input("\nEnter your choice: ").strip()
            
            if choice not in scene["choices"]:
                typewriter_print("Invalid choice. Please try again.")
                time.sleep(1)
                continue
            
            # Process choice
            next_scene, effects = handle_choice(player, scene, scene["choices"][choice])
            
            # Display effects
            for effect in effects:
                typewriter_print(effect)
                time.sleep(1)
            
            # Check for death
            if player.health <= 0:
                typewriter_print("\nCritical system failure! Mission failed.")
                time.sleep(2)
                return False
            
            # Move to next scene
            if next_scene:
                current_scene = next_scene
                
                # Check if this is a final scene
                if "final_scene" in scenes[current_scene]:
                    typewriter_print(f"\n{scenes[current_scene]['description']}")
                    time.sleep(2)
                    return scenes[current_scene]["success"]
            
            time.sleep(1)
            
        except (EOFError, KeyboardInterrupt):
            typewriter_print("\nEmergency evacuation initiated!")
            time.sleep(1)
            return False

def complete_adventure(player, adventure_id):
    """Handle adventure completion and rewards."""
    adventures = load_json_file(get_data_path('adventures.json'))
    rewards = load_json_file(get_data_path('rewards.json'))
    
    adventure = adventures[adventure_id]
    reward_data = rewards[adventure['reward_id']]
    
    # Give rewards
    player.gold += reward_data["gold"]
    for item in reward_data["items"]:
        player.inventory.append(item)
    
    # Add experience (level up if needed)
    for _ in range(reward_data["experience"] // 50):
        player.level_up()
    
    # Mark milestone as completed
    player.unlock_milestone(adventure["completion_milestone"])
    
    # Display rewards
    clear_screen()
    typewriter_print("=== Mission Complete ===")
    typewriter_print("\nMission Rewards:")
    typewriter_print(f"- {reward_data['gold']} credits")
    typewriter_print(f"- {reward_data['experience']} experience points")
    for item in reward_data["items"]:
        typewriter_print(f"- {item}")
    
    if reward_data["experience"] >= 50:
        typewriter_print(f"\nLevel up! You are now level {player.get_level()}")
    
    time.sleep(2) 