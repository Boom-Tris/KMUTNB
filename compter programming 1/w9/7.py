x = 0
d = 0
while(True):
   r = input()
   b = r.split(" ")
   if(b[0]=='-1'):
       break
   x = x+int(b[1])
   d = d+1
print(x/d)

   
