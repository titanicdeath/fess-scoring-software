from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
)

# I really don't know why I put this here. I should move it to main.py or to main_menu.py
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


class NavButton(QPushButton):
    def __init__(self, full_text: str, short_text: str, route_name: str):
        super().__init__(full_text)
        self.full_text = full_text
        self.short_text = short_text
        self.route_name = route_name

        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(46)
        self.setToolTip(full_text)

        self._apply_style(collapsed=False) # WIP Collapse item. 

    #
    # Work in Progress Section | I really don't understand this for collapsing tabs. like I am so tempted to abdandon collapse 
    #
    def set_collapsed(self, collapsed: bool):
        pass

    def _apply_style(self, collapsed: bool):
        align = "center" if collapsed else "left"
        padding = "10px 0px" if collapsed else "10px 14px"

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {PALETTE["text"]};
                border: 1px solid transparent;
                border-radius: 12px;
                text-align: {align};
                padding: {padding};
                font-size: 14px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {PALETTE["surface_3"]};
                border: 1px solid {PALETTE["border"]};
            }}
            QPushButton:checked {{
                background-color: {PALETTE["navy"]};
                border: 1px solid {PALETTE["gold"]};
                color: white;
            }}
        """)


class SideTab(QFrame):
    nav_requested = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._collapsed = False
        self.expanded_width = 220
        self.collapsed_width = 72
        self.nav_buttons = {}

        self.setObjectName("sideTab")
        self.setFixedWidth(self.expanded_width)

        self._build_ui()
        self._apply_shell_style()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        top_row = QHBoxLayout()

        self.toggle_button = QPushButton("≡")
        self.button_toggle()
        

        self.brand_title = QLabel("FESS")
        self.brand_title.setStyleSheet(f"color: {PALETTE['text']}; font-size: 22px; font-weight: 800;")

        top_row.addWidget(self.toggle_button)
        top_row.addWidget(self.brand_title, 1)
        layout.addLayout(top_row)

        self.brand_subtitle = QLabel("Quick nav")
        self.brand_subtitle.setStyleSheet(f"color: {PALETTE['muted']}; font-size: 12px;")
        layout.addWidget(self.brand_subtitle)

        nav_specs = [
                    ("Main menu", "M", "home"),
                    ("Combat", "C", "combat"),
                    ("Profiles", "P", "profiles"),
                    ("Controls", "K", "controls"),
                    ("Tournament", "T", "tournament"),
                    ("[Temp] Scoreboard", "S", "scoreboard")]

        for full_text, short_text, route_name in nav_specs:
            button = NavButton(full_text, short_text, route_name)
            button.clicked.connect(
                lambda checked=False, route=route_name: self.nav_requested.emit(route)
            )
            self.nav_buttons[route_name] = button
            layout.addWidget(button)

        layout.addStretch()


    def button_toggle(self):
        self.toggle_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.toggle_button.setFixedSize(42, 42)
        self.toggle_button.clicked.connect(self.toggle_collapsed)
        self.toggle_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {PALETTE["surface_2"]};
                color: {PALETTE["text"]};
                border: 1px solid {PALETTE["border"]};
                border-radius: 12px;
                font-size: 18px;
                font-weight: 700;
            }}
            QPushButton:hover {{
                background-color: {PALETTE["surface_3"]};
            }}
        """)

    def _apply_shell_style(self):
        self.setStyleSheet(f"""
            QFrame#sideTab {{
                background-color: {PALETTE["surface"]};
                border-right: 1px solid {PALETTE["border"]};
            }}
        """)

    def set_active_route(self, route_name: str):
        for name, button in self.nav_buttons.items():
            button.setChecked(name == route_name)

    def toggle_collapsed(self):
        # Will do later
        pass