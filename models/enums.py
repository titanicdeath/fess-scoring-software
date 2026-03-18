from enum import Enum, auto

class BoutMode(Enum):
    CONVENTIONAL = "conventional"
    AUTO_PRACTICE = "auto_practice"
    POINT_TRACKER = "point_tracker"
    CUSTOM = "custom"

class BoutState(Enum):
    # Core state machine for bout flow
    IDLE = auto()               # No bout loaded
    READY = auto()              # Bout loaded, waiting for Allez (Start)
    RUNNING = auto()            # Timer counting down, touches active
    PAUSED = auto()             # Manual pause by Director
    TOUCH_DETECTED = auto()     # FRIMB sent R/G, timer auto-stopped
    AWAITING_DECISION = auto()  # Director deciding to award point or not
    PERIOD_END = auto()         # Clock hit 0:00
    REST_PERIOD = auto()        # 1-minute break between periods
    BOUT_COMPLETE = auto()      # Score limit reached or final period ended

class FencerSide(Enum):
    LEFT = "left"    # Traditionally Red
    RIGHT = "right"  # Traditionally Green

class InputAction(Enum):
    # Abstract actions that hardware inputs map to
    START_TIMER = "START_TIMER"
    PAUSE_TIMER = "PAUSE_TIMER"
    AWARD_POINT_LEFT = "AWARD_POINT_LEFT"
    AWARD_POINT_RIGHT = "AWARD_POINT_RIGHT"
    UNDO = "UNDO"
    DELAY_RESTART = "DELAY_RESTART"
    END_SESSION = "END_SESSION"
    
    # Menu Navigation
    NAVIGATE_UP = "NAVIGATE_UP"
    NAVIGATE_DOWN = "NAVIGATE_DOWN"
    NAVIGATE_LEFT = "NAVIGATE_LEFT"
    NAVIGATE_RIGHT = "NAVIGATE_RIGHT"
    SELECT = "SELECT"
    BACK = "BACK"
    
    # Hardware Signals
    FRIMB_RED = "FRIMB_RED"
    FRIMB_GREEN = "FRIMB_GREEN"