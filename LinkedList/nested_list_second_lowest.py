# Find students with the second lowest marks and print their names in alphabetical order

stu_data=[[input(), float(input())] for i in range(int(input()))]
marks=[i[1] for i in stu_data]
unique=sorted(set(marks))
second=unique[1]
name=sorted([k[0] for k in stu_data if k[1]==second])
for j in name:
    print([j])
