def arithmetic_arranger(problems, show_answers=False):
  ################################################################
  #          Check if the numbers and operations are valid       #
  ################################################################
  if len(problems)> 5:
    return 'Error: Too many problems.'

  problems_separated = []
  for problem in problems:
    item = problem.split()
    if len(item[0])<=4:
      for char in item[0]:
        if char.isalpha():
          return 'Error: Numbers must only contain digits.'
      else:
        first_num = item[0]
    else:
      return 'Error: Numbers cannot be more than four digits.'
    
    if item[1] in ['+','-']:
      operator = item[1]
    else:
      return "Error: Operator must be '+' or '-'."
    
    if len(item[2])<=4:
      for char in item[2]:
        if char.isalpha():
          return 'Error: Numbers must only contain digits.'
      else:
        second_num = item[2]
        
    else:
      return 'Error: Numbers cannot be more than four digits.'
    
    longest_operand_size = max(len(item[0]),len(item[2])) + 2     
    problems_separated.append([first_num, operator, second_num, longest_operand_size])
    
  ################################################################
  #                                                              #
  ################################################################
  
  first_elements = ''
  second_elements = ''
  dashes = ''
  answers = ''
  
  for problem in problems_separated:
    f_element = problem[0]
    operat =    problem[1]
    s_element = problem[2]
    prob_size = problem[3]
    
    # Formating and concatenating the elements
    first_elements += ''.join((' ' * (prob_size-len(f_element)) ) + f_element + '    ')
    second_elements += ''.join((operat + (' ' * (prob_size-(len(s_element)+1))) + s_element + '    '))
    dashes += ''.join(('-' * prob_size )+ '    ')
    
    if show_answers:
      if operat == '+':
        ans = int(f_element) + int(s_element)
      else:
        ans = int(f_element) - int(s_element)
      answers+= ''.join((' ' * (prob_size-len(str(ans)))) + str(ans) + '    ')
  if show_answers:    
    return first_elements[:-4] + '\n' + second_elements[:-4] + '\n' + dashes[:-4] + '\n' + answers[:-4]
  else:
    return first_elements[:-4] + '\n' + second_elements[:-4] + '\n' + dashes[:-4]
  
print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
