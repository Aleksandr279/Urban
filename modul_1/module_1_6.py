my_dict = {'A': 10001, 'B': 10010, 'C': 10011, 'D': 10100, 'E': 10101}
print(my_dict)
print(my_dict['C'])
my_dict['F'] = 10110
print(my_dict)
my_dict.update({'G': 10111,
                'H': 11000})
print(my_dict)
a = my_dict.pop('C')
print("'A': ",a)
print(my_dict)
#
my_set = {1, 2, 3, 1, 2, 3, 4, True, 'algaritm', (1, 2, 3, 4)}
print(my_set)
print(my_set.add(5))
print(my_set.add(6))
print(my_set.discard(2))
print(my_set)