# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]


a = {1: 2, 2: 1}
print(a, type(a))
a = [*a.items()]
print(a, type(a))

