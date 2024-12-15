def send_email(mes, recipient, sender="university.help@gmail.com"):
    # Проверка на наличие в адресе ".com", ".net", ".ru"
    if adr(recipient, ".com", 4) == 0 and adr(recipient, ".net", 4) == 0 and adr(recipient, ".ru", 3) == 0:
        mes = "Невозможно отправить письмо с адреса " + sender + " на адрес "+ recipient
        return mes
    elif adr(sender, ".com", 4) == 0 and adr(sender, ".net", 4) == 0 and adr(sender, ".ru",3) == 0:
        mes = "Невозможно отправить письмо с адреса " + sender + " на адрес "+ recipient
        return mes
        # Проверка на наличие в адресе "@"
    elif dog(recipient) == 1:
        mes = "Невозможно отправить письмо с адреса " + sender + " на адрес "+ recipient
        return mes
    elif dog(sender) == 1:
        mes = "Невозможно отправить письмо с адреса " + sender + " на адрес "+ recipient
        return mes
    # Проверка не сам ли себе оправил
    elif recipient == sender:
        mes = "Нельзя отправить письмо самому себе!"
        return mes
    # Проверка адреса стандпртного отправителя
    elif sender != "university.help@gmail.com":
        mes = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient
        return mes
    else:
        mes ="Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient
        return mes

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

print(send_email("", "qwerty@mail.net", "university.help@gmail.com"))
print(send_email("","qwertymail.ru", "university.help@gmail.com"))
print(send_email("", "university.help@gmail.com", "university.help@gmail.com"))
print(send_email("", "qwerty@mail.net", "help@gmail.com"))
