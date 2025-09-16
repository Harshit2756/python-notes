# zip function
# Iterate over several iterables in parallel, producing tuples with an item from each one.
# 1) if the  iterables are of uneven length, 3 ways to handle it:
#    a) stop when the shortest iterable is exhausted (default behavior)
#    b) strict = True, raise an ValueError if the iterables are of uneven length
#    c) fill in missing values with None

name = ["Hitesh", "Vaibhav", "Ankit", "Pratik", "Yash"]
bills = [250, 150, 200, 300, 350]
order_ids = [1, 2, 3, 4, 5]

for n, b, o in zip(name, bills, order_ids):
    print(f"Hello {n}, your order id is {o} and your bill amount is {b}.")
