a=int(input("ENTER A NUMBER"))
print(a)
b=0
if(a==0):
  print("no")
for j in range(2,a//2):
  if((a%j)==0):
      b=1
      break
if(b==0):
  print("yes")
else:
  print("no")
    
    
  
