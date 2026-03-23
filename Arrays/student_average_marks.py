# Calculate and print the average marks of a queried student from a dictionary of student records

n = int(input())
student_marks = {}
for _ in range(n):
      name, *line = input().split()
      scores = list(map(float, line))
      student_marks[name] = scores
query_name = input()

marks= student_marks[query_name]
avg= sum(marks)/len(marks)
print(f"{avg:.2f}")
        
