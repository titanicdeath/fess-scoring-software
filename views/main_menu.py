import sys

from config import Color

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
) 



class MainMenu(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("FRIMB Main Menu")
        self.resize(1024, 600)
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")

        self.myColor = ["#9C1A0E","#0E509C","#1E3147","#9C7A0E"]

        self.init_ui()

        widget = QWidget()
        widget.setLayout(self.menuLayout)
        self.setCentralWidget(widget)

    def init_ui(self):
        self.menuLayout = QVBoxLayout()

        buttonI = QPushButton(parent=self)
        buttonII = QPushButton(parent=self)
        buttonIII= QPushButton(parent=self)
        buttonIV = QPushButton(parent=self)

        buttonI
        buttonII
        buttonIII
        buttonIV

        buttonI.setFixedSize(100,60)
        buttonII.setFixedSize(100,60)
        buttonIII.setFixedSize(100,60)
        buttonIV.setFixedSize(100,60)

        buttonI = QPushButton(text="Center", parent=self)
        buttonII = QPushButton(text="Center", parent=self)
        buttonIII = QPushButton(text="Center", parent=self)
        buttonIV = QPushButton(text="Center", parent=self)

        self.menuLayout.addWidget(Color(self.myColor[0]))
        self.menuLayout.addWidget(Color(self.myColor[1]))
        self.menuLayout.addWidget(Color(self.myColor[2]))
        self.menuLayout.addWidget(Color(self.myColor[3]))
        


app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()