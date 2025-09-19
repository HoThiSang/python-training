def solve(s):
    newStr = ""
    temp = s.split(" ")
    for i in temp: 
        if i.isdigit():
            newStr += i + " "
        else: 
            newStr += i.capitalize() + " "
    return newStr
                       
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)