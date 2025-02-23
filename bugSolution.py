def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")  # Raise exception
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
try:
    my_numbers = []
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

# Example with data
try:
    my_numbers = [10,20,30,40,50]
    average = calculate_average(my_numbers)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}") 