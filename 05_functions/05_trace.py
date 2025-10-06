# Example of using the trace module programmatically
# Python's built-in trace module allows for tracking the execution of Python statements.
import trace
def my_function():
    print("Inside my_function")
    return 1 + 2
tracer = trace.Trace(count=True, trace=True)
tracer.run('my_function()')
results = tracer.results()
results.write_results(show_missing=True, summary=True, coverdir="coverage_report")

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100,150,200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")


