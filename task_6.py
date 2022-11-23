firstday_km = input("Введите расстояние за первый день: ")
desired_km = input("Введите желаемое расстояние: ")
try:
    int_firstday = int(firstday_km)
    int_desired = int(desired_km)
except Exception:
    print("Ошибка, введено не число")
else:
    counter_km = int_firstday
    counter_day = 1
    while counter_km <= int_desired:
        addkm_perday = counter_km * 10 / 100
        counter_km = addkm_perday + counter_km
        counter_day = counter_day + 1
    print(f"на {counter_day} день спортсмен достиг результата — не менее {int_desired} км")
