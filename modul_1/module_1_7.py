grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
#
chislitel_0 = 0
for chislo in grades[0]:
    chislitel_0 = chislitel_0 + chislo
chislitel_1 = 0
for chislo in grades[1]:
    chislitel_1 = chislitel_1 + chislo
chislitel_2 = 0
for chislo in grades[2]:
    chislitel_2 = chislitel_2 + chislo
chislitel_3 = 0
for chislo in grades[3]:
    chislitel_3 = chislitel_3 + chislo
chislitel_4 = 0
for chislo in grades[4]:
    chislitel_4 = chislitel_4 + chislo
#
znamenatel_0 = len(grades[0])
znamenatel_1 = len(grades[1])
znamenatel_2 = len(grades[2])
znamenatel_3 = len(grades[3])
znamenatel_4 = len(grades[4])
#
grades[0] = chislitel_0 / znamenatel_0
grades[1] = chislitel_1 / znamenatel_1
grades[2] = chislitel_2 / znamenatel_2
grades[3] = chislitel_3 / znamenatel_3
grades[4] = chislitel_4 / znamenatel_4
#
print(dict(zip(students, grades)))
