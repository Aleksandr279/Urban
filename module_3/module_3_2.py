def send_email(message_, recipient_, sender_="university.help@gmail.com"):
    list_recipient_ = (list(recipient_))
    list_sender_ = (list(sender_))
    string_a_ = sender_[:-5:-1]
    string_b_ = recipient_[:-5:-1]
    if string_a_[-1] != '.':
        string_a_ = string_a_[:-1]
    if string_b_[-1] != '.':
        string_b_ = string_b_[:-1]
    print(list_sender_)
    print(list_recipient_)
    print(string_a_)
    print(string_b_)
    if print('@' in list_recipient_) and print('@' in list_sender_):
        for i in ['moc.', 'ur.', 'ten.']:
            if string_a_ == i:
                print('Yes')
                break
            else:
                print('No')

    # print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')
    # range(len(list_))
    # string_a_ == list_[a + 1]
    # print('Yes')
    # a += 1
    # break

    # elif print(string_a_ in list_) and print(string_b_ in list_):
    # print('Yes')
    # else:
    # print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')

    # print(sender_[:-5:-1])
    # print(recipient_[:-5:-1])


send_email('a', 'b2b@mail.ru')