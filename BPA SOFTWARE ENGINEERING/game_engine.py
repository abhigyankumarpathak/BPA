"""
Game Engine v5.1 - CHALLENGES LOADING FIX
BPA Software Engineering Team Competition - 2026
Complete progression system with 6 puzzles per era reaching 100% on completion.
"""

import logging
import random
from datetime import datetime


class GameEngine:
    """
    Core game engine with FIXED progression mechanics.

    PROGRESSION SYSTEM:
    - 4 Eras
    - 6 main puzzles per era (1 per "difficulty" level)
    - 25% per era = 100% total when all 4 eras complete
    - Each puzzle solved = ~4.2% completion (25% ÷ 6 puzzles)
    """

    def __init__(self):
        """Initialize game engine with fixed progression."""
        # Game State
        self.current_screen = 'menu'
        self.current_era = None
        self.health = 100
        self.inventory = []
        self.puzzles_solved = {}  # puzzle_id -> True
        self.sound_enabled = True
        self.npc_dialog = None
        self.hints_used = {}  # puzzle_id -> count
        self.attempts = {}  # puzzle_id -> count
        self.score = 0
        self.achievements = []
        self.difficulty_setting = 'normal'  # normal, hard, expert
        self.game_start_time = datetime.now()
        self.current_puzzle_index = 0  # Track which puzzle in current era

        logging.info("GameEngine v5.1 initialized")

        # Historical Eras
        self.eras = [
            {
                'id': 'egypt',
                'name': 'Ancient Egypt',
                'year': '2560 BCE',
                'emoji': '🏛️',
                'description': 'Restore the pyramid construction timeline.',
                'story': 'The Nile\'s waters flow backwards. Temporal anomalies threaten 3000 years of civilization.',
                'npc': 'Pharaoh Khufu',
            },
            {
                'id': 'medieval',
                'name': 'Medieval Europe',
                'year': '1347 CE',
                'emoji': '🏰',
                'description': 'Fix castle defense mechanisms against temporal rifts.',
                'story': 'Castle walls collapse through time. Knights fade from existence.',
                'npc': 'Knight Commander',
            },
            {
                'id': 'renaissance',
                'name': 'Renaissance Italy',
                'year': '1504 CE',
                'emoji': '🎨',
                'description': 'Restore da Vinci\'s invention timeline.',
                'story': 'Leonardo\'s drawings vanish. Masterpieces turn to dust.',
                'npc': 'Leonardo da Vinci',
            },
            {
                'id': 'spaceage',
                'name': 'Space Age',
                'year': '1969 CE',
                'emoji': '🚀',
                'description': 'Synchronize the lunar landing timeline.',
                'story': 'Apollo program vanishes. Humanity\'s greatest dream dies.',
                'npc': 'Mission Control',
            }
        ]

        # FIXED: 6 puzzles per era, each ~4.2% (25% ÷ 6)
        self.puzzles = {
            # EGYPT ERA
            'egypt_puzzle_1': {
                'era': 'egypt',
                'puzzle_num': 1,
                'question': 'Complete the hieroglyphic sequence: 🏛️ 👑 ⚱️ ?',
                'options': ['🪶', '☀️', '⭐', '🗿'],
                'correct': 1,
                'reward': 'Scarab Amulet',
                'explanation': 'The sun represents Ra\'s eternal cycle - resurrection and continuity.',
                'difficulty': 'Easy',
                'base_points': 100,
                'hint': 'Think about the daily cycle in Egyptian mythology',
                'completion_percent': 4.2
            },
            'egypt_puzzle_2': {
                'era': 'egypt',
                'puzzle_num': 2,
                'question': 'Egyptian fraction math: 1/2 + 1/4 = ?',
                'options': ['1/6', '3/4', '2/4', '1/1'],
                'correct': 1,
                'reward': 'Papyrus Scroll',
                'explanation': '1/2 + 1/4 = 2/4 + 1/4 = 3/4. Ancient Egyptians mastered fractions.',
                'difficulty': 'Easy-Medium',
                'base_points': 125,
                'hint': 'Convert to common denominator',
                'completion_percent': 4.2
            },
            'egypt_puzzle_3': {
                'era': 'egypt',
                'puzzle_num': 3,
                'question': 'Nile geometry: A pyramid\'s shadow points 45°. Sun elevation angle?',
                'options': ['30°', '45°', '60°', '90°'],
                'correct': 1,
                'reward': 'Golden Scepter',
                'explanation': 'Complementary angles: 45° shadow angle = 45° sun elevation.',
                'difficulty': 'Medium',
                'base_points': 150,
                'hint': 'Complementary angles in a right triangle',
                'completion_percent': 4.2
            },
            'egypt_puzzle_4': {
                'era': 'egypt',
                'puzzle_num': 4,
                'question': 'Delta population ratio 2:3:5. Smallest district: 50,000. Total?',
                'options': ['100,000', '250,000', '500,000', '1,000,000'],
                'correct': 1,
                'reward': 'Nile Navigation Chart',
                'explanation': 'Ratio parts total: 2+3+5=10. If 2 parts=50,000, then 1 part=25,000. Total=250,000.',
                'difficulty': 'Medium-Hard',
                'base_points': 175,
                'hint': 'Find the total ratio parts first',
                'completion_percent': 4.2
            },
            'egypt_puzzle_5': {
                'era': 'egypt',
                'puzzle_num': 5,
                'question': 'Egyptian numerals: 1 million + 3 thousand = ?',
                'options': ['3,000', '1,003,000', '1,000,003', '4,000,000'],
                'correct': 1,
                'reward': 'Numeral Papyrus',
                'explanation': 'Egyptian additive system: 1,000,000 + 3,000 = 1,003,000.',
                'difficulty': 'Hard',
                'base_points': 200,
                'hint': 'Egyptian numerals are additive',
                'completion_percent': 4.2
            },
            'egypt_puzzle_6': {
                'era': 'egypt',
                'puzzle_num': 6,
                'question': 'Great Pyramid: base 230m, height 146.5m. Aspect ratio (h/b)?',
                'options': ['0.5', '0.64', '1.618', '1.0'],
                'correct': 1,
                'reward': 'Geometric Blueprint',
                'explanation': '146.5 ÷ 230 ≈ 0.637 ≈ 0.64. Reflects Egyptian mathematical mastery.',
                'difficulty': 'Expert',
                'base_points': 250,
                'hint': 'Divide height by base',
                'completion_percent': 4.2
            },

            # MEDIEVAL ERA
            'medieval_puzzle_1': {
                'era': 'medieval',
                'puzzle_num': 1,
                'question': 'Castle lock code: (2+3) × 4 + 5 = ?',
                'options': ['15', '20', '25', '30'],
                'correct': 2,
                'reward': 'Castle Key',
                'explanation': '(2+3)=5, ×4=20, +5=25. Follow PEMDAS.',
                'difficulty': 'Easy',
                'base_points': 100,
                'hint': 'Use order of operations (PEMDAS)',
                'completion_percent': 4.2
            },
            'medieval_puzzle_2': {
                'era': 'medieval',
                'puzzle_num': 2,
                'question': 'Walls protect 1/4 of fortress. Enemies breach 1/3 of walls. Safe?',
                'options': ['1/6', '2/3', '7/12', '1/3'],
                'correct': 1,
                'reward': 'Knight\'s Shield',
                'explanation': 'Protected 1/4, breached 1/3 of that = 1/12 lost. Remaining safe area calculation.',
                'difficulty': 'Easy-Medium',
                'base_points': 125,
                'hint': 'Work with fractions carefully',
                'completion_percent': 4.2
            },
            'medieval_puzzle_3': {
                'era': 'medieval',
                'puzzle_num': 3,
                'question': 'Siege: 100 soldiers eat 1 ton grain/day. 250 soldiers, 30 days?',
                'options': ['30 tons', '75 tons', '100 tons', '150 tons'],
                'correct': 1,
                'reward': 'Medieval Crown',
                'explanation': '250 soldiers = 2.5× consumption. 1 ton × 2.5 × 30 = 75 tons.',
                'difficulty': 'Medium',
                'base_points': 150,
                'hint': 'Scale up consumption then multiply by days',
                'completion_percent': 4.2
            },
            'medieval_puzzle_4': {
                'era': 'medieval',
                'puzzle_num': 4,
                'question': 'Heraldry: 2 lions, 3 dragons displayed. Unique arrangements?',
                'options': ['10', '60', '120', '5040'],
                'correct': 0,
                'reward': 'Heraldic Banner',
                'explanation': 'Permutations with repetition: 5!/(2!×3!) = 10 arrangements.',
                'difficulty': 'Medium-Hard',
                'base_points': 175,
                'hint': 'Consider permutations with repetition',
                'completion_percent': 4.2
            },
            'medieval_puzzle_5': {
                'era': 'medieval',
                'puzzle_num': 5,
                'question': 'Knight moves L-shape on chess: From a1, how many valid moves?',
                'options': ['2', '4', '8', '6'],
                'correct': 0,
                'reward': 'Knight\'s Gambit',
                'explanation': 'From corner a1, only b3 and c2 are valid moves. Board edge limits options.',
                'difficulty': 'Hard',
                'base_points': 200,
                'hint': 'Limited movement at the board\'s corner',
                'completion_percent': 4.2
            },
            'medieval_puzzle_6': {
                'era': 'medieval',
                'puzzle_num': 6,
                'question': 'Square castle 500m/side. Patrol 100m inside walls. Patrol perimeter?',
                'options': ['1200m', '1400m', '1600m', '2000m'],
                'correct': 0,
                'reward': 'Fortification Master',
                'explanation': 'Inner square: 500 - 2(100) = 300m/side. Perimeter = 4 × 300 = 1200m.',
                'difficulty': 'Expert',
                'base_points': 250,
                'hint': 'Calculate inner square dimensions',
                'completion_percent': 4.2
            },

            # RENAISSANCE ERA
            'renaissance_puzzle_1': {
                'era': 'renaissance',
                'puzzle_num': 1,
                'question': 'Fibonacci: 1, 1, 2, 3, 5, 8, ?',
                'options': ['10', '11', '13', '16'],
                'correct': 2,
                'reward': 'Golden Compass',
                'explanation': 'Fibonacci: each = sum of previous two. 5+8=13.',
                'difficulty': 'Easy',
                'base_points': 100,
                'hint': 'Each number = sum of previous two',
                'completion_percent': 4.2
            },
            'renaissance_puzzle_2': {
                'era': 'renaissance',
                'puzzle_num': 2,
                'question': 'Golden ratio φ≈1.618. Rectangle long=10, short side?',
                'options': ['6', '7.5', '8', '9'],
                'correct': 0,
                'reward': 'Renaissance Masterpiece',
                'explanation': 'Golden ratio: long/short = 1.618. 10/1.618 ≈ 6.18 ≈ 6.',
                'difficulty': 'Easy-Medium',
                'base_points': 125,
                'hint': 'Divide long by golden ratio',
                'completion_percent': 4.2
            },
            'renaissance_puzzle_3': {
                'era': 'renaissance',
                'puzzle_num': 3,
                'question': 'One-point perspective: vanishing points?',
                'options': ['0', '1', '2', '3'],
                'correct': 1,
                'reward': 'Artistic Vision',
                'explanation': 'One-point uses 1 vanishing point. Leonardo revolutionized art.',
                'difficulty': 'Medium',
                'base_points': 150,
                'hint': 'The name hints at the answer',
                'completion_percent': 4.2
            },
            'renaissance_puzzle_4': {
                'era': 'renaissance',
                'puzzle_num': 4,
                'question': 'Vitruvian Man: head = 1/8 body height. Head=22.5cm, total?',
                'options': ['144cm', '168cm', '180cm', '225cm'],
                'correct': 2,
                'reward': 'Vitruvian Blueprint',
                'explanation': 'Head (1/8) = 22.5cm → full body = 22.5 × 8 = 180cm.',
                'difficulty': 'Medium-Hard',
                'base_points': 175,
                'hint': 'Head is 1/8 of total',
                'completion_percent': 4.2
            },
            'renaissance_puzzle_5': {
                'era': 'renaissance',
                'puzzle_num': 5,
                'question': 'Gear system A(40t)→B(60t)→C(20t). A rotates 6x, C rotates?',
                'options': ['12', '18', '24', '36'],
                'correct': 1,
                'reward': 'Mechanical Codex',
                'explanation': 'Gear ratio calculation: (40/60)×(60/20)×6 rotations = 18 for C.',
                'difficulty': 'Hard',
                'base_points': 200,
                'hint': 'Calculate gear ratios step by step',
                'completion_percent': 4.2
            },
            'renaissance_puzzle_6': {
                'era': 'renaissance',
                'puzzle_num': 6,
                'question': 'Concentric circles outer=10cm, inner=6cm. Area ratio?',
                'options': ['1:1', '2:3', '3:5', '1:2'],
                'correct': 2,
                'reward': 'Optical Treatise',
                'explanation': 'Area ratio: 100:36 ≈ 3:1 approximately 3:5 when simplified.',
                'difficulty': 'Expert',
                'base_points': 250,
                'hint': 'Consider the areas',
                'completion_percent': 4.2
            },

            # SPACE AGE ERA
            'spaceage_puzzle_1': {
                'era': 'spaceage',
                'puzzle_num': 1,
                'question': 'Convert 8 decimal to binary: ?',
                'options': ['1000', '0100', '1010', '0011'],
                'correct': 0,
                'reward': 'Data Core',
                'explanation': 'Binary 1000 = 1×8+0×4+0×2+0×1 = 8.',
                'difficulty': 'Easy',
                'base_points': 100,
                'hint': 'Count place values: 8, 4, 2, 1',
                'completion_percent': 4.2
            },
            'spaceage_puzzle_2': {
                'era': 'spaceage',
                'puzzle_num': 2,
                'question': 'Escape velocity 11.2 km/s to km/h?',
                'options': ['40,320 km/h', '50,400 km/h', '60,480 km/h', '73,920 km/h'],
                'correct': 0,
                'reward': 'Rocket Blueprint',
                'explanation': '11.2 × 3600 = 40,320 km/h.',
                'difficulty': 'Easy-Medium',
                'base_points': 125,
                'hint': 'Multiply by 3,600 s/h',
                'completion_percent': 4.2
            },
            'spaceage_puzzle_3': {
                'era': 'spaceage',
                'puzzle_num': 3,
                'question': 'Moon orbit every 27.3 days. Orbits per year?',
                'options': ['10', '13', '15', '20'],
                'correct': 1,
                'reward': 'Lunar Triumph',
                'explanation': '365 ÷ 27.3 ≈ 13.4 ≈ 13 orbits/year.',
                'difficulty': 'Medium',
                'base_points': 150,
                'hint': 'Divide year days by orbital period',
                'completion_percent': 4.2
            },
            'spaceage_puzzle_4': {
                'era': 'spaceage',
                'puzzle_num': 4,
                'question': 'Rocket fuel: Stage 1=80%, Stage 2=15%, Stage 3=5%. Total=300,000kg. Stage 2?',
                'options': ['45,000 kg', '60,000 kg', '75,000 kg', '240,000 kg'],
                'correct': 0,
                'reward': 'Propulsion Manual',
                'explanation': '15% × 300,000 = 45,000 kg.',
                'difficulty': 'Medium-Hard',
                'base_points': 175,
                'hint': 'Calculate 15% of total',
                'completion_percent': 4.2
            },
            'spaceage_puzzle_5': {
                'era': 'spaceage',
                'puzzle_num': 5,
                'question': 'Earth-Moon signal (384,400 km, speed=300,000 km/s). Delay?',
                'options': ['0.64s', '1.28s', '2.56s', '5.12s'],
                'correct': 1,
                'reward': 'Communication Array',
                'explanation': '384,400 ÷ 300,000 ≈ 1.28 seconds.',
                'difficulty': 'Hard',
                'base_points': 200,
                'hint': 'Distance divided by speed',
                'completion_percent': 4.2
            },
            'spaceage_puzzle_6': {
                'era': 'spaceage',
                'puzzle_num': 6,
                'question': 'Thrust F=7.5MN, v=2,500 m/s. Mass flow rate = F/v?',
                'options': ['1,000 kg/s', '3,000 kg/s', '5,000 kg/s', '7,500 kg/s'],
                'correct': 1,
                'reward': 'Engine Specifications',
                'explanation': '7,500,000 ÷ 2,500 = 3,000 kg/s.',
                'difficulty': 'Expert',
                'base_points': 250,
                'hint': 'Rearrange F=m×v to m=F/v',
                'completion_percent': 4.2
            },
        }

        # NPC dialogue
        self.npc_messages = {
            'Pharaoh Khufu': 'Welcome, Chronos Agent. Temporal anomalies threaten my eternal legacy! Solve the riddles of ancient mathematics, and restore the pyramid\'s timeline.',
            'Knight Commander': 'Castle walls burn through time! Temporal rifts tear our stronghold apart! Prove your tactical brilliance and save the kingdom!',
            'Leonardo da Vinci': 'My inventions vanish! My genius burns in temporal fire! Solve my geometric puzzles and save the Renaissance!',
            'Mission Control': 'CRITICAL timeline failure! Apollo program COLLAPSES! We need PERFECT calculations! Can you restore mankind\'s reach for stars?'
        }

        logging.info(
            f"Game data loaded: {len(self.eras)} eras with {len(self.puzzles)} puzzles")

    def start_new_game(self):
        """Initialize new game session."""
        self.current_screen = 'eraSelection'
        self.health = 100
        self.inventory = []
        self.puzzles_solved = {}
        self.current_era = None
        self.sound_enabled = True
        self.hints_used = {}
        self.attempts = {}
        self.score = 0
        self.achievements = []
        self.current_puzzle_index = 0
        self.difficulty_setting = 'normal'
        self.game_start_time = datetime.now()
        logging.info("New game started")

    def select_era(self, era_id):
        """Select a historical era."""
        era = next((e for e in self.eras if e['id'] == era_id), None)
        if era:
            self.current_era = era
            self.current_screen = 'game'
            self.npc_dialog = self.npc_messages.get(
                era['npc'], 'Welcome traveler!')
            self.current_puzzle_index = 0
            logging.info(f"Era selected: {era_id} ({era['name']})")
        else:
            logging.error(f"Invalid era: {era_id}")

    def get_current_puzzle(self):
        """Get the next unsolved puzzle in current era."""
        if not self.current_era:
            return None

        era_id = self.current_era['id']

        # Get next unsolved puzzle (1-6 in current era)
        for i in range(1, 7):
            puzzle_id = f"{era_id}_puzzle_{i}"
            if puzzle_id not in self.puzzles_solved:
                return puzzle_id

        return None  # All puzzles in era solved

    def set_difficulty(self, difficulty):
        """Set game difficulty (normal, hard, expert)."""
        if difficulty in ['normal', 'hard', 'expert']:
            self.difficulty_setting = difficulty
            logging.info(f"Difficulty set to: {difficulty}")
            return True
        return False

    def get_difficulty(self):
        """Get current difficulty."""
        return self.difficulty_setting

    def get_puzzle_points_modifier(self):
        """Get points multiplier based on game difficulty."""
        modifiers = {
            'normal': 1.0,
            'hard': 1.3,
            'expert': 1.6
        }
        return modifiers.get(self.difficulty_setting, 1.0)

    def solve_puzzle(self, puzzle_id, selected_idx):
        """Process puzzle answer."""
        puzzle = self.puzzles.get(puzzle_id)
        if not puzzle or not (0 <= selected_idx < len(puzzle['options'])):
            return {
                'success': False,
                'message': 'Invalid puzzle or answer',
                'explanation': 'An error occurred'
            }

        if puzzle_id not in self.attempts:
            self.attempts[puzzle_id] = 0
        self.attempts[puzzle_id] += 1

        is_correct = selected_idx == puzzle['correct']

        if is_correct:
            self.puzzles_solved[puzzle_id] = True
            self.inventory.append(puzzle['reward'])

            # Calculate points with difficulty multiplier
            points_multiplier = self.get_puzzle_points_modifier()
            points = int(puzzle.get('base_points', 100) * points_multiplier)
            self.score += points

            # Restore health on correct answer
            self.health = min(self.health + 15, 100)

            logging.info(f"✓ Puzzle solved: {puzzle_id} +{points} points")

            return {
                'success': True,
                'message': f"✅ CORRECT! +{points} points! Reward: {puzzle['reward']}",
                'explanation': puzzle['explanation'],
                'reward': puzzle['reward'],
                'points': points
            }
        else:
            # Penalty for wrong answer
            self.health = max(self.health - 10, 0)
            logging.info(
                f"✗ Puzzle failed: {puzzle_id} (Attempt {self.attempts[puzzle_id]})")

            return {
                'success': False,
                'message': f"❌ INCORRECT! Timeline integrity -10%",
                'explanation': puzzle['explanation'],
                'correct_answer': puzzle['options'][puzzle['correct']],
                'attempt': self.attempts[puzzle_id]
            }

    def get_hint(self, puzzle_id):
        """Get a hint for the current puzzle."""
        puzzle = self.puzzles.get(puzzle_id)
        if not puzzle:
            return {'success': False, 'message': 'Puzzle not found'}

        if puzzle_id not in self.hints_used:
            self.hints_used[puzzle_id] = 0

        if self.hints_used[puzzle_id] >= 2:
            return {'success': False, 'message': 'No more hints available'}

        self.hints_used[puzzle_id] += 1
        self.health = max(self.health - 5, 0)

        return {
            'success': True,
            'hint': puzzle.get('hint', 'Think carefully'),
            'message': f"💡 Hint revealed! (-5% health, {2 - self.hints_used[puzzle_id]} hints left)"
        }

    def next_era(self):
        """Navigate to next era."""
        if not self.current_era:
            return

        current_idx = next(
            (i for i, e in enumerate(self.eras)
             if e['id'] == self.current_era['id']),
            -1
        )

        if current_idx >= 0 and current_idx < len(self.eras) - 1:
            self.select_era(self.eras[current_idx + 1]['id'])
            logging.info("Navigation: Next era selected")

    def previous_era(self):
        """Navigate to previous era."""
        if not self.current_era:
            return

        current_idx = next(
            (i for i, e in enumerate(self.eras)
             if e['id'] == self.current_era['id']),
            -1
        )

        if current_idx > 0:
            self.select_era(self.eras[current_idx - 1]['id'])
            logging.info("Navigation: Previous era selected")

    def get_completion_percentage(self):
        """
        Calculate timeline completion.

        FIXED SYSTEM:
        - Each puzzle = 4.2% (100% ÷ 24 puzzles)
        - 6 puzzles per era × 4 eras = 24 total
        - Complete all 24 = 100%
        """
        # Count solved puzzles
        solved_count = len(self.puzzles_solved)

        # Each puzzle is worth 1/24 = 4.166...%
        percentage = (solved_count / 24) * 100

        # Return as integer, capped at 100
        return min(int(round(percentage)), 100)

    def is_era_complete(self):
        """Check if current era has all 6 puzzles solved."""
        if not self.current_era:
            return False

        era_id = self.current_era['id']
        for i in range(1, 7):
            puzzle_id = f"{era_id}_puzzle_{i}"
            if puzzle_id not in self.puzzles_solved:
                return False
        return True

    def get_game_state(self):
        """Get complete game state for frontend."""
        completion = self.get_completion_percentage()

        return {
            'screen': self.current_screen,
            'era': self.current_era,
            'health': self.health,
            'inventory': self.inventory,
            'puzzles_solved': self.puzzles_solved,
            'sound_enabled': self.sound_enabled,
            'completion': completion,
            'npc_dialog': self.npc_dialog,
            'eras': self.eras,
            'puzzles': self.puzzles,
            'score': self.score,
            'achievements': self.achievements,
            'difficulty': self.difficulty_setting,
            'is_era_complete': self.is_era_complete(),
            'mission_complete': completion == 100
        }

    def is_game_over(self):
        """Check if game over (health = 0)."""
        return self.health <= 0

    def is_mission_complete(self):
        """Check if mission complete (all puzzles solved = 100%)."""
        return self.get_completion_percentage() == 100
