
students = ["Ola",
           "Piotr",
           "Żaneta",
           "Tomek",
           "Angela",
           "Michał",
           "Igor",
           "Andrij",
           "Filip"]

student = set(students)

import random
x = random.sample(student,3)
print(x)
student = student.difference(x)
x = random.sample(student,3)
print(x)
student = student.difference(x)
x = random.sample(student,3)
print(x)

# from itertools import permutations
# for i in permutations(student, 3):
#     print(i)
#     student = student.difference(i)

