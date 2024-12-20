def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... some code that might raise an exception ...
            f.write("This is a test")
            return 10
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
result = function_with_closed_file('my_file.txt')
print(f"Result: {result}")

# Verify that the file has been closed
# if you have file descriptors or similar monitoring tools available.