import os
from pathlib import Path

# The exact structure from the FESS SDD (Section 3.1)
FOLDERS =[
    "models",
    "controllers",
    "views/widgets",
    "services",
    "data/profiles",
    "data/bout_logs",
    "data/tournaments",
    "assets/styles",
    "assets/sounds",
    "tests"
]

FILES = {
    "main.py": "# Entry point for FESS Scoring Software\n",
    "config.py": "# Constants, default keybindings, file paths\n",
    "models/__init__.py": "",
    "models/bout.py": "",
    "models/fencer_profile.py": "",
    "models/bout_log.py": "",
    "models/tournament.py": "",
    "models/enums.py": "",
    "controllers/__init__.py": "",
    "controllers/bout_controller.py": "",
    "controllers/input_controller.py": "",
    "controllers/stats_controller.py": "",
    "views/__init__.py": "",
    "views/main_menu.py": "",
    "views/scoreboard_view.py": "",
    "views/mode_select_view.py": "",
    "views/profile_view.py": "",
    "views/controls_view.py": "",
    "views/tournament_view.py": "",
    "views/widgets/__init__.py": "",
    "views/widgets/timer_widget.py": "",
    "views/widgets/score_widget.py": "",
    "views/widgets/period_widget.py": "",
    "services/__init__.py": "",
    "services/gamepad_service.py": "",
    "services/storage_service.py": "",
    "services/sound_service.py": "",
    "assets/styles/scoreboard.qss": "/* Main Qt Stylesheet */\n",
    "tests/__init__.py": "",
    "tests/test_bout.py": "",
    "tests/test_timer.py": "",
    "tests/test_tournament.py": "",
}

def build_scaffold():
    # 1. Create Directories
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
        # Add a .gitkeep to empty data folders so Git tracks them
        if folder.startswith("data/") or folder.startswith("assets/"):
            Path(f"{folder}/.gitkeep").touch()
            
    # 2. Create Files
    for filepath, content in FILES.items():
        with open(filepath, "w") as f:
            f.write(content)
            
    print("✅ FESS project scaffolded successfully!")

if __name__ == "__main__":
    build_scaffold()