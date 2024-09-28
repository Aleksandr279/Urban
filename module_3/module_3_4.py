def single_root_words_(root_word_, *other_words_):
    same_words_ = []
    for i in other_words_:
        if root_word_.lower() in i.lower() or i.lower() in root_word_.lower():
            same_words_.append(i)
    return same_words_


result_1 = single_root_words_('Domiki','DOM', 'miKkI', 'Mik', 'Omiks', 'domikiti')
result_2 = single_root_words_('123','012345', '32145', '12', '2', '123')
print(result_1)
print(result_2)
