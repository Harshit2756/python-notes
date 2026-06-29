# this is a advance logger module with multiple logging levels and formatting(colors, timestamps etc can be added later)
def log_info(message):
    print(f"[INFO]: {message}" )
def log_warning(message):
    print(f"[WARNING]: {message}")
def log_error(message):
    print(f"[ERROR]: {message}")
def log_debug(message):
    print(f"[DEBUG]: {message}")
def log_critical(message):
    print(f"[CRITICAL]: {message}")