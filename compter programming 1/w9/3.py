x = []
a = int(input())
for i in range(int(a)):
    b = input()
    x.append(int(b))
print(sum(x)/len(x))
x.sort()
d = int((len(x)-1)/2)
print(x[d])


