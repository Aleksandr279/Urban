def print_params_(a = 2, b = 'строка', c = True):
    print(a, b, c)
    return [a, b, c]


print_params_()
print_params_(4)
print_params_(4, 2)
print_params_(5, c = 8)
print_params_(b = 25)
print_params_(c = [1, 2, 3])

print('____________________________')
list_ = print_params_()
print(list_)
values_list_ = ['Urban', 19, (1, 2, 3)]
print(values_list_)
values_dict_ = dict(zip(list_, values_list_))
print(values_dict_)
print_params_(*values_list_)

list_2 = ['a', 'b', 'c']
values_dict_2 = dict(zip(list_2, values_list_))
print(values_dict_2)
print_params_(**values_dict_2)

print('____________________________')
values_list_2 = [53, 'name']
print_params_(*values_list_2, 42)