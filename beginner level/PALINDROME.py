a=int(input("enter a number"))
z=a
c=0
while(a>0):
  print(a)
  b=a%10
  print(b)
  c=10*c+b
  print(c)
  a=a//10  
if(z==c):
  print("yes")
else:
  print("no")

  
  
