calls_ = 0


def  count_calls():
    global calls_
    calls_ += 1


def string_info(string_):
    count_calls()
    n = len(string_)
    m = string_.upper()
    l = string_.lower()
    tuple_ = (n, m, l)
    print(tuple_)
    return tuple_


def  is_contains(string_, list_to_search_):
    count_calls()
    string_ = string_.lower()
    print(string_)
    a = -1
    for i in (list_to_search_):
        range(len(list_to_search_))
        list_to_search_[a + 1] = list_to_search_[a + 1].lower()
        a +=1
    print(list_to_search_)
    print(string_ in list_to_search_)


string_info('Еlephant')
string_info('Сrocodile')
is_contains('Жить ХОРОШО', ['жиТь хОрОшО', 'жить ЕЩЁ луЧше', 'неПОНИмаю'])
is_contains('ХОРОШО Жить', ['жиТь хОрОшО', 'жить ЕЩЁ луЧше', 'неПОНИмаю'])
print(f'функции вызывались {calls_} раза')
