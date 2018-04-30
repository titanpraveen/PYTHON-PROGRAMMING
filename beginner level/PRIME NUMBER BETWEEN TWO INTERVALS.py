x=int(input("ENTER THE FIRST NUMBER"))
y=int(input("ENTER THE SECOND NUMBER"))
s=0

for z in range(x,1+y):
  if(z==2):
    print("2")
  elif(z==3):
    print("3")
  elif(z==5):
    print("5")
  elif(z==7):
    print("7")
  
  if(z%2==0):
    s=0
  elif(z%3==0):
    s=0
  elif(z%5==0):
    s=0
  elif(z%7==0):
   s=0
  else:
    print(z)
  
