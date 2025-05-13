from utils.printing import typewriter_print
player = {
    "name": "",
    "health": 100,
    "gold": 971,
    "inventory": [],
    "progress": {
        "level": 1,
        "quests_completed": [],
        "locations_discovered": ["town"],
        "shop_tier": 1,
        "milestones": []
    }
}

def set_player_name(name):
    player["name"] = name

def unlock_milestone(milestone_id):
    """Add a milestone to track player progress"""
    if milestone_id not in player["progress"]["milestones"]:
        player["progress"]["milestones"].append(milestone_id)
        return True
    return False

def get_player_level():
    return player["progress"]["level"]

def level_up():
    player["progress"]["level"] += 1
    return player["progress"]["level"]

def set_shop_tier(tier):
    player["progress"]["shop_tier"] = tier
    return tier

def get_shop_tier():
    return player["progress"]["shop_tier"]

def complete_quest(quest_id):
    if quest_id not in player["progress"]["quests_completed"]:
        player["progress"]["quests_completed"].append(quest_id)
        return True
    return False

def discover_location(location):
    if location not in player["progress"]["locations_discovered"]:
        player["progress"]["locations_discovered"].append(location)
        return True
    
def health_gold_name():
    typewriter_print("=======================================")
    typewriter_print(f"Name: {player['name']} | Health: {player['health']} | Gold: {player['gold']}")
    typewriter_print("=======================================")
