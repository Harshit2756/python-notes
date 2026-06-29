# this a logger module with multiple logging levels properly colored on the console based on the logging level

def log_info(message):
    print(f"\033[94m[INFO]: {message}\033[0m" )  # Blue color
def log_warning(message):
    print(f"\033[93m[WARNING]: {message}\033[0m")  # Yellow color
def log_error(message):
    print(f"\033[91m[ERROR]: {message}\033[0m")  # Red color
def log_debug(message):
    print(f"\033[92m[DEBUG]: {message}\033[0m")  # Green color
def log_critical(message):
    print(f"\033[95m[CRITICAL]: {message}\033[0m")  # Magenta color
    
    
    # for more reference on ANSI escape codes for coloring text in terminal, visit: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit