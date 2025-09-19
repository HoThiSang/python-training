def design_door_mat(n, m): 
    for i in range(n//2): 
        t = (2*i) + 1
        print(('.|.'*t).center(m, '-'))

    print("WELCOME".center(m,'-'))

    for i in reversed(range(n//2)): 
        t = (2*i) + 1
        print(('.|.'*t).center(m, '-'))
    
n, m = map(int, input().split())
design_door_mat(n, m)