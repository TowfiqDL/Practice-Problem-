##Fibonacci Number 
##Fibonacci Series F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) 

def fibonacci(n): 
  ##base Case
  if n == 0:
    return 0 
  ##base case 
  if n == 1: 
    return 1 
  
  return fibonacci(n-1) + fibonacci(n-2) 

##Sum of non negative integer upto n
def sumAll(n): 
  ##base case 
  if n == 0: 
    return 0 
  
  return n + sumAll(n-1) 

##Calculate The GCF 
def GCF(x, y): 
  ## x < y 
  
  if x == 0: 
    return y 
  
  return GCF(y%x, x)
