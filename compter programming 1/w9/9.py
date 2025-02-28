x = []
a = int(input())
for i in range(int(a)):
    b = input()
    x.append(int(b))

for i in range(a):
    for e in range(a):
        if x[i] < x[e]:
            d = x[i]
            x[i] = x[e]
            x[e] = d
print(x)
            
        
        
for i in range(a):
    for e in range(a):
        if x[i] > x[e]:
            d = x[i]
            x[i] = x[e]
            x[e] = d
print(x)
            
        
        

