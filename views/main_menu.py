from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QSizePolicy,
)


# I don't know why I put PALETTE in the SideTab. At this point might be painful to move. Or at least right now at 1:50 am
try:
    from side_tab import SideTab, PALETTE
except ImportError:
    from .side_tab import SideTab, PALETTE


class MenuTile(QFrame):
    clicked = pyqtSignal(str)

    def __init__(self, title: str, subtitle: str, accent: str, route_name: str, parent=None):
        super().__init__(parent)
        self.title = title
        self.subtitle = subtitle
        self.accent = accent
        self.route_name = route_name
        self.hovered = False

        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setMinimumHeight(210)
        self.setObjectName("menuTile")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Creates the border/outline of the menu tiles.
        accent_bar = QFrame()
        accent_bar.setFixedHeight(6)
        accent_bar.setStyleSheet(f"background-color: {accent}; border: none; border-radius: 3px;")

        # Creates and formats the text for the title of the respective card (i.g. Combat Modes)
        title_label = QLabel(title)
        title_label.setStyleSheet(f"color: {PALETTE['text']}; font-size: 28px; font-weight: 750;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Creates and formats essentially a short description of the tile.
        subtitle_label = QLabel(subtitle)
        subtitle_label.setWordWrap(True)
        subtitle_label.setStyleSheet(f"color: {PALETTE['muted']}; font-size: 15px;")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Not sure if you are needed
        # open_label = QLabel("Open")
        # open_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        # open_label.setStyleSheet(f"color: {accent}; font-size: 13px; font-weight: 700;")

        layout.addWidget(accent_bar)
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        layout.addStretch()
        # layout.addWidget(open_label)

        self._refresh_style()

    def _refresh_style(self):
        bg = PALETTE["surface_3"] if self.hovered else PALETTE["surface"]
        self.setStyleSheet(f"""
            QFrame#menuTile {{
                background-color: {bg};
                border: 1px solid {self.accent};
                border-radius: 18px;
            }}
        """)

    def enterEvent(self, event):
        self.hovered = True
        self._refresh_style()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.hovered = False
        self._refresh_style()
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.route_name)
        super().mousePressEvent(event)


class MainMenu(QWidget):
    nav_requested = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("mainMenu")
        self._build_ui()
        self._apply_style()

    def _build_ui(self):
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.side_tab = SideTab()

        root.addWidget(self.side_tab)

        content_shell = QWidget()
        content_layout = QVBoxLayout(content_shell)
        content_layout.setContentsMargins(28, 28, 28, 28)
        content_layout.setSpacing(22)

        card = self._build_card()
        tile_grid = self._build_tile_grid()

        content_layout.addWidget(card)
        content_layout.addLayout(tile_grid, 1)

        root.addWidget(content_shell, 1)

    # Title Card Function
    # Function for creating the title card centered at the top of the screen on the main menu
    def _build_card(self):
        card = QFrame()
        card.setObjectName("card")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(8)

        title = QLabel("FESS Digital Scoring Interface")
        title.setStyleSheet(f"color: {PALETTE['text']}; font-size: 34px; font-weight: 800;")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(title)

        return card

    def _build_tile_grid(self):
        grid = QGridLayout()
        grid.setHorizontalSpacing(18)
        grid.setVerticalSpacing(18)

        tiles = [
            (
                "Combat Modes",
                "Select preset modes and launch a bout.",
                PALETTE["red"],
                "combat",
            ),
            (
                "Profiles & Stats",
                "View, compare, and create fencer profiles.",
                PALETTE["green"],
                "profiles",
            ),
            (
                "Controls",
                "Keyboard, gamepad, and FRIMB remapping.",
                PALETTE["gold"],
                "controls",
            ),
            (
                "Tournament",
                "Roster, bracket flow, and DE launches.",
                PALETTE["bronze"],
                "tournament",
            ),
        ]

        # Thank you ChatGPT. 
        # I got no clue how the you were able to condense my monstrosity of loops that took up 38 lines into only 5 lines. I could not even articulate what the hell it was supposed to do.
        # I mean seriously every single time I would add/modify one of the objects my loops woujld break. I really mean every single time.
        # like seriously wtf are they gonna need humans for? 
        # An LLM could do in minutes that I spent hours trying to do.
        for index, (title, subtitle, accent, route_name) in enumerate(tiles):
            tile = MenuTile(title, subtitle, accent, route_name)
            tile.clicked.connect(self.side_tab.open_page)
            row, col = divmod(index, 2)
            grid.addWidget(tile, row, col)

        return grid

    def _apply_style(self):
        self.setStyleSheet(f"""
            QWidget#mainMenu {{
                background-color: {PALETTE["bg"]};
            }}
            QFrame#card {{
                background-color: {PALETTE["surface"]};
                border: 1px solid {PALETTE["border"]};
                border-radius: 22px;
            }}
        """)