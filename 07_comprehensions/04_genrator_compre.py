daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
# ( expression for item in iterable if condition )
# this is memory efficient as it works as a stream of data and does not store the entire list in memory where the list comprehension does
# so they need to be consumed like using sum() list() filter() etc
total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)