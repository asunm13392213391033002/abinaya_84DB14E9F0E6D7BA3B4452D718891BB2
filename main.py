def factorial (n):
  if n==1 or n==1:
    return(1)
  else:
    return n*factorial(n-1)
num=int(input("enter a number:"))
fact=factorial(num)
print("THE FACTORIAL OF",num,"IS",fact)