immutable_var = ('Opel', 'LADA', 125, True, 0.01)
print(immutable_var)
#immutable_var[2] = 'Mersedes'
#print(immutable_var)
# третий элемент кортежа 125 невозможно заменить на 'Mersedes", т.к. кортеж является
# неизменяемым объектом.
#
mutable_list = ['Mersedes', 'Volkswagen', 1, len, 4.5]
print(mutable_list)
mutable_list[3] = 'Opel'
mutable_list[4] = 'Mersedes'
mutable_list[0] = 4.5
print(mutable_list)
