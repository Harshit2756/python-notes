class TeaLeaf:
    def __init__(self, tea_type):
        # Private attribute with underscore prefix
        self._tea_type = tea_type

    @property
    def tea_type(self):
        return self._tea_type

    @tea_type.setter
    def tea_type(self, new_tea_type):
        if new_tea_type in ["green", "black", "herbal"]:
            self._tea_type = new_tea_type
        else:
            raise ValueError("Invalid tea type. Choose from 'green', 'black', or 'herbal'.")
    @tea_type.deleter
    def tea_type(self):
        del self._tea_type

    @tea_type.getter
    def tea_type(self):
        return self._tea_type


# Example usage
tea = TeaLeaf("green")
print(tea.tea_type)  # Accessing the property
tea.tea_type = "black"  # Setting the property
print(tea.tea_type)
del tea.tea_type  # Deleting the property