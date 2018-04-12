a=int(input("PRINT NUMBER A"))
b=int(input("PRINT NUMBER B"))
c=a

if(a%2==0):
 for i in range(a+2,b,2):
  print(i)
  
if(a%2!=0):
 for i in range(a,b):
   c=c+1
   if(c%2==0):
    print(c)
   else:
    print("")
    
