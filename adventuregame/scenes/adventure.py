"""Adventure scene implementation."""
from utils.printing import typewriter_print, clear_screen
from router import go_to_spaceship, register_scene
from player import player
from adventures.adventure_manager import (
    get_available_adventures,
    display_adventure_info,
    run_adventure,
    complete_adventure
)
import time

def adventure():
    """The adventure scene where player can view and start adventures."""
    while True:
        player.display_status()
        typewriter_print("\n=== Adventure Control ===")
        typewriter_print("Available Adventures:")
        
        available = get_available_adventures(player)
        if not available:
            typewriter_print("\nNo adventures available! Level up or complete prerequisites first.")
            typewriter_print("\n1. Return to Ship")
            
            choice = input("\nEnter your choice (1): ").strip()
            if choice == "1":
                clear_screen()
                go_to_spaceship()
                break
            continue
            
        # Create numbered menu of adventures
        adventure_menu = {}
        for i, (adv_id, adventure) in enumerate(available.items(), 1):
            adventure_menu[str(i)] = adv_id
            typewriter_print(f"\n{i}. {adventure['name']}")
            typewriter_print(f"   Level {adventure['min_level']} | {adventure['description']}")
        
        typewriter_print(f"\n{len(adventure_menu) + 1}. Return to Ship")
        
        try:
            choice = input("\nEnter your choice (or 'info X' for more details): ").strip().lower()
            
            if choice.startswith("info"):
                try:
                    num = choice.split()[1]
                    if num in adventure_menu:
                        clear_screen()
                        display_adventure_info(available[adventure_menu[num]])
                        time.sleep(2)
                except (IndexError, KeyError):
                    typewriter_print("Invalid info command. Try again.")
                continue
                
            if choice == str(len(adventure_menu) + 1):
                clear_screen()
                go_to_spaceship()
                break
                
            if choice in adventure_menu:
                adv_id = adventure_menu[choice]
                clear_screen()
                typewriter_print(f"Preparing for adventure: {available[adv_id]['name']}")
                typewriter_print("Are you sure you want to proceed? (y/n)")
                
                if input().strip().lower() == 'y':
                    success = run_adventure(player, adv_id)
                    if success:
                        complete_adventure(player, adv_id)
                
                clear_screen()
                continue
            
            typewriter_print("Invalid choice. Please try again.")
            time.sleep(1)
            clear_screen()
            
        except (EOFError, KeyboardInterrupt):
            typewriter_print("\nAborting adventure selection...")
            time.sleep(1)
            clear_screen()
            go_to_spaceship()
            break

# Register the adventure scene
register_scene("adventure", adventure) 