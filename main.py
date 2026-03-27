import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from views.main_menu import MainMenu



APP_STYLESHEET = """
QWidget {
    background-color: #0B1118;
    color: #EAF0F7;
    font-family: "Segoe UI";
}
QToolTip {
    background-color: #121A23;
    color: #EAF0F7;
    border: 1px solid #263545;
    padding: 6px;
}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FESS Digital Scoring Interface")
        self.resize(1440, 900)
        self.setMinimumSize(1100, 700)
        self.setCentralWidget(MainMenu())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(APP_STYLESHEET)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())