def send_email(message_, recipient_, sender_='university.help@gmail.com'):

    if print(recipient_.endswith('@')) and print(sender_.endswith('@')):
        print('Отправить письмо')
    if print(recipient_.endswith('.com', -4, -1)) or print(recipient_.endswith('.ru', -3, -1)) or print(recipient_.endswith('.net', -4, -1)):
        print('Отправить письмо')
    if print(sender_.endswith('.com', -4, -1)) or print(sender_.endswith('.ru', -3, -1)) or print(sender_.endswith('.net', -4, -1)):
        print('Отправить письмо')
    else:
        print(f'Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}')



send_email('a', 'b2b@mail.ru')
