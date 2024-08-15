# 📚 Higher-Order Functions with Lambda
Objective
Implement higher-order functions using lambda functions.

# Requirements
Define the Function

Create the apply_operation function with the following signature:

def apply_operation(numbers, operation):
    """
    Apply the given operation to each element in the list of numbers.
    
    :param numbers: List of numbers to be processed.
    :param operation: A function that defines the operation to apply to each element.
    :return: A new list with the operation applied to each element.
    """
    return [operation(number) for number in numbers]

Example input and output
input: [1, 2, 3, 4, 5] Doubled: [2, 4, 6, 8, 10] Squared: [1, 4, 9, 16, 25] Filtered (odd numbers): [1, 3, 5]
