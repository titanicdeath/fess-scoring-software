# Entry point for FESS Scoring Software
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from views.scoreboard_view import ScoreboardView
from views.main_menu import MainMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FESS Digital Scoring Interface")
        self.resize(1024, 600)
        
        # Apply a dark theme globally to the window
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")
        
        # Instantiate and set ScoreboardView as main content
        self.scoreboard = ScoreboardView()
        self.setCentralWidget(self.scoreboard)

if __name__ == "__main__":

    test = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    test.exec()

    # Create the Qt Application
    

    app = QApplication(sys.argv)
    
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())