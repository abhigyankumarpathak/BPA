# ChronoQuest: Fractures in Time - Complete User Manual

## EXECUTIVE SUMMARY

ChronoQuest is a comprehensive time-travel puzzle adventure game where players 
assume the role of Chronos Agents tasked with restoring critical timeline anomalies.

**Genre**: Puzzle Adventure, Turn-Based
**Platform**: Windows, macOS, Linux
**Language**: Python 3.7+
**No External Dependencies Required**

## COMPILATION & INSTALLATION

### System Requirements

**Minimum:**
- Python 3.7 or higher
- 50MB disk space
- UTF-8 compatible terminal
- 64-bit processor

**Recommended:**
- Python 3.9 or 3.10
- 100MB free disk space
- Modern terminal (Windows 10+, macOS 10.14+, Linux)
- 1920x1080 display resolution

### Step-by-Step Installation

1. **Download Files**
   - Download all 5 Python files
   - Save in same folder: main.py, game_engine.py, database.py, ui.py

2. **Verify Python Installation**
```bash
   # Windows
   python --version
   
   # macOS/Linux
   python3 --version
```
   Should show Python 3.7 or higher

3. **Navigate to Game Directory**
```bash
   # Windows
   cd path\to\ChronoQuest
   
   # macOS/Linux
   cd path/to/ChronoQuest
```

4. **Run the Game**
```bash
   # Windows
   python main.py
   
   # macOS/Linux
   python3 main.py
```

5. **Verify Launch**
   - Main menu should display
   - All text properly formatted
   - Game ready to play

### Troubleshooting Installation

**Error: "python: command not found"**
- Solution: Use `python3` instead of `python`
- Or install Python from python.org

**Error: "ModuleNotFoundError"**
- Solution: Ensure all 4 .py files in same directory
- Check filename spelling

**Error: "UnicodeEncodeError"**
- Solution: Update terminal encoding to UTF-8
- Windows: Use Windows Terminal instead of old CMD

## HOW TO PLAY

### Main Game Flow

1. **Start Game** → Select "New Game" from main menu
2. **Choose Era** → Select one of 4 historical periods
3. **Solve Puzzle** → Answer the NPC's challenge
4. **Collect Reward** → Receive artifact on success
5. **Progress** → Navigate between eras
6. **Win** → Complete all 4 eras with 100% restoration

### Detailed Gameplay

#### Main Menu