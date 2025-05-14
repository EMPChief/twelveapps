"""Shop inventory and item definitions."""

SHOP_ITEMS = {
    "Health Potion": {
        "description": "Restores 25 health points",
        "base_price": 25,
        "tier": 1,
        "effect": "heal",
        "effect_value": 25
    },
    "Gold Bar": {
        "description": "A valuable trading item",
        "base_price": 100,
        "tier": 2,
        "effect": "value",
        "effect_value": 150
    },
    "Space Suit": {
        "description": "Protects against environmental damage",
        "base_price": 200,
        "tier": 2,
        "effect": "armor",
        "effect_value": 10
    },
    "Laser Gun": {
        "description": "A basic weapon for self-defense",
        "base_price": 150,
        "tier": 2,
        "effect": "weapon",
        "effect_value": 15
    },
    "Shield Generator": {
        "description": "Generates a protective shield",
        "base_price": 300,
        "tier": 3,
        "effect": "shield",
        "effect_value": 30
    },
    "Energy Drink": {
        "description": "Temporary health boost",
        "base_price": 15,
        "tier": 1,
        "effect": "temp_heal",
        "effect_value": 10
    },
    "Quantum Chip": {
        "description": "Advanced technology component",
        "base_price": 500,
        "tier": 3,
        "effect": "quest",
        "effect_value": 0
    }
}

def get_available_items(shop_tier):
    """Get items available for the current shop tier."""
    return {
        name: item for name, item in SHOP_ITEMS.items()
        if item["tier"] <= shop_tier
    }
