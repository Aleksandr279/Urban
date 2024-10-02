def get_multiplied_digits(number_):
    str_number_ = str(number_)
    first_ = int(str_number_[0])
    str_number_ = str_number_.replace("0", "1")
    n = len(str_number_)
    a = 1
    if n != 0:
        for i in str_number_[1:]:
            a *= int(i)
        return first_ * get_multiplied_digits(int(str_number_[1:]))

    else:
        return first_
    

result_ = get_multiplied_digits(40203)
print(result_)

