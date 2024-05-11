def generate_password(n):
    result = ""  # Инициализируем пустую строку для хранения пароля
    for i in range(1, n):  # Цикл по всем числам от 1 до n-1
        for j in range(i + 1, n + 1):  # Цикл по числам от i+1 до n+1
            if n % (i + j) == 0:  # Проверяем, кратна ли сумма чисел n
                result += str(i) + str(j)  # Добавляем пару чисел к паролю
    return result

# Доп задание - "Слишком древний шифр" по модулю: "Базовые структуры данных"
for n in range(3, 21):
    password = generate_password(n)
    print(f"Пароль для числа {n}: {password}")

