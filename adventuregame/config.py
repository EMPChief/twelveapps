"""Game configuration settings."""

# Player settings
PLAYER_MAX_HEALTH = 100
PLAYER_STARTING_GOLD = 100
PLAYER_STARTING_INVENTORY = []

# Shop settings
SHOP_TIERS = {
    1: {"min_price": 5, "max_price": 150, "min_stock": 5, "max_stock": 100},
    2: {"min_price": 100, "max_price": 500, "min_stock": 3, "max_stock": 50},
    3: {"min_price": 400, "max_price": 1500, "min_stock": 1, "max_stock": 25}
}

# Tavern settings
TAVERN_SLEEP_COST = 50
TAVERN_STEW_COST = 10
TAVERN_HEAL_AMOUNT = 20
TAVERN_POISON_DAMAGE = 5
TAVERN_POISON_DURATION = 3

# Game settings
DEV_MODE = False  # Set to False for production
TYPEWRITER_DELAY = 0.05