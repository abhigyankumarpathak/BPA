"""
Database Module - Persistence & Save/Load System
BPA Software Engineering Team - ChronoQuest v1.0

This module manages game data persistence using JSON format.
Handles saving game state, loading saved games, and managing
save file operations with error handling.
"""

import json
import os
import logging
from datetime import datetime


class GameDatabase:
    """
    Manages game data persistence using JSON files.

    RESPONSIBILITIES:
    - Save game state to file
    - Load game state from file
    - Delete save file
    - Check for save data existence
    - Handle file I/O errors gracefully

    ATTRIBUTES:
        filename (str): Name of save file
        filepath (str): Full path to save file location

    STORAGE LOCATION:
        ~/Documents/chronoquest_save.json
        (Created in user's Documents folder)
    """

    def __init__(self, filename='chronoquest_save.json'):
        """
        Initialize database with save file location.

        PARAMETERS:
            filename (str): Name of save file (default: chronoquest_save.json)

        LOGIC:
        - Set filename
        - Determine filepath (Documents folder)
        - Create Documents folder if needed
        """
        self.filename = filename
        self.filepath = os.path.join(
            os.path.expanduser('~'),
            'Documents',
            filename
        )

        # Create Documents folder if it doesn't exist
        try:
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            logging.info(f"Database initialized: {self.filepath}")
        except Exception as e:
            logging.error(f"Failed to initialize database directory: {str(e)}")

    def save_game(self, engine):
        """
        Save current game state to file.

        PARAMETERS:
            engine (GameEngine): Game engine with current state

        RETURNS:
            dict: Result with success flag and message

        SAVE DATA STRUCTURE:
        {
            'timestamp': ISO format datetime,
            'health': int (0-100),
            'inventory': list of artifacts,
            'puzzles_solved': dict of puzzle IDs,
            'current_era_id': str (era ID or None),
            'sound_enabled': bool,
            'completion': int (0-100)
        }

        LOGIC:
        - Create save data dictionary
        - Add timestamp
        - Serialize to JSON
        - Write to file
        - Handle file I/O errors
        - Log save operation
        """
        try:
            save_data = {
                'timestamp': datetime.now().isoformat(),
                'version': '1.0',
                'health': engine.health,
                'inventory': engine.inventory,
                'puzzles_solved': engine.puzzles_solved,
                'current_era_id': engine.current_era['id'] if engine.current_era else None,
                'sound_enabled': engine.sound_enabled,
                'completion': engine.get_completion_percentage()
            }

            # Write to file
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=4, ensure_ascii=False)

            timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"✓ Game saved successfully at {timestamp_str}"

            logging.info(f"Game saved: {self.filepath}")
            logging.debug(f"Save data: {save_data}")

            return {'success': True, 'message': message}

        except IOError as e:
            error_msg = f"✗ Failed to save game: I/O Error - {str(e)}"
            logging.error(f"Save failed: {error_msg}")
            return {'success': False, 'message': error_msg}
        except Exception as e:
            error_msg = f"✗ Failed to save game: {str(e)}"
            logging.error(f"Save failed: {error_msg}")
            return {'success': False, 'message': error_msg}

    def load_game(self, engine):
        """
        Load game state from file and restore to engine.

        PARAMETERS:
            engine (GameEngine): Game engine to restore state to

        RETURNS:
            dict: Result with success flag and message

        LOGIC:
        - Check if save file exists
        - Read JSON file
        - Parse save data
        - Restore engine state
        - Handle file not found
        - Handle JSON parse errors
        - Log load operation
        """
        try:
            if not os.path.exists(self.filepath):
                logging.warning("Save file not found")
                return {'success': False, 'message': 'No save data found'}

            # Read file
            with open(self.filepath, 'r', encoding='utf-8') as f:
                save_data = json.load(f)

            # Restore game state
            engine.health = save_data.get('health', 100)
            engine.inventory = save_data.get('inventory', [])
            engine.puzzles_solved = save_data.get('puzzles_solved', {})
            engine.sound_enabled = save_data.get('sound_enabled', True)

            # Restore current era
            current_era_id = save_data.get('current_era_id')
            if current_era_id:
                engine.select_era(current_era_id)

            timestamp = save_data.get('timestamp', 'Unknown')
            message = f"✓ Game loaded from {timestamp}"

            logging.info(f"Game loaded: {self.filepath}")
            logging.debug(
                f"Restored state: Health={engine.health}%, Inventory={len(engine.inventory)}, Completion={engine.get_completion_percentage()}%")

            return {'success': True, 'message': message}

        except json.JSONDecodeError as e:
            error_msg = f"✗ Failed to load game: Save file corrupted - {str(e)}"
            logging.error(f"Load failed: {error_msg}")
            return {'success': False, 'message': error_msg}
        except IOError as e:
            error_msg = f"✗ Failed to load game: I/O Error - {str(e)}"
            logging.error(f"Load failed: {error_msg}")
            return {'success': False, 'message': error_msg}
        except Exception as e:
            error_msg = f"✗ Failed to load game: {str(e)}"
            logging.error(f"Load failed: {error_msg}")
            return {'success': False, 'message': error_msg}

    def delete_save(self):
        """
        Delete save file from disk.

        RETURNS:
            dict: Result with success flag and message

        LOGIC:
        - Check if save file exists
        - Delete file
        - Handle file not found
        - Handle permission errors
        - Log deletion
        """
        try:
            if os.path.exists(self.filepath):
                os.remove(self.filepath)
                logging.info("Save file deleted")
                return {'success': True, 'message': '✓ Save data deleted'}
            else:
                logging.warning("Save file does not exist")
                return {'success': False, 'message': 'No save data to delete'}
        except PermissionError as e:
            error_msg = f"✗ Permission denied: {str(e)}"
            logging.error(f"Delete failed: {error_msg}")
            return {'success': False, 'message': error_msg}
        except Exception as e:
            error_msg = f"✗ Failed to delete save: {str(e)}"
            logging.error(f"Delete failed: {error_msg}")
            return {'success': False, 'message': error_msg}

    def has_save_data(self):
        """
        Check if save file exists.

        RETURNS:
            bool: True if save file exists, False otherwise
        """
        exists = os.path.exists(self.filepath)
        logging.debug(f"Save file check: {self.filepath} - Exists: {exists}")
        return exists

    def get_save_info(self):
        """Get brief save file information."""
        try:
            if not os.path.exists(self.filepath):
                return "No save"

            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            timestamp = data.get('timestamp', 'Unknown').split('T')[0]
            completion = data.get('completion', 0)
            return f"{timestamp} ({completion}% complete)"
        except:
            return "Corrupted save"

    def get_save_details(self):
        """Get detailed save file information."""
        try:
            if not os.path.exists(self.filepath):
                return "No save file found."

            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            timestamp = data.get('timestamp', 'Unknown')
            health = data.get('health', 0)
            inventory_count = len(data.get('inventory', []))
            completion = data.get('completion', 0)
            era_id = data.get('current_era_id', 'None')

            details = f"""
SAVE FILE INFORMATION
{'='*70}
Location: {self.filepath}
Timestamp: {timestamp}
Version: {data.get('version', '1.0')}

GAME STATE:
  Health: {health}%
  Inventory: {inventory_count}/4 artifacts
  Progress: {completion}% timeline restored
  Current Era: {era_id}

ARTIFACTS:
"""
            for item in data.get('inventory', []):
                details += f"  ✓ {item}\n"

            if not data.get('inventory', []):
                details += "  (None collected yet)\n"

            details += "="*70
            return details

        except Exception as e:
            return f"Error reading save file: {str(e)}"

    def get_save_statistics(self):
        """Get gameplay statistics from save file."""
        try:
            if not os.path.exists(self.filepath):
                return "No save file found."

            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            puzzles_solved = len(data.get('puzzles_solved', {}))
            total_puzzles = 4
            health = data.get('health', 0)
            completion = data.get('completion', 0)
            timestamp = data.get('timestamp', 'Unknown')

            stats = f"""
GAME STATISTICS
{'='*70}
Save Created: {timestamp}

PROGRESS:
  Puzzles Solved: {puzzles_solved}/{total_puzzles}
  Timeline Restored: {completion}%
  Health: {health}%

INVENTORY:
  Items Collected: {len(data.get('inventory', []))}/4
  Items: {', '.join(data.get('inventory', [])) or 'None'}

PERFORMANCE:
  Completion Percentage: {completion}%
  Status: {'✅ MISSION READY' if completion >= 100 else '⏳ IN PROGRESS'}
{'='*70}
"""
            return stats

        except Exception as e:
            return f"Error reading statistics: {str(e)}"
