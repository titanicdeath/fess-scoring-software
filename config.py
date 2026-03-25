# Constants, default keybindings, file paths
import os
from pathlib import Path

# --- File Paths ---
# Ensures paths work correctly whether on Windows, Mac, or Linux
BASE_DIR = Path(__file__).parent.resolve()
DATA_DIR = BASE_DIR / "data"
PROFILES_DIR = DATA_DIR / "profiles"
BOUT_LOGS_DIR = DATA_DIR / "bout_logs"
TOURNAMENTS_DIR = DATA_DIR / "tournaments"
CONFIG_FILE = BASE_DIR / "config.json"

# --- UI Constants ---
# Colors mapped to match the FRIMB hardware channels
COLOR_LEFT_RED = "#E24B4A"
COLOR_RIGHT_GREEN = "#1D9E75"

# --- Default Configurations ---
# JSON schema 
DEFAULT_CONFIG = {
    "keybindings": {
        "keyboard": {
            "START_TIMER": "Space",
            "AWARD_POINT_LEFT": "Left",
            "AWARD_POINT_RIGHT": "Right",
            "UNDO": "Backspace",
            "DELAY_RESTART": "D",
            "END_SESSION": "End",
            "NAVIGATE_UP": "Up",
            "NAVIGATE_DOWN": "Down",
            "NAVIGATE_LEFT": "Left",
            "NAVIGATE_RIGHT": "Right",
            "SELECT": "Return",  # PyQt recognizes Enter as 'Return'
            "BACK": "Escape"
        },
        "gamepad": {
            "START_TIMER": "BTN_0",       # Usually A/Cross
            "AWARD_POINT_LEFT": "BTN_4",  # Usually L Bumper
            "AWARD_POINT_RIGHT": "BTN_5", # Usually R Bumper
            "UNDO": "BTN_3",              # Usually Y/Triangle
            "DELAY_RESTART": "BTN_1",     # Usually B/Circle
            "END_SESSION": "BTN_7"        # Usually Start
        },
        "frimb": {
            "FRIMB_RED": "R",
            "FRIMB_GREEN": "G"
        }
    },
    "display": {
        "fullscreen": False,
        "theme": "dark",
        "left_fencer_color": COLOR_LEFT_RED,
        "right_fencer_color": COLOR_RIGHT_GREEN
    }
}

from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget


class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)