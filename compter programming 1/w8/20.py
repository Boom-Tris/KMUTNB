a = int(input())
b = int(input())
c = int(input())
d = int(input())

mn = a
if a<b and a<c and a<d:
    mn = a
if b<a and b<c and b<d:
    mn =b
if c<a and c<b and c<d:
    mn = c
if d<a and d<b and d<c:
    mn = d
for i in range(mn,0,-1):
    if(a% i == 0) and (b% i == 0) and (c% i == 0)  and (d% i) == 0:
        print(i)
        break
    
