student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(round(sum(student_heights) / len(student_heights)))

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
h_score = 0
for s in student_scores:
    if s > h_score:
        h_score = s

print(h_score)

e = 0

for n in range(2, 101, 2):
    e += n

print(e)

# Other way
for n in range(1, 101):
    if n % 2 == 0:
        e += n

print(e)