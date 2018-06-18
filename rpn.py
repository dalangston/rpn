import math
from inspect import signature

operators = {
  '+':lambda x, y:x+y,
  '-':lambda x, y:x-y,
  '/':lambda x, y:x/y,
  '*':lambda x, y:x*y,
  'ac':lambda :rpn_stack.clear(),
  'c':lambda :rpn_stack.pop(),
  'q':lambda :exit(0),
  '!':lambda x:math.factorial(x),
  'sw':lambda :stack_swap(rpn_stack),
  '^':lambda x, y:math.pow(x, y),
  'sqrt':lambda x:math.sqrt(x),
  'ln':lambda x:math.log(x),
  'log':lambda x:math.log10(x),
  'pi':lambda :rpn_stack.append(math.pi)
}

rpn_stack = []

def stack_swap(stack):
  if len(stack) > 1:
    stack.append(stack.pop(-2))
  else:
    print("Nothing to swap")

def compute(oper):
  num_ops = len(signature(oper).parameters)

  if len(rpn_stack) < num_ops:
    print("Too few operands")
  
  elif num_ops == 2:
    op2 = rpn_stack.pop()
    op1 = rpn_stack.pop()
    rpn_stack.append(oper(op1, op2))
  
  elif num_ops == 1:
    op = rpn_stack.pop()
    rpn_stack.append(oper(op))
  
  elif num_ops == 0:
    oper()

def disp_stack():
  box_width = 40
  box_ends = ""
  
  for i in range(box_width):
    box_ends += "-"
  
  stack_size = len(rpn_stack)
  
  print(box_ends)
  
  if stack_size < 1:
    print()

  for i in range(stack_size):
    reg_line = "  R" + str(((stack_size -i)-1)) + ":\t" + str(rpn_stack[i])
    print(reg_line)
  print(box_ends, "\n")

while (True):
  disp_stack()
  val = input("=> ").lower()
  
  try:
    val = float(val)
    rpn_stack.append(val)
  
  except ValueError:
    if val in operators:
      compute(operators[val])
    
    else:
      print("Unknown Function:\t", val )
