age = int(input("Введіть вік: "))

if age < 0:
    print("Помилка: вік не може бути від'ємним!")
elif age < 12:
    print("Категорія: Дитина")
elif age >= 12 and age <= 17:
    print("Категорія: Підліток")
elif age >= 18 and age <= 59:
    print("Категорія: Дорослий")
else:
    print("Категорія: Літня людина")