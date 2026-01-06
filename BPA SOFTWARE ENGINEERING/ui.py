"""
UI Module - User Interface Display & Formatting
BPA Software Engineering Team - ChronoQuest v1.0

This module contains GameUI class for consistent and attractive
console output formatting throughout the game.
"""

import logging


class GameUI:
    """
    User interface management for console-based display.

    RESPONSIBILITIES:
    - Display formatted headers
    - Show HUD (heads-up display)
    - Display era information
    - Show NPC dialogue
    - Display inventory
    - Show formatted messages
    - Present puzzles
    - Format game results
    """

    @staticmethod
    def display_header(title):
        """
        Display formatted header with title.

        FORMAT:
        ══════════════════════════════════════════════════════════════════════
        ║ TITLE HERE                                                         ║
        ══════════════════════════════════════════════════════════════════════
        """
        padding = (70 - len(title)) // 2
        print("\n" + "="*70)
        print(f"║ {title:^68} ║")
        print("="*70)

    @staticmethod
    def display_hud(engine):
        """
        Display game HUD with current statistics.

        SHOWS:
        - Game title
        - Current health
        - Inventory count
        - Timeline restoration percentage
        """
        state = engine.get_game_state()

        print("\n" + "─"*70)
        print(
            f"⏳ CHRONOQUEST │ ❤️  Health: {state['health']:3d}% │ 🎒 Items: {len(state['inventory'])}/4 │ 📊 Timeline: {state['completion']:3d}%")
        print("─"*70)

    @staticmethod
    def display_era_info(era):
        """
        Display current era information banner.

        SHOWS:
        - Era emoji
        - Era name
        - Historical year
        - Era description
        """
        if not era:
            return

        print(f"\n{era['emoji']} {era['name'].upper()} ({era['year']})")
        print("─"*70)
        print(f"Mission: {era['description']}")

    @staticmethod
    def display_npc_dialog(npc_name, message):
        """Display NPC dialogue with formatting."""
        print(f"\n📢 {npc_name}:")
        print(f"   \"{message}\"")

    @staticmethod
    def display_inventory(inventory):
        """
        Display player inventory.

        SHOWS:
        - Number of items
        - List of all items with star emoji
        """
        if not inventory:
            return

        print(f"\n🎒 INVENTORY ({len(inventory)}/4)")
        print("─"*70)
        for item in inventory:
            print(f"   ⭐ {item}")

    @staticmethod
    def show_message(message, message_type='info'):
        """
        Display formatted message with type indicator.

        TYPES:
        - 'info': Information message (ℹ️)
        - 'success': Success message (✓)
        - 'error': Error message (✗)
        - 'warning': Warning message (⚠️)
        """
        symbols = {
            'info': 'ℹ️',
            'success': '✓',
            'error': '✗',
            'warning': '⚠️'
        }
        symbol = symbols.get(message_type, '•')
        print(f"\n{symbol} {message}")

    @staticmethod
    def show_puzzle(puzzle_id, puzzle):
        """
        Display puzzle with question and options.

        FORMAT:
        🧩 PUZZLE CHALLENGE
        ══════════════════════════════════════════════════════════════════════
        Question: [puzzle question]

           1. [option 1]
           2. [option 2]
           3. [option 3]
           4. [option 4]
        ══════════════════════════════════════════════════════════════════════
        """
        print(f"\n🧩 PUZZLE CHALLENGE")
        print("="*70)
        print(f"Question: {puzzle['question']}\n")

        for idx, option in enumerate(puzzle['options'], 1):
            print(f"   {idx}. {option}")

        print("="*70)

    @staticmethod
    def show_result(success, message, explanation):
        """
        Display puzzle result with explanation.

        SUCCESS: Shows checkmark, message, and explanation
        FAILURE: Shows X mark, message, and explanation
        """
        if success:
            print(f"\n✅ SUCCESS!")
            print(f"   {message}")
        else:
            print(f"\n❌ FAILURE!")
            print(f"   {message}")

        print(f"\n   Explanation: {explanation}")

    @staticmethod
    def show_game_over():
        """Display game over screen."""
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                           💔 TIMELINE COLLAPSED 💔                           ║
║                                                                              ║
║                       The temporal fabric has ruptured.                      ║
║                        Mission failed. History is lost.                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)

    @staticmethod
    def show_success():
        """Display mission success screen."""
        print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                        🎉 MISSION COMPLETE! 🎉                              ║
║                                                                              ║
║                    Timeline successfully restored!                           ║
║                   History is preserved. Reality is saved.                    ║
║                                                                              ║
║                     Thank you, Chronos Agent!                                ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """)
