def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    # f.close()  # Missing file closure
    return 10

# Example usage that might cause issues:
try:
    result = function_with_unclosed_file('my_file.txt')
except Exception as e:
    print(f"An error occurred: {e}")
print(f"Result: {result}")