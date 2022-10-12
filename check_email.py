def check_email(email):
    email_lower = email.lower()
    if '@yandex' and not '@yandex-team' in email_lower:
        email_lower.replace('@yandex', '@ya')
    return email_lower


assert check_email('m1@Yandex.ru') == 
'm1@ya.ru'
assert check_email('m1@Yandex-team.ru') == 
'm1@yandex-team.ru.ru'
