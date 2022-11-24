revenue = input("Введите полученую выручку: ")
costs = input("Введите понесенные издержки: ")
try:
    int_revenue = int(revenue)
    int_costs = int(costs)
except Exception:
    print("Неверные данные. Введите числа")
else:
    if int_revenue > int_costs:
        print("Прибыль")
        print(f"Рентабельность: {int_revenue / int_costs}")
        empl = input("Введите число сотрудников: ")
        try:
            int_empl = int(empl)
        except Exception:
            print("Введено не число")
        else:
            pribil = int_revenue - int_costs
            print(f"Прибыль в рассчете на одного сотрудника: {pribil / int_empl}")
    else:
        print("Убыток")


