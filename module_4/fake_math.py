

def divide(first, second):
    if second == 0:
        return 'Ошибка '
    else:
        return first / second


if __name__ == "__main__":
    result_1 = divide(5, 2)
    result_2 = divide(5, 0)
    result_3 = divide(-8, 2)
    print(result_1)
    print(result_2)
    print(result_3)
