# neologger/core/Base.py

class FontColour:
    """ANSI escape sequences for font colors."""
    BLUE = "\033[94m"         # Light blue text
    DARKBLUE = "\033[34m"     # Dark blue text
    CYAN = "\033[96m"         # Light cyan text
    DARKCYAN = "\033[36m"     # Dark cyan text
    GREEN = "\033[92m"        # Light green text
    DARKGREEN = "\033[32m"    # Dark green text
    YELLOW = "\033[93m"       # Light yellow text
    DARKYELLOW = "\033[33m"   # Dark yellow text
    RED = "\033[91m"          # Light red text
    DARKRED = "\033[31m"      # Dark red text
    MAGENTA = "\033[95m"      # Light magenta text
    DARKMAGENTA = "\033[35m"  # Dark magenta text
    GREY = "\033[37m"         # Light grey text
    DARKGREY = "\033[90m"     # Dark grey text
    BLACK = "\033[30m"        # Black text
    WHITE = "\033[97m"        # White text
    ENDC = "\033[0m"          # Reset to default text color

class BackgroundColour:
    """ANSI escape sequences for background colors."""
    BLUE = "\033[104m"         # Light blue background
    DARKBLUE = "\033[44m"      # Dark blue background
    CYAN = "\033[106m"         # Light cyan background
    DARKCYAN = "\033[46m"      # Dark cyan background
    GREEN = "\033[102m"        # Light green background
    DARKGREEN = "\033[42m"     # Dark green background
    YELLOW = "\033[103m"       # Light yellow background
    DARKYELLOW = "\033[43m"    # Dark yellow background
    RED = "\033[101m"          # Light red background
    DARKRED = "\033[41m"       # Dark red background
    MAGENTA = "\033[105m"      # Light magenta background
    DARKMAGENTA = "\033[45m"   # Dark magenta background
    GREY = "\033[47m"          # Light grey background
    DARKGREY = "\033[100m"     # Bright black background (appears as dark grey)
    BLACK = "\033[40m"         # Black background
    WHITE = "\033[107m"        # White background
    ENDC = "\033[0m"           # Reset to default background color

class FontStyle:
    """ANSI escape sequences for font styles."""
    BOLD = "\033[1m"            # Bold text
    ITALIC = "\033[3m"          # Italic text
    UNDERLINE = "\033[4m"       # Underlined text
    DOUBLEUNDERLINE = "\033[21m"  # Double underlined text
    DIM = "\033[2m"             # Dim text
    NORMAL = "\033[22m"         # Normal intensity text
    ENDC = "\033[0m"            # Reset to default text style

class Icon:
    """Unicode characters for icons."""
    MONITOR = "\U0001F5A5"     # Desktop computer icon
    DONE = "\U00002705"        # Check mark icon
    READY = "\U00002728"       # Sparkles icon
    LOCK = "\U0001F510"        # Lock with key icon
    KEY = "\U0001F511"         # Key icon
    USER = "\U0001F464"        # User silhouette icon
    ERROR = "\U000026D4"       # No entry icon
    SURPRISE = "\U00002049"    # Exclamation question mark icon
    BULLSEYE = "\U0001F3AF"    # Bullseye icon
    STOP = "\U0000270B"        # Raised hand icon
    CONFIRM = "\U00002754"     # Question mark icon
    CANCEL = "\U0001F536"      # Large red circle icon
    LOGOUT = "\U0001F463"      # Footprints icon
    CATALOGS = "\U00002699"    # Gear icon
    WARNING = "\U000026A0"     # Warning sign icon
    STAR = "\U0001F31F"        # Glowing star icon

class Template:
    """Predefined templates for styling."""
    NORMAL = "NORMAL"          # Normal template
    DARK = "DARK"              # Dark template
    BASE = "BASE"              # Base template