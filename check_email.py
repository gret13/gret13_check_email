def check_email(email):
    if '@yandex' and not '@yandex.team' in email.lower():
        return email.lower().replace('@yandex', '@ya')
    else:
        return email.lower()


def main():
    email_list = ['mail_1@Yandex.ru', 'mail_2@Ya.ru', 'mail_3@Yandex.team.ru', 'mail_4@Yandex.com']
    for value in email_list:
        print(check_email(value))


if __name__ == '__main__':
    main()
