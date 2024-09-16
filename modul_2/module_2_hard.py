import random

numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chislo_ = random.randint(3, 20)
print(chislo_)
parol_ = []

for i in range(len(numbers_)):
    if numbers_[i] == chislo_:
        break
    for j in range(len(numbers_)):
        a = numbers_[i] + numbers_[j]
        if a > chislo_:
            break
        elif numbers_[i] >= numbers_[j]:
            continue
        elif chislo_ % a == 0:
            parol_.extend([numbers_[i], numbers_[j]])
print(*parol_)
