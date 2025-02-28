a = int(input())
for i in range(a):
    for r in range(i):
        print("  ",end="")
    for r in range(a-i):
        print(str(r+1)+"|",end="")
    print("")
   
