a = int(input())
for i in range(a):
    for r in range(a-i-1):
        print("  ",end="")
    for r in range(i+1):
        print(str(r+1)+"|",end="")
    print("")
   
