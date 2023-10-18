from typing import List
# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
  """
  Computes the sum of the squares of all even numbers in a list of integers.
  
  Args:        even_int_list: A list of even integers.
  
  Returns:        The sum of the squares of all even numbers in the list.
  """    
  # TODO: Implement sum_of_squares_of_even    
  result = 0
  
  for i in even_int_list:
    sq = i**2
    result += sq
  
  return result
  pass