def send_email(message_, recipient_, *, sender_='university.help@gmail.com'):
# Проверка на корректность email получателя и отправителя
    valid_domains = ('.com', '.ru', '.net')
    if '@' not in recipient_ or not recipient_.endswith(valid_domains):
        print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')
        return
    if '@' not in sender_ or not sender_.endswith(valid_domains):
        print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')
        return
# Проверка на отправителя по умолчанию
    if sender_ == 'university.help@gmail.com'and recipient_ != sender_:
        print(f'Письмо успешно отправлено с адреса {sender_} на адрес {recipient_}.')
        return
# Проверка на отправку самому себе
    elif recipient_ == sender_:
        print(f'НЕЛЬЗЯ ОТПРАВИТЬ ПИСЬМО САМОМУ СЕБЕ.')
        return
#Проверка на отправку с нестандартного адреса
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender_} на адрес {recipient_}.')
        return


send_email('a', 'b2b_/_mail.ru')
send_email('a', 'b2b@mail.ru', sender_='university.help@gmail.<=>')
print('_______________________________________')
send_email('a', 'b2b@mail.ru')
send_email('a', 'university.help@gmail.com')
send_email('a', 'university.help@gmail.com', sender_='b2b@mail.ru')
