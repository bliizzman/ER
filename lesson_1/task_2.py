import datetime
my_var = input("Введите секунды: ")
try:
    my_int_var = int(my_var)
    print(f"Ваше время:{datetime.timedelta(seconds=my_int_var)}")
except Exception:
    print("Неверный ввод. Введите число")
