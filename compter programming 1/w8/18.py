a = int(input())
for i in range(1,a+1,1):
    for d in range(a-i):
        print("  ",end="" )
    for d in range (i):
        print(str(d+1)+"|",end="")
    for d in range(i-1):
        print(str(i-d-1)+"|",end="")
    print("")
