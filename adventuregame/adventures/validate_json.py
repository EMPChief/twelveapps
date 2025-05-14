"""JSON schema validation for adventure system files.

This module provides schema validation for all JSON files in the adventure system.
It includes schemas for adventures, items, rewards, milestones, and scenes.
"""

import json
import os
import jsonschema
from typing import Dict, Any

# Schema definitions
ADVENTURE_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {
            "type": "object",
            "required": ["name", "description", "min_level", "starting_scene", "completion_milestone", "reward_id"],
            "properties": {
                "name": {"type": "string"},
                "description": {"type": "string"},
                "min_level": {"type": "integer", "minimum": 1},
                "starting_scene": {"type": "string"},
                "completion_milestone": {"type": "string"},
                "reward_id": {"type": "string"}
            }
        }
    }
}

ITEM_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {
            "type": "object",
            "required": ["type", "description", "value", "usable", "consumable"],
            "properties": {
                "type": {
                    "type": "string",
                    "enum": ["tool", "consumable", "resource", "equipment", "key", "quest_item"]
                },
                "description": {"type": "string"},
                "value": {"type": "integer", "minimum": 0},
                "usable": {"type": "boolean"},
                "consumable": {"type": "boolean"},
                "effect": {
                    "type": "object",
                    "required": ["type"],
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["heal", "damage", "protection"]
                        },
                        "amount": {"type": "integer"},
                        "against": {"type": "string"}
                    }
                }
            }
        }
    }
}

REWARD_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {
            "type": "object",
            "required": ["gold", "items", "experience"],
            "properties": {
                "gold": {"type": "integer", "minimum": 0},
                "items": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "experience": {"type": "integer", "minimum": 0}
            }
        }
    }
}

MILESTONE_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {
            "type": "object",
            "required": ["title", "description", "experience_bonus", "unlocks"],
            "properties": {
                "title": {"type": "string"},
                "description": {"type": "string"},
                "experience_bonus": {"type": "integer", "minimum": 0},
                "unlocks": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            }
        }
    }
}

EFFECT_SCHEMA = {
    "type": "object",
    "required": ["text", "leads_to"],
    "properties": {
        "text": {"type": "string"},
        "damage": {"type": "integer", "minimum": 0},
        "heal": {"type": "integer", "minimum": 0},
        "bonus_xp": {"type": "integer", "minimum": 0},
        "loot": {
            "type": "array",
            "items": {"type": "string"}
        },
        "leads_to": {"type": "string"}
    }
}

SCENE_SCHEMA = {
    "type": "object",
    "patternProperties": {
        "^.*$": {
            "type": "object",
            "required": ["description", "choices"],
            "properties": {
                "description": {"type": "string"},
                "choices": {
                    "type": "object",
                    "patternProperties": {
                        "^.*$": {
                            "type": "object",
                            "required": ["text"],
                            "properties": {
                                "text": {"type": "string"},
                                "requires_item": {"type": "string"},
                                "success_rate": {
                                    "type": "number",
                                    "minimum": 0,
                                    "maximum": 1
                                },
                                "success": {
                                    "oneOf": [
                                        {"type": "string"},
                                        {"$ref": "#/definitions/effect"}
                                    ]
                                },
                                "failure": {
                                    "oneOf": [
                                        {"type": "string"},
                                        {"$ref": "#/definitions/effect"}
                                    ]
                                },
                                "leads_to": {"type": "string"},
                                "loot": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "reveals": {"type": "string"},
                                "damage": {"type": "integer", "minimum": 0},
                                "heal": {"type": "integer", "minimum": 0},
                                "bonus_xp": {"type": "integer", "minimum": 0}
                            }
                        }
                    }
                },
                "final_scene": {"type": "boolean"},
                "success": {"type": "boolean"}
            }
        }
    },
    "definitions": {
        "effect": EFFECT_SCHEMA
    }
}

def load_json_file(filepath: str) -> Dict[str, Any]:
    """Load and return JSON data from a file.
    
    Args:
        filepath: Path to the JSON file to load.
        
    Returns:
        Dict containing the JSON data if successful, empty dict otherwise.
        
    Raises:
        FileNotFoundError: If the file doesn't exist.
        JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find file {filepath}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file {filepath}")
        return {}

def validate_json(data: Dict[str, Any], schema: Dict[str, Any], filepath: str) -> bool:
    """Validate JSON data against a schema.
    
    Args:
        data: The JSON data to validate.
        schema: The schema to validate against.
        filepath: Path to the file (for error reporting).
        
    Returns:
        True if validation succeeds, False otherwise.
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"✓ {filepath} is valid")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"✗ {filepath} validation error:")
        print(f"  {e.message}")
        return False

def validate_all_json_files() -> bool:
    """Validate all JSON files in the adventure system.
    
    This function validates:
    - Main configuration files (adventures.json, items.json, etc.)
    - Scene files for each adventure
    
    Returns:
        True if all files are valid, False if any validation fails.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    
    all_valid = True
    
    # Validate main JSON files
    files_to_validate = {
        'adventures.json': ADVENTURE_SCHEMA,
        'items.json': ITEM_SCHEMA,
        'rewards.json': REWARD_SCHEMA,
        'milestones.json': MILESTONE_SCHEMA
    }
    
    for filename, schema in files_to_validate.items():
        filepath = os.path.join(data_dir, filename)
        data = load_json_file(filepath)
        if data:
            if not validate_json(data, schema, filename):
                all_valid = False
    

    for adventure_dir in os.listdir(data_dir):
        adventure_path = os.path.join(data_dir, adventure_dir)
        if os.path.isdir(adventure_path):
            scenes_file = os.path.join(adventure_path, 'scenes.json')
            if os.path.exists(scenes_file):
                data = load_json_file(scenes_file)
                if data:
                    if not validate_json(data, SCENE_SCHEMA, f"{adventure_dir}/scenes.json"):
                        all_valid = False
    
    return all_valid

if __name__ == "__main__":
    print("Validating adventure system JSON files...")
    if validate_all_json_files():
        print("\nAll JSON files are valid! ✨")
    else:
        print("\nSome JSON files have validation errors. 😕")
        exit(1) 