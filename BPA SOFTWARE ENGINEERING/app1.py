"""
ChronoQuest: Fractures in Time - Flask Web Server (FIXED v5.0)
BPA Software Engineering Team Competition - 2026
"""

from flask import Flask, render_template, jsonify, request, session
from flask_session import Session
import os
import secrets
import logging
from game_engine import GameEngine
from database import GameDatabase

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('chronoquest_debug.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__, template_folder='templates', static_folder='static')

# Flask configuration
app.config.update(
    SECRET_KEY=secrets.token_hex(32),
    SESSION_TYPE='filesystem',
    SESSION_FILE_DIR='./flask_session',
    SESSION_PERMANENT=False,
    SESSION_USE_SIGNER=True,
    SESSION_KEY_PREFIX='chronoquest_',
)

# Create necessary directories
os.makedirs(app.config['SESSION_FILE_DIR'], exist_ok=True)
os.makedirs('templates', exist_ok=True)
os.makedirs('static', exist_ok=True)

# Initialize session
Session(app)

# Store game instances per session
active_games = {}


def get_game_engine():
    """Get or create game engine for current session."""
    session_id = session.get('game_id')
    if not session_id:
        return None

    if session_id not in active_games:
        active_games[session_id] = GameEngine()
        logging.info(f"New game engine for session: {session_id}")

    return active_games[session_id]


@app.route('/')
def index():
    """Serve the main game page."""
    if 'game_id' not in session:
        session['game_id'] = secrets.token_hex(16)
        logging.info(f"New session: {session['game_id']}")

    return render_template('index.html')


@app.route('/api/game/init', methods=['POST'])
def init_game():
    """Initialize a new game."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No session'}), 400

        # Get difficulty from request
        data = request.get_json() or {}
        difficulty = data.get('difficulty', 'normal')

        engine.start_new_game()
        engine.set_difficulty(difficulty)

        logging.info(f"Game initialized with difficulty: {difficulty}")
        return jsonify({'success': True, 'message': 'Game started'})
    except Exception as e:
        logging.error(f"Init error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/game/state')
def get_game_state():
    """Get current game state."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'error': 'No active game'}), 400

        state = engine.get_game_state()
        return jsonify(state)
    except Exception as e:
        logging.error(f"State error: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/eras')
def get_eras():
    """Get all available eras."""
    try:
        engine = get_game_engine() or GameEngine()
        return jsonify({'eras': engine.eras})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/era/select', methods=['POST'])
def select_era():
    """Select an era to play."""
    try:
        data = request.get_json()
        era_id = data.get('era_id')

        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        engine.select_era(era_id)
        state = engine.get_game_state()

        # Get current puzzle for this era
        current_puzzle_id = engine.get_current_puzzle()
        current_puzzle = None
        if current_puzzle_id and current_puzzle_id in engine.puzzles:
            current_puzzle = {
                'id': current_puzzle_id,
                'data': engine.puzzles[current_puzzle_id]
            }

        return jsonify({
            'success': True,
            'state': state,
            'current_puzzle': current_puzzle
        })
    except Exception as e:
        logging.error(f"Select era error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/puzzle/current', methods=['GET'])
def get_current_puzzle():
    """Get the current puzzle for the era."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        puzzle_id = engine.get_current_puzzle()
        if not puzzle_id:
            return jsonify({
                'success': False,
                'message': 'Era complete! Move to next era.'
            }), 200

        puzzle = engine.puzzles.get(puzzle_id)
        if not puzzle:
            return jsonify({'success': False, 'error': 'Puzzle not found'}), 400

        return jsonify({
            'success': True,
            'puzzle_id': puzzle_id,
            'puzzle': puzzle
        })
    except Exception as e:
        logging.error(f"Get puzzle error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/puzzle/solve', methods=['POST'])
def solve_puzzle():
    """Solve a puzzle."""
    try:
        data = request.get_json()
        puzzle_id = data.get('puzzle_id')
        answer_idx = data.get('answer_idx')

        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        result = engine.solve_puzzle(puzzle_id, answer_idx)
        state = engine.get_game_state()

        return jsonify({
            'success': True,
            'result': result,
            'state': state
        })
    except Exception as e:
        logging.error(f"Puzzle solve error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/puzzle/hint', methods=['POST'])
def get_hint():
    """Get a hint for a puzzle."""
    try:
        data = request.get_json()
        puzzle_id = data.get('puzzle_id')

        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        result = engine.get_hint(puzzle_id)

        if result['success']:
            state = engine.get_game_state()
            return jsonify({
                'success': True,
                'hint': result['hint'],
                'message': result['message'],
                'state': state
            })
        return jsonify(result)
    except Exception as e:
        logging.error(f"Hint error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/era/next', methods=['POST'])
def next_era():
    """Move to next era."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        engine.next_era()
        state = engine.get_game_state()

        # Get first puzzle of new era
        current_puzzle_id = engine.get_current_puzzle()
        current_puzzle = None
        if current_puzzle_id:
            current_puzzle = {
                'id': current_puzzle_id,
                'data': engine.puzzles[current_puzzle_id]
            }

        return jsonify({
            'success': True,
            'state': state,
            'current_puzzle': current_puzzle
        })
    except Exception as e:
        logging.error(f"Next era error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/era/previous', methods=['POST'])
def previous_era():
    """Move to previous era."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        engine.previous_era()
        state = engine.get_game_state()

        current_puzzle_id = engine.get_current_puzzle()
        current_puzzle = None
        if current_puzzle_id:
            current_puzzle = {
                'id': current_puzzle_id,
                'data': engine.puzzles[current_puzzle_id]
            }

        return jsonify({
            'success': True,
            'state': state,
            'current_puzzle': current_puzzle
        })
    except Exception as e:
        logging.error(f"Previous era error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/game/save', methods=['POST'])
def save_game():
    """Save game state."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        db = GameDatabase()
        result = db.save_game(engine)
        return jsonify(result)
    except Exception as e:
        logging.error(f"Save error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/game/load', methods=['POST'])
def load_game():
    """Load saved game."""
    try:
        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        db = GameDatabase()
        result = db.load_game(engine)

        if result['success']:
            return jsonify({
                'success': True,
                'state': engine.get_game_state(),
                'message': result['message']
            })
        return jsonify(result)
    except Exception as e:
        logging.error(f"Load error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/game/save-check')
def check_save():
    """Check if save data exists."""
    try:
        db = GameDatabase()
        exists = db.has_save_data()
        info = db.get_save_info() if exists else None
        return jsonify({'exists': exists, 'info': info})
    except Exception as e:
        return jsonify({'exists': False, 'error': str(e)})


@app.route('/api/game/delete-save', methods=['POST'])
def delete_save():
    """Delete save data."""
    try:
        db = GameDatabase()
        result = db.delete_save()
        return jsonify(result)
    except Exception as e:
        logging.error(f"Delete save error: {str(e)}")
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/difficulty/set', methods=['POST'])
def set_difficulty():
    """Set game difficulty."""
    try:
        data = request.get_json()
        difficulty = data.get('difficulty', 'normal')

        engine = get_game_engine()
        if not engine:
            return jsonify({'success': False, 'error': 'No active game'}), 400

        success = engine.set_difficulty(difficulty)

        return jsonify({
            'success': success,
            'difficulty': engine.get_difficulty(),
            'message': f'Difficulty set to {difficulty}'
        })
    except Exception as e:
        logging.error(f"Set difficulty error: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500


if __name__ == '__main__':
    logging.info("ChronoQuest Flask Server Starting...")
    logging.info("Visit http://127.0.0.1:5000 in your browser")
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
