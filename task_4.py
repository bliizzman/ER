numb = input("Введите целое положительное число: ")
try:
    number = int(numb)
except Exception:
    print("Неверно, введите число")
else:
    if number > 0:
        while True:
            str_number = f"{number}"
            max_digit = 0
            for current_digit in str_number:
                int_current_digit = int(current_digit)
                if int_current_digit > max_digit:
                    max_digit = int_current_digit
            print(f"Наибольшая цифра: {max_digit}")
            break