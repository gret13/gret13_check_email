def check_email(email):
    emali_lower = email.lower()
    if '@yandex' and not '@yandex-team' in emali_lower:
        return emali_lower.replace('@yandex', '@ya')
    emali_lower


def main():
    email_list = ['mail_1@Yandex.ru', 'mail_2@Ya.ru', 'mail_3@Yandex.team.ru', 'mail_4@Yandex.com']
    for value in email_list:
        print(check_email(value))


if __name__ == '__main__':
    main()
