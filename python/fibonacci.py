def fibonacci(n):
  num1 = 0
  num2 = 1
  sum = 0

  if n < 1 : 
    return 1

  i=0
  for i in range(0,n) :
    sum = num1 + num2
    num1 = num2
    num2 = sum 
    i+1
   

  return num1    


