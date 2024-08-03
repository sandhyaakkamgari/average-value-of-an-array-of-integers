def calculate_average(arr):
  """
  Calculates the average value of an array of integers.

  Args:
    arr: The array of integers.

  Returns:
    The average value of the array.
  """
  if not arr:
    return 0  # Handle empty array case
  return sum(arr) / len(arr)

# Example usage:
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average is:", average)