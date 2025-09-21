n = int(input("Enter : "))

for i in range(1,n+1): 
    left = [f"{j}" for j in range(1, i+1)]
    right = [f"{j}" for j in range(i-1, 0 ,-1)]

    print("".join(left+right))