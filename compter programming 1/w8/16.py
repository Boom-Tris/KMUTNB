a = int(input())
b = True
for i in range(2,a):
    if(a%i==0):
        print("No prime number")
        b = False
        break
if b:
    print("prime number")
    
