import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 40, 100)
x2 = np.linspace(-5, 40, 100)

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,15)
plt.ylim(-5,15)

plt.plot(x1, (21 - 2*x1) / 3, label='2X1+3X2<=21', color='salmon', linestyle='dashed')
plt.plot(x1, 10 - x1, label='X1+X2<=10', color='pink', linestyle='dashed')
plt.plot(x1, (16 - 2 * x1) / 2, label='2X1+2X2<=16', color='#DB7093', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.fill_between([0, 0, 3,8], [0, 7, 5, 0], color='lavender')

plt.arrow(0,0,  2.7,  2, head_width=0.4, head_length=0.8, fc='black', ec='black', label='вектор z')
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, -3/4 * x1_green, linestyle='-.', color='green', label='перпендикуляр')

plt.plot(8,0,'o', c='#DB7093')
plt.text(8,-1, 'max (8,0)')
plt.title('Задание 1')
plt.grid(True)
plt.legend()
plt.show()

#решение с помощью библиотеки pulp
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
#print (value(problem.objective))
stop = time.time()
print ("Время :")
print(stop- start)

