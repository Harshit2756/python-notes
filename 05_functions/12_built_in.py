# Built-in functions 
#
def chai_flavor(flavor="masala"):
    # __doc__ string is below the function definition
    """Return the flavor of chai."""

    chai="ginger"
    return flavor

# dunder = "__"  # double underscore
# __doc__ = "This is a module to demonstrate built-in functions"
# __name__ = "built_in" name of it
# __module__ = "05_functions.12_built_in"  # path of the module
# __package__ = "05_functions"  # parent module


print(chai_flavor.__doc__)
print(chai_flavor.__module__)
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    : return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

generate_bill(2, 3)