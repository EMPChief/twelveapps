# Contributing to the Adventure Game

## Quick Reference Guide

### Adding New Content

#### 1. Add a New Adventure
1. Edit `adventures/data/adventures.json`:
```json
{
    "your_adventure_id": {
        "name": "Your Adventure Name",
        "description": "Adventure description",
        "min_level": 1,
        "starting_scene": "first_scene_id",
        "completion_milestone": "milestone_id",
        "reward_id": "reward_id"
    }
}
```

2. Create directory: `adventures/data/your_adventure_id/`
3. Create `adventures/data/your_adventure_id/scenes.json`
4. Add reward in `adventures/data/rewards.json`
5. Add milestone in `adventures/data/milestones.json`

#### 2. Add a New Item
1. Edit `adventures/data/items.json`:
```json
{
    "your_item_name": {
        "type": "weapon/armor/consumable/key",
        "description": "Item description",
        "value": 100,
        "usable": true,
        "consumable": false,
        "effect": {
            "type": "damage/heal/buff",
            "amount": 50,
            "against": "target_type"
        }
    }
}
```

#### 3. Add a New Scene
1. Locate the relevant adventure's scenes.json
2. Add new scene:
```json
{
    "your_scene_id": {
        "description": "Scene description",
        "choices": {
            "1": {
                "text": "Choice text",
                "leads_to": "next_scene_id"
            }
        }
    }
}
```

### Removing Content

#### 1. Remove an Adventure
1. Delete the adventure's directory: `adventures/data/adventure_id/`
2. Remove entry from `adventures/data/adventures.json`
3. Remove associated rewards from `adventures/data/rewards.json`
4. Remove associated milestones from `adventures/data/milestones.json`

#### 2. Remove an Item
1. Remove entry from `adventures/data/items.json`
2. Search all scene files for item references and remove them:
   - Check "requires_item" fields
   - Check "loot" arrays
   - Check any special effects

#### 3. Remove a Scene
1. Locate the scene in its adventure's scenes.json
2. Remove the scene entry
3. Search the same file for any "leads_to" references to this scene
4. Update or remove choices that lead to the deleted scene

### Modifying Content

#### 1. Change Adventure Properties
1. Edit the adventure entry in `adventures/data/adventures.json`
2. If changing requirements or rewards:
   - Update `milestones.json` if needed
   - Update `rewards.json` if needed

#### 2. Modify Item Properties
1. Edit the item in `adventures/data/items.json`
2. If changing fundamental properties (like making a non-consumable consumable):
   - Review all scenes where the item appears
   - Update any related game logic in `adventure_manager.py`

#### 3. Update Scene Content
1. Find the scene in its adventure's scenes.json
2. Modify the scene properties
3. If changing choice outcomes:
   - Verify new scene references exist
   - Update any related milestones

## Validation

Always run validation after changes:
```bash
python adventures/validate_json.py
```

## Common File Locations

- Adventure definitions: `adventures/data/adventures.json`
- Item definitions: `adventures/data/items.json`
- Reward configurations: `adventures/data/rewards.json`
- Achievement tracking: `adventures/data/milestones.json`
- Scene content: `adventures/data/[adventure_name]/scenes.json`
- Validation logic: `adventures/validate_json.py`
- Game engine: `adventures/adventure_manager.py`

## Testing Changes

1. Run the validation script
2. Test the modified content in-game
3. Check all paths and outcomes
4. Verify rewards and milestones
5. Test related content that might be affected

## Common Issues and Solutions

### Invalid JSON
- Use a JSON validator
- Check for missing commas
- Verify closing brackets and braces

### Missing References
- Validate all scene connections
- Check item references in scenes
- Verify milestone and reward IDs

### Broken Paths
- Map out all scene connections
- Verify no dead ends
- Check all choice outcomes

## Need Help?

1. Check the ARCHITECTURE.md for system design
2. Review the JSON schemas in validate_json.py
3. Test changes in small increments
4. Document any new patterns you discover 