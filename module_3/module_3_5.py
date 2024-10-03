def get_multiplied_digits(number_):
    str_number_ = str(number_)
    first_ = int(str_number_[0])
    while first_ != 0 and str_number_[-1] == '0':
        str_number_ = str_number_[:-1]
    if len(str_number_) > 1:
        return first_ * get_multiplied_digits(int(str_number_[1:]))
    else:
        return first_


result_1 = get_multiplied_digits(40203)
result_2 = get_multiplied_digits(42300)
result_3 = get_multiplied_digits(4)
result_4 = get_multiplied_digits(0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)
