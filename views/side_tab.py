from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QMainWindow
from views.scoreboard_view import ScoreboardView


PALETTE = {
    "bg": "#0B1118",
    "surface": "#121A23",
    "surface_2": "#17212C",
    "surface_3": "#1D2935",
    "border": "#263545",
    "text": "#EAF0F7",
    "muted": "#95A4B4",
    "gold": "#C9A54B",
    "navy": "#244B70",
    "slate": "#31465A",
    "red": "#8F3028",
    "green": "#2E6E67",
    "bronze": "#8A4B22",
}


class SideTab(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(220)
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {PALETTE["surface"]};
                border-right: 1px solid {PALETTE["border"]};
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        top_row = QHBoxLayout()

        self.toggle_button = QPushButton("≡")
        self.toggle_button.setFixedSize(42, 42)

        self.brand_title = QLabel("FESS")

        top_row.addWidget(self.toggle_button)
        top_row.addWidget(self.brand_title)

        layout.addLayout(top_row)

        layout.addWidget(self.make_button("Main menu", "home"))
        layout.addWidget(self.make_button("Combat", "combat"))
        layout.addWidget(self.make_button("Profiles", "profiles"))
        layout.addWidget(self.make_button("Controls", "controls"))
        layout.addWidget(self.make_button("Tournament", "tournament"))
        layout.addWidget(self.make_button("[Temp] Scoreboard Directeur", "scoreboard_directeur"))
        layout.addWidget(self.make_button("[Temp] Scoreboard Automatic", "scoreboard_automatic"))

        layout.addStretch()

    def make_button(self, text, route_name):
        button = QPushButton(text)
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setMinimumHeight(46)

        button.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {PALETTE["text"]};
                border: 1px solid transparent;
                border-radius: 12px;
                text-align: left;
                padding: 10px 14px;
                font-size: 14px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {PALETTE["surface_3"]};
                border: 1px solid {PALETTE["border"]};
            }}
        """)

        button.clicked.connect(lambda: self.open_page(route_name))
        return button

    def open_page(self, route_name):
        window = self.window()

        if not isinstance(window, QMainWindow):
            return

        if route_name == "home":
            try:
                from views.main_menu import MainMenu
            except ImportError:
                from main_menu import MainMenu

            window.setCentralWidget(MainMenu())

        elif route_name == "scoreboard_directeur":
            scoreboard = ScoreboardView("directeur")
            window.setCentralWidget(scoreboard)
            scoreboard.setFocus()

        elif route_name == "scoreboard_automatic":
            scoreboard = ScoreboardView("automatic")
            window.setCentralWidget(scoreboard)
            scoreboard.setFocus()

        else:
            print("Open route:", route_name)