
n = int(input())
student_marks = {}
for x in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input("Enter query : ")
if(query_name in student_marks):
    total = sum(student_marks[query_name])
    average = total/len(student_marks[query_name])
    print(f"{average:.2f}")
else: 
    print("Not found student")