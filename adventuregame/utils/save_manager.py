"""
Save Manager for the Adventure Game.
Handles saving and loading game progress using TinyDB.

Auto-save features:
- Slot 9: General auto-saves
- Slot 8: Adventure completion auto-saves
"""

import os
from datetime import datetime
from typing import Dict, Optional, Any

from marshmallow import Schema, fields
from tinydb import TinyDB, Query
from tinydb.table import Document

class PlayerStateSchema(Schema):
    """Schema for serializing/deserializing player state."""
    name = fields.Str(required=True)
    level = fields.Int(required=True)
    health = fields.Int(required=True)
    inventory = fields.List(fields.Str(), required=True)
    completed_adventures = fields.List(fields.Str(), required=True)
    current_adventure = fields.Str(allow_none=True)
    current_scene = fields.Str(allow_none=True)
    milestones = fields.List(fields.Str(), required=True)
    experience = fields.Int(required=True)
    last_saved = fields.DateTime(required=True)
    last_completed_adventure = fields.Str(allow_none=True)  # Track last completed adventure

class SaveManager:
    """Manages game save files using TinyDB."""
    
    def __init__(self, save_dir: str = "saves"):
        """Initialize the save manager.
        
        Args:
            save_dir: Directory to store save files
        """
        self.save_dir = save_dir
        os.makedirs(save_dir, exist_ok=True)
        self.db_path = os.path.join(save_dir, "savegames.json")
        self.db = TinyDB(self.db_path)
        self.schema = PlayerStateSchema()
        
    def save_game(self, player_state: Dict[str, Any], slot: int = 0) -> bool:
        """Save the current game state.
        
        Args:
            player_state: Dictionary containing player's current state
            slot: Save slot number (0-9)
            
        Returns:
            bool: True if save successful, False otherwise
        """
        try:
            # Add timestamp
            player_state['last_saved'] = datetime.now()
            
            # Validate and serialize the state
            validated_state = self.schema.dump(player_state)
            
            # Save to database
            self.db.upsert(
                Document(
                    validated_state,
                    doc_id=slot
                )
            )
            return True
            
        except Exception as e:
            print(f"Error saving game: {e}")
            return False
    
    def load_game(self, slot: int = 0) -> Optional[Dict[str, Any]]:
        """Load a saved game state.
        
        Args:
            slot: Save slot to load (0-9)
            
        Returns:
            Optional[Dict]: The loaded game state or None if not found/error
        """
        try:
            # Query the save file
            saved_state = self.db.get(doc_id=slot)
            
            if not saved_state:
                print(f"No save file found in slot {slot}")
                return None
            
            # Deserialize and validate the state
            loaded_state = self.schema.load(saved_state)
            return loaded_state
            
        except Exception as e:
            print(f"Error loading save file: {e}")
            return None
    
    def list_saves(self) -> Dict[int, datetime]:
        """List all available save files and their timestamps.
        
        Returns:
            Dict[int, datetime]: Dictionary of slot numbers and save times
        """
        saves = {}
        for save in self.db.all():
            slot = save.doc_id
            timestamp = datetime.fromisoformat(save.get('last_saved'))
            saves[slot] = timestamp
        return saves
    
    def delete_save(self, slot: int) -> bool:
        """Delete a save file.
        
        Args:
            slot: Save slot to delete
            
        Returns:
            bool: True if deletion successful, False otherwise
        """
        try:
            self.db.remove(doc_ids=[slot])
            return True
        except Exception as e:
            print(f"Error deleting save file: {e}")
            return False
    
    def auto_save(self, player_state: Dict[str, Any]) -> bool:
        """Create an auto-save.
        
        Args:
            player_state: Current player state
            
        Returns:
            bool: True if auto-save successful, False otherwise
        """
        return self.save_game(player_state, slot=9)  # Use slot 9 for auto-saves
        
    def save_adventure_completion(self, player_state: Dict[str, Any], adventure_id: str) -> bool:
        """Create an auto-save after completing an adventure.
        
        Args:
            player_state: Current player state
            adventure_id: ID of the completed adventure
            
        Returns:
            bool: True if save successful, False otherwise
        """
        # Update the state with the completed adventure
        player_state['last_completed_adventure'] = adventure_id
        
        # Save in the adventure completion slot
        return self.save_game(player_state, slot=8)  # Use slot 8 for adventure completion saves 