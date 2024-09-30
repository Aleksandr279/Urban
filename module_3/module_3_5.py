def get_multiplied_digits(number_):
    str_number_ = str(number_)
    multi_number_ = []
    multi_number_.extend(str_number_)
    first_ = int(multi_number_[0])
    multi_number_.remove(multi_number_[0])
    for i in multi_number_:
        if i == '0':
            multi_number_.remove(i)
        else:
            continue
    n = len(multi_number_)
    a = 1
    if n == 0:
        return first_
    else:
        for i in multi_number_:
            a *= int(i)
        return first_ * a


result_ = get_multiplied_digits(40203)
print(result_)
