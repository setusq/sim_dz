import pulp
import time

start = time.time()

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

#max
problem_max = pulp.LpProblem('0_max', pulp.LpMaximize)
problem_max += x - 2 * y, "Функция цели"
problem_max += 5 * x + 3 * y >= 30, "1"
problem_max += x - y <= 3, "2"
problem_max += -3 * x + 5 * y <= 15, "3"
problem_max.solve()

print("Результат для максимизации:")
for variable in problem_max.variables():
    print(variable.name, "=", variable.varValue)

print("Max:")
print(pulp.value(problem_max.objective))

# min
problem_min = pulp.LpProblem('0_min', pulp.LpMinimize)
problem_min += x - 2 * y, "Функция цели"
problem_min += 5 * x + 3 * y >= 30, "1"
problem_min += x - y <= 3, "2"
problem_min += -3 * x + 5 * y <= 15, "3"
problem_min.solve()

print("Результат для минимизации:")
for variable in problem_min.variables():
    print(variable.name, "=", variable.varValue)

print("Min:")
print(pulp.value(problem_min.objective))

stop = time.time()
print("Время :")
print(stop - start)
