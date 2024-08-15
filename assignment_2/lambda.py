def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.
    
    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]


numbers = [1, 2, 3, 4, 5]

doubled = apply_operation(numbers, lambda x: x * 2)
squared = apply_operation(numbers, lambda x: x * x)
filtered_odds = apply_operation(numbers, lambda x: x if x % 2 != 0 else None)

filtered_odds = list(filter(lambda x: x is not None, filtered_odds))

# Print results
print("Doubled:", doubled)          # Output: [2, 4, 6, 8, 10]
print("Squared:", squared)          # Output: [1, 4, 9, 16, 25]
print("Filtered (odd numbers):", filtered_odds)  # Output: [1, 3, 5]
