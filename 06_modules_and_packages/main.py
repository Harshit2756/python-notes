# this way imports the whole module
# import masala_chai.py
# masala_chai.brew()

# this way imports only the brew function from masala_chai module
# from masala_chai import brew
# brew()

# this way imports a function and renames it
# from masala_chai import brew as brew_masala
# brew_masala()

# this way imports all functions from masala_chai module
# from masala_chai import *

# import recipes.flavors

# print(recipes.flavors.ginger_chai())


# from recipes.flavors import elachai_chai, ginger_chai

# print(ginger_chai())



# ------------ logger package usage example ------------
# from logger_package.logger import log_info, log_warning, log_error, log_debug, log_critical
from logger_package.sub_logger import color_logg
from logger_package import logger

logger.log_info("This is an info message")
logger.log_warning("This is a warning message")
logger.log_error("This is an error message")
logger.log_debug("This is a debug message")
logger.log_critical("This is a critical message")

print("\nUsing colored logger:\n")

color_logg.log_info("This is a colored info message")
color_logg.log_warning("This is a colored warning message")
color_logg.log_error("This is a colored error message")
color_logg.log_debug("This is a colored debug message")
