import numpy as np
import matplotlib.pyplot as plt

# Создаем массивы x1 и x2
x1 = np.linspace(0, 40, 100)
x2 = np.linspace(0, 40, 100)

# Создаем сетку X1 и X2
X1, X2 = np.meshgrid(x1, x2)

# Задаем ограничения
constraint1 = X1 - 2 * X2 <= 30
constraint2 = 5 * X1 - X2 <= 25

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,50)
plt.ylim(-5,50)
plt.plot(x1, (x1 - 30) / 2, label='x1-2x2=30', color='red', linestyle='dashed')
plt.plot(x1, 5 * x1 - 25, label='5x1-x2=25', color='pink', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed', label='x1=0')
plt.axhline(y=0, color='gray', linestyle='dashed', label='x2=0')
plt.fill_between([0, 5, 15,0], [0, 0, 50, 50], color='lavender')
plt.arrow(0, 0, 5, 5, head_width=0.7, head_length=0.7, fc='black', ec='black', label='вектор z')
perpendicular_x = np.array([-5, 5])
perpendicular_y = np.array([5, -5])
plt.plot(perpendicular_x, perpendicular_y, linestyle='dashed', color='green', label='перпендикуляр')

plt.title('Линейная функция')
plt.grid(True)
plt.legend()
plt.show()

