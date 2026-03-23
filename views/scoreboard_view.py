from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent, QFont
from models.bout import BoutTimer

from config import COLOR_LEFT_RED, COLOR_RIGHT_GREEN

class ScoreboardView(QWidget):
    def __init__(self):
        super().__init__()
        
        
        # --- Temporary state for testing (move to BoutController later) ---
        self.left_score = 0
        self.right_score = 0

        self.init_ui()
        
        # Initialize timer
        self.timer = BoutTimer()
        self.timer.time_updated.connect(self.update_timer_display)
        self.timer.set_time(3 * 60 * 1000) # Set to 3:00 minutes (in milliseconds)        


    def init_ui(self):
        # --- Layouts ---
        main_layout = QVBoxLayout()
        score_layout = QHBoxLayout()
        
        # --- Fonts ---
        score_font = QFont("Arial", 140, QFont.Weight.Bold)
        timer_font = QFont("Arial", 120, QFont.Weight.Bold)
        
        # --- Widgets ---
        # 1. Top Status Bar
        self.status_label = QLabel("READY (Press Space to Start)")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 28px; color: #AAAAAA; margin-bottom: 20px;")
        
        # 2. Left Score (Red)
        self.left_label = QLabel(str(self.left_score))
        self.left_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.left_label.setFont(score_font)
        self.left_label.setStyleSheet(f"color: {COLOR_LEFT_RED};")
        
        # 3. Center Timer
        #print("CENTER TIMER")
        self.timer_label = QLabel("03:00.0")
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer_label.setFont(timer_font)
        
        # 4. Right Score (Green)
        self.right_label = QLabel(str(self.right_score))
        self.right_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.right_label.setFont(score_font)
        self.right_label.setStyleSheet(f"color: {COLOR_RIGHT_GREEN};")
        
        # --- Assembly ---
        score_layout.addWidget(self.left_label)
        score_layout.addWidget(self.timer_label, stretch=1)
        score_layout.addWidget(self.right_label)
        
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(score_layout)
        
        self.setLayout(main_layout)
        
        # Allows this specific widget to capture keystrokes
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def update_timer_display(self, ms: int):
        # Converts milliseconds to MM:SS and handles tenths of a second
        total_seconds = ms / 1000.0
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        tenths = int((ms % 1000) / 100)
        
        # Show tenths of a second precision only if under 1 minute, per fencing norms
        if minutes > 0:
            time_str = f"{minutes:02d}:{seconds:02d}"
        else:
            time_str = f"{minutes:02d}:{seconds:02d}.{tenths}"
            
        self.timer_label.setText(time_str)

    def keyPressEvent(self, event: QKeyEvent):
        # TEMPORARY hardware/keyboard bindings for testing
        key = event.key()
        
        # START / PAUSE (Spacebar)
        if key == Qt.Key.Key_Space:
            if self.timer.is_running:
                self.timer.pause()
                self.status_label.setText("PAUSED (Press Space to Resume)")
            else:
                self.timer.resume()
                self.status_label.setText("RUNNING - Allez!")
        
        # INCREMENT LEFT SCORE (Left Arrow)
        elif key == Qt.Key.Key_Left:
            self.left_score += 1
            self.left_label.setText(str(self.left_score))

        # DECREMENT LEFT SCORE (UP Arrow)
        elif key == Qt.Key.Key_Up:
            if (self.left_score != 0):
                self.left_score -= 1
                self.left_label.setText(str(self.left_score))
        
        # INCREMENT RIGHT SCORE (Right Arrow)
        elif key == Qt.Key.Key_Right:
            self.right_score += 1
            self.right_label.setText(str(self.right_score))

        # DECREMENT RIGHT SCORE (Down Arrow)
        elif key == Qt.Key.Key_Down:
            if (self.right_score != 0):
                self.right_score -= 1
                self.right_label.setText(str(self.right_score))
        
        # FRIMB RED TOUCH ('R') - Hardware Simulation
        elif key == Qt.Key.Key_R:
            if self.timer.is_running:
                self.timer.pause()
                self.status_label.setText("HALT - RED TOUCH DETECTED")
        
        # FRIMB GREEN TOUCH ('G') - Hardware Simulation
        elif key == Qt.Key.Key_G:
            if self.timer.is_running:
                self.timer.pause()
                self.status_label.setText("HALT - GREEN TOUCH DETECTED")
                
        # RESET BOUT TEST (Backspace)
        elif key == Qt.Key.Key_Backspace:
            self.timer.set_time(3 * 60 * 1000)
            self.left_score = 0
            self.right_score = 0
            self.left_label.setText("0")
            self.right_label.setText("0")
            self.status_label.setText("READY (Press Space to Start)")