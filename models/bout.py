from PyQt6.QtCore import QObject, QTimer, QElapsedTimer, pyqtSignal

class BoutTimer(QObject):
    # --- Qt Signals ---
    # UI will connect to update the screen
    time_updated = pyqtSignal(int)  # Remaining time in milliseconds
    timer_expired = pyqtSignal()    # Clock hits exactly 0:00

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # QTimer UI refresh rate 
        self.qtimer = QTimer(self)
        self.qtimer.setInterval(50)  # Fire every 50ms 
        self.qtimer.timeout.connect(self._tick)
        
        # QElapsedTimer tracks the actual time passed
        self.elapsed = QElapsedTimer()
        
        # State variables
        self.remaining_ms = 0
        self.snapshot_remaining = 0
        self.is_running = False

    def set_time(self, duration_ms: int):
        # Sets the timer to a specific duration without starting it
        self.snapshot_remaining = duration_ms
        self.remaining_ms = duration_ms
        self.is_running = False
        self.time_updated.emit(self.remaining_ms)

    def start(self, duration_ms: int = None):
        # Starts the timer
        # If duration_ms is provided, resets to that duration
        if duration_ms is not None:
            self.snapshot_remaining = duration_ms
        else:
            self.snapshot_remaining = self.remaining_ms
            
        if self.snapshot_remaining <= 0:
            return

        self.is_running = True
        self.elapsed.start()
        self.qtimer.start()

    def pause(self):
        # Pauses the timer & saves the exact remaining time
        if not self.is_running:
            return
            
        self.remaining_ms = self._current_remaining()
        self.qtimer.stop()
        self.is_running = False
        self.time_updated.emit(self.remaining_ms)

    def resume(self):
        # Resumes the timer from the paused state
        if self.is_running or self.remaining_ms <= 0:
            return
        self.start()

    def _current_remaining(self) -> int:
        # Calculates the exact remaining time
        if not self.is_running:
            return self.remaining_ms
        return max(0, self.snapshot_remaining - self.elapsed.elapsed())

    def _tick(self):
        # Called every 50ms by QTimer
        # Computes time and alerts the UI
        current = self._current_remaining()
        self.remaining_ms = current
        self.time_updated.emit(self.remaining_ms)
        
        # Check if time has run out
        if current <= 0:
            self.qtimer.stop()
            self.is_running = False
            self.timer_expired.emit()