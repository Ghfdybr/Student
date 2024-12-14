def send_email(recipient, sender):
    # Проверка на наличие в адресе ".com", ".net", ".ru"
    if adr(recipient, ".com", 4) == 0 and adr(recipient, ".net", 4) == 0 and adr(recipient, ".ru", 3) == 0:
        return 1
    elif adr(sender, ".com", 4) == 0 and adr(sender, ".net", 4) == 0 and adr(sender, ".ru",3) == 0:
        return 1
    # Проверка на наличие в адресе "@"
    elif dog(recipient) == 1:
        return 1
    elif dog(sender) == 1:
        return 1
    # Проверка не сам ли себе оправил
    elif recipient == sender:
        return 2
    # Проверка адреса стандпртного отправителя
    elif sender != "university.help@gmail.com":
        return 0
    else:
        return 3

# функция проверяет знак @ в адресе
def dog(a):
    i = 0
    for i in range(len(a)):
        if a[i] == "@":
            return 0
        else: i += 1
    return 1

# функция проверяет, совпадает ли адрес отправителя с адресом отправляемого
def adr(a, c, d):
    if a[len(a)-d:len(a)] == c:
        return 0
    else: return 1



def main_f(recipient, sender):
    if send_email(recipient, sender) == 1:
        print("Невозможно отправить письмо с адреса ",  sender, " на адрес ", recipient)
    elif send_email(recipient, sender) == 2:
        print("Нельзя отправить письмо самому себе! ")
    elif send_email(recipient, sender) == 3:
        print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)
    else:
        send_email(recipient, sender) == 0
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ", sender, " на адрес ", recipient)



main_f("qwerty@mail.net", "university.help@gmail.com")
main_f("qwertymail.ru", "university.help@gmail.com")
main_f("university.help@gmail.com", "university.help@gmail.com")
main_f("qwerty@mail.net", "help@gmail.com")
