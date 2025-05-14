# Adventure Game Architecture

## Overview
The adventure game is built with a modular architecture that separates content from logic. The system uses JSON files for content definition and Python modules for game mechanics.

## Core Components

### 1. Adventure System
- `adventure_manager.py`: Core engine for running adventures
- `validate_json.py`: JSON schema validation for content files
- Data files in JSON format for content definition

### 2. Scene Management
- Scene transitions and state management
- Player choice processing
- Event and effect handling

### 3. Player System
- Character stats and progression
- Inventory management
- Milestone tracking

### 4. Content System
All game content is defined in JSON files:
```
adventures/
├── data/
│   ├── adventures.json    # Adventure definitions
│   ├── items.json        # Item definitions
│   ├── rewards.json      # Reward configurations
│   ├── milestones.json   # Achievement system
│   └── [adventure_name]/ # Adventure-specific content
│       └── scenes.json   # Scene definitions
```

## Data Structures

### Adventure Definition
```json
{
    "adventure_id": {
        "name": "Adventure Name",
        "description": "Adventure description",
        "min_level": 1,
        "starting_scene": "first_scene_id",
        "completion_milestone": "milestone_id",
        "reward_id": "reward_id"
    }
}
```

### Scene Definition
```json
{
    "scene_id": {
        "description": "Scene description",
        "choices": {
            "1": {
                "text": "Choice description",
                "leads_to": "next_scene_id",
                "requires_item": "optional_item",
                "success_rate": 0.7,
                "success": "success_scene",
                "failure": "failure_scene",
                "loot": ["item1", "item2"],
                "reveals": "Discovery text",
                "damage": 10,
                "heal": 20,
                "bonus_xp": 50
            }
        }
    }
}
```

### Item Definition
```json
{
    "item_name": {
        "type": "item_type",
        "description": "Item description",
        "value": 100,
        "usable": true,
        "consumable": false,
        "effect": {
            "type": "effect_type",
            "amount": 50,
            "against": "effect_target"
        }
    }
}
```

## Game Flow

1. **Adventure Selection**
   - Player views available adventures
   - System checks level requirements
   - System verifies milestone prerequisites

2. **Adventure Execution**
   - Load adventure data
   - Present starting scene
   - Process player choices
   - Handle scene transitions
   - Apply effects and rewards

3. **Scene Processing**
   - Display scene description
   - Show available choices
   - Check requirements
   - Process outcomes
   - Update game state

4. **Completion Handling**
   - Award rewards
   - Update milestones
   - Save progress
   - Return to hub

## State Management

The game maintains several state objects:
- Player state (health, inventory, etc.)
- Adventure state (current scene, collected items)
- Global progress (milestones, completed adventures)

### Save System

The game uses TinyDB for reliable save state management:

1. **Save Slots**
   - Slots 0-7: Manual save slots
   - Slot 8: Adventure completion auto-saves
   - Slot 9: General auto-saves

2. **Auto-Save Triggers**
   - After completing an adventure
   - At key checkpoints (configurable)
   - Before potentially dangerous actions

3. **Saved Data**
   - Player information (name, level, health)
   - Inventory contents
   - Adventure progress
   - Milestone achievements
   - Experience and rewards
   - Timestamps
   - Last completed adventure

4. **Save Management**
   - Multiple save slots for different playthroughs
   - Auto-save backup system
   - Save validation and error handling
   - Easy save/load interface

## Error Handling

1. **Content Validation**
   - JSON schema validation
   - Scene connection verification
   - Item reference checking

2. **Runtime Validation**
   - Player state validation
   - Choice availability checking
   - Resource verification

## Adding New Content

1. **New Adventures**
   - Create adventure entry in adventures.json
   - Create adventure directory
   - Add scenes.json with content
   - Define rewards and milestones

2. **New Items**
   - Add item definition to items.json
   - Update relevant scenes
   - Define any new effects

3. **New Features**
   - Update schemas if needed
   - Add new effect types if required
   - Update documentation

## Best Practices

1. **Content Creation**
   - Use descriptive IDs
   - Maintain consistent difficulty curve
   - Provide multiple paths
   - Balance risk and reward

2. **Code Maintenance**
   - Validate JSON files before deployment
   - Test all paths in new content
   - Keep documentation updated
   - Follow naming conventions 

## Quick Modification Guide

### Common Tasks

1. **Change Adventure Difficulty**
   - File: `adventures/data/adventures.json`
   - Modify: "min_level" field
   - Update rewards accordingly

2. **Adjust Item Effects**
   - File: `adventures/data/items.json`
   - Modify: "effect" object properties
   - Test balance in-game

3. **Update Scene Text**
   - File: `adventures/data/[adventure_name]/scenes.json`
   - Modify: "description" or choice "text" fields
   - No validation needed for text changes

4. **Change Success Rates**
   - File: `adventures/data/[adventure_name]/scenes.json`
   - Modify: "success_rate" in choice objects
   - Range: 0.0 to 1.0

5. **Modify Rewards**
   - File: `adventures/data/rewards.json`
   - Adjust: item lists, XP amounts
   - Consider game balance

For detailed modification instructions, see CONTRIBUTING.md 