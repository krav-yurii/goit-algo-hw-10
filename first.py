import pulp

# Створення проблеми лінійного програмування
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
L = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
F = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Цільова функція
model += L + F, "Total_Products"

# Обмеження
model += 2*L + 1*F <= 100, "Water_Constraint"
model += 1*L <= 50, "Sugar_Constraint"
model += 1*L <= 30, "Lemon_Juice_Constraint"
model += 2*F <= 40, "Fruit_Puree_Constraint"

# Розв'язання проблеми
model.solve()

# Виведення результатів
print(f"Статус розв'язку: {pulp.LpStatus[model.status]}")
print(f"Кількість виробленого Лимонаду: {L.varValue}")
print(f"Кількість виробленого Фруктового соку: {F.varValue}")
print(f"Максимальна загальна кількість продуктів: {pulp.value(model.objective)}")
