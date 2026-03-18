# Entry point for FESS Scoring Software
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from views.scoreboard_view import ScoreboardView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("FESS Digital Scoring Interface")
        self.resize(1024, 600)
        
        # Apply a sleek dark theme globally to the window
        self.setStyleSheet("background-color: #121212; color: #FFFFFF;")
        
        # Instantiate and set our ScoreboardView as the main content
        self.scoreboard = ScoreboardView()
        self.setCentralWidget(self.scoreboard)

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())