a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())

for i in range(1,(a1*a2*a3*a4)+1):
    if(i%a1==0)and (i%a2==0)and (i%a3==0)and (i%a4)==0:
        print(i)
        break
