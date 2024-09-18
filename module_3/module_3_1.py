calls_ = 0


def  count_calls():
    global calls_
    calls_ += 1


def string_info():
    count_calls()
    l = input('Введите любой текст: ')
    n = len(l)
    m = l.upper()
    s = l.lower()
    string_ = (n, m, s)
    print(string_)


def  is_contains():
    count_calls()
    l = input('Введите любой текст ещё раз: ')
    l = l.lower()
    list_to_search_ = ['жить хорошо', 'хорошо жить ещё лучше', 'ничего не понимаю']
    m = l in list_to_search_
    string_ = (l, list_to_search_)
    print(m)
    print(string_)


print(string_info())
print(is_contains())
print(f'функции вызывались {calls_} раз')
