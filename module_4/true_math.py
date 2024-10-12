from math import inf

def divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


result_1 = divide(6, 2)
result_2 = divide(6, 0)
result_3 = divide(-9, 2)
print(result_1)
print(result_2)
print(result_3)

if __name__ == '__divide__':
    divide()
