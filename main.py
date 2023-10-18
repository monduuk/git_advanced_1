def even_list(int_list: List[int]) -> List[int]:
  """
  Determines if a number is even and return an even list.
        
  Args:        int_list: A list of integer.
        
  Returns:        A list of even integers.    
  """ 
        
  # TODO: Implement even_list    
  lst = []
  
  for i in int_list:
    if i%2 == 0:
      lst.append(i)
  
  return lst

  pass