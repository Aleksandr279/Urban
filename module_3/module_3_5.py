def get_multiplied_digits(number_):
    str_number_ = str(number_)
    first_ = int(str_number_[0])
    if len(str_number_) == 1 and first_ == 0:
        return 0
    elif len(str_number_) > 1:
        return first_ * get_multiplied_digits(int(str_number_[1:]))
    else:
        return first_ if first_ != 0 else 1


result_ = get_multiplied_digits(40203)
print(result_)
