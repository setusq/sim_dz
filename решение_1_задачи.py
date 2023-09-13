import pulp
import time
start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += 400*x1 + 300*x2, "Функция цели"
problem += 2*x1+ 3*x2 <= 21, "1"
problem +=x1+x2<=10, "2"
problem +=2*x1+2*x2<=16, "3"
problem.solve()
print ("Результат:")
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
print ("Прибыль:")
print(pulp.value(problem.objective))
stop = time.time()
print ("Время :")
print(stop- start)
