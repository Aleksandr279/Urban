

def get_sum_values(*args):
    global sum_data_structure
    global result
    sum_data_structure = 0
    result = 0
    for i in args:
        if isinstance(i, str):
            sum_data_structure += len(i)

        elif isinstance(i, int):
            sum_data_structure += i

        elif isinstance(i, dict):
            i = [*i.items()]
            for j in i:
                for k in j:
                    if isinstance(k, str):
                        sum_data_structure += len(k)
                    elif isinstance(k, int):
                        sum_data_structure += k

        elif isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
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
get_sum_values(['abc', [[1, 2], 1, 2], (1, 2), {1: 2, 2: 1}, 3])
print(sum_data_structure)
