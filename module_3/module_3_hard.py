data_structure = [
                [1, 2, 3],
                {'a': 4, 'b': 5},
                (6, {'cube': 7, 'drum': 8}),
                "Hello",
                ((), [{(2, 'Urban', ('Urban2', 35))}])
                ]


def get_sum_values(*args):
    global sum_data_structure
    global list_
    sum_data_structure = 0
    list_ = []
    for i in args:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, dict):
                    list_.extend([*j.items()])
                elif isinstance(j, str) or isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, list) or isinstance(j, tuple) or isinstance(j, set):
                    for k in j:
                        if isinstance(k, dict):
                            list_.extend([*k.items()])
                        elif isinstance(k, str) or isinstance(k, int) or isinstance(k, tuple) or isinstance(k, set):
                            list_.append(k)
                        elif isinstance(k, list):
                            list_.extend(k)
    for i in list_:
        if isinstance(i, str):
            sum_data_structure += len(i)
        elif isinstance(i, int):
            sum_data_structure += i
        else:
            for j in i:
                if isinstance(j, str):
                    sum_data_structure += len(j)
                elif isinstance(j, int):
                    sum_data_structure += j
                else:
                    for k in j:
                        if isinstance(k, str):
                            sum_data_structure += len(k)
                        elif isinstance(k, int):
                            sum_data_structure += k
                        else:
                            for l in k:
                                if isinstance(l, str):
                                    sum_data_structure += len(l)
                                elif isinstance(l, int):
                                    sum_data_structure += l
    return sum_data_structure


get_sum_values(data_structure)
print(sum_data_structure)
