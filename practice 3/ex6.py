print("=== КВЕСТ ===")
print("Перед вами двоє дверей.")
print("1 — Червоні двері")
print("2 — Сині двері")

door_choice = input("Ваш вибір: ")

if door_choice == "1":
    print("Перед вами монстр!")
    print("1 — Битися")
    print("2 — Втекти")

    monster_choice = input("Ваш вибір: ")

    if monster_choice == "1":
        strength = int(input("Введіть силу персонажа: "))
        if strength >= 50:
            print("Ви перемогли монстра!")
        else:
            print("Монстр виявився сильнішим. Ви програли.")
    elif monster_choice == "2":
        print("Ви успішно втекли")
    else:
        print("Неправильний вибір")

elif door_choice == "2":
    print("Ви знайшли скриню!")
    print("1 — Відкрити")
    print("2 — Не чіпати")

    chest_choice = input("Ваш вибір: ")

    if chest_choice == "1":
        print("Ви знайшли 100 золотих!")
    elif chest_choice == "2":
        print("Ви вирішили не ризикувати.")
    else:
        print("Неправильний вибір")

else:
    print("Неправильний вибір дверей")