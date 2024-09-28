def get_multiplied_digits(number_):
    str_number_ = str(number_)
    multi_number_ = []
    multi_number_.extend(str_number_)
    first_ = int(multi_number_[0])
    multi_number_.remove(multi_number_[0])
    a = 1
    b = len(multi_number_)
    for i in multi_number_:
        if int(i) == 0:
            continue
        a *= int(i)
    return first_ * a


result_ = get_multiplied_digits(40203)
print(result_)
