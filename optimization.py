import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість Лимонаду
B = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')  # Кількість Фруктового соку

# Функція цілі (Максимізація виробництва)
model += A + B, "Total Production"

# Додавання обмежень
model += 2 * A + 1 * B <= 100  # Обмеження для Води
model += 1 * A <= 50  # Обмеження для Цукру
model += 1 * A <= 30  # Обмеження для Лимонного соку
model += 2 * B <= 40  # Обмеження для Фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти Лимонаду:", A.varValue)
print("Виробляти Фруктового соку:", B.varValue)