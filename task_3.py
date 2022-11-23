my_var = input("Введите число: ")
try:
    my_int_var = int(my_var)
    double_int_var = int(f"{my_int_var}{my_int_var}")
    triple_int_var = int(f"{my_int_var}{my_int_var}{my_int_var}")
    print(my_int_var, double_int_var, triple_int_var)
    print(f"{my_int_var + double_int_var + triple_int_var}")
except Exception:
    print("Неверный ввод. Введите число")
