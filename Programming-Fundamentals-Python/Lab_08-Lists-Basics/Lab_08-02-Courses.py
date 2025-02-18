# 2. Courses
# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

# Verzija 1 - pomocu .append()

n = int(input())
courses = []
for i in range(n):
    course = input()
    courses.append(course)
print(courses)

# Verzija 2 - pomocu .insert()

# n = int(input())
# courses = []
# for i in range(n):
#     course = input()
#     courses.insert(i,course)
# print(courses)