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
            a = 0
            if string_a_ != i:
                a += 1
                break
            print('a = ', a)
            if a < 3:
                print('Отправить письмо')
            else:
                print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')



send_email('a', 'b2b@mail.ru')
