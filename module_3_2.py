def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ("@" not in recipient or not (
            recipient.endswith(".com") or recipient.endswith(".ru") or recipient.endswith(".net"))) or \
            ("@" not in sender or not (sender.endswith(".com") or sender.endswith(".ru") or sender.endswith(".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    if not sender == 'university.help@gmail.com':
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')





# def func_with_params(a, b=2, c=None):
    # if c is None:
        # c = []
        # c.append(a)
    # print(c)

# func_with_params(3)
# func_with_params(4)
# func_with_params(5)
# func_with_params(6)

# def print_params(a=6, b=5, c=1):
    # print (a, b, c)
    # print (b + c)
    # print (a)
    # print (b - c)

# print_params()