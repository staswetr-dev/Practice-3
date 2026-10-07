num1 = int(input("Перше число: "))
num2 = int(input("Друге число: "))
num3 = int(input("Третє число: "))

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3

print("Найбільше число:", max_num)

count_max = 0
if num1 == max_num:
    count_max = count_max + 1
if num2 == max_num:
    count_max = count_max + 1
if num3 == max_num:
    count_max = count_max + 1

if count_max == 3:
    print("Усі три числа однакові")
elif count_max == 2:
    print("Є два однакові найбільші числа")