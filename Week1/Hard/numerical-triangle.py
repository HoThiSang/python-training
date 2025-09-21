n = int(input())

if(n<=0): exit() 
else: 
    for x in range(1, n): 
        for y in range(x): 
            print(x, end="")
        print()