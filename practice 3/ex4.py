total_amount = float(input("Сума покупки: "))

if total_amount < 0:
    print("Сума не може бути від'ємною")
else:
    if total_amount < 1000:
        discount_percent = 0
    elif total_amount >= 1000 and total_amount < 3000:
        discount_percent = 5
    elif total_amount >= 3000 and total_amount < 5000:
        discount_percent = 10
    else:
        discount_percent = 15

    discount_amount = total_amount * discount_percent / 100
    final_amount = total_amount - discount_amount

    print("Сума покупки:", total_amount, "грн")
    print("Знижка:", discount_percent, "%")
    print("Сума знижки:", discount_amount, "грн")
    print("До сплати:", final_amount, "грн")