# Character	Meaning
# 'r'	open for reading (default)
# 'w'	open for writing, truncating the file first
# 'x'	create a new file and open it for writing
# 'a'	open for writing, appending to the end of the file if it exists
# 'b'	binary mode
# 't'	text mode (default)
# '+'	open a disk file for updating (reading and writing)
# 'U'	universal newline mode (deprecated)


# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

# The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers.
with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")
#  __enter__() dunder method is called at the beginning of the block and the __exit__() dunder method is called at the end of the block.

