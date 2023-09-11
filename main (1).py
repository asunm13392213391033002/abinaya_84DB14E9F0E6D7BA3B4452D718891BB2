def leapyear(num):
  if(num%4==0):
      print(num,"IS LEAP YEAR")
  else:
       print(num,"IS NOT A LEAP YEAR")
num=int(input("ENTER A YEAR:"))    
leapyear(num)