correct_login = "admin"
correct_password = "1234"

entered_login = input("Введіть логін: ")
entered_password = input("Введіть пароль: ")

if entered_login == correct_login and entered_password == correct_password:
    print("Вхід дозволено")
elif entered_login != correct_login:
    print("Неправильний логін")
else:
    print("Неправильний пароль")