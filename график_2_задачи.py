import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-5, 40, 100)
x2 = np.linspace(-5, 40, 100)

plt.figure(figsize=(5, 5))
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(-5,20)
plt.ylim(-5,20)

plt.plot(x1, (30 - 5*x1) / 3, label='5x+3y>=30', color='salmon', linestyle='dashed')
plt.plot(x1, x1-3, label='x-y<=3', color='pink', linestyle='dashed')
plt.plot(x1, (15 + 3 * x1) / 5, label='-3x+5y<=15', color='#DB7093', linestyle='dashed')
plt.axvline(x=0, color='gray', linestyle='dashed')
plt.axhline(y=0, color='gray', linestyle='dashed')

plt.fill_between([3.075, 4.87, 15, 3.075], [4.84, 1.874, 12, 4.84], color='lavender')

plt.arrow(0,0 ,-1,2, head_width=0.3, head_length=0.6, fc='black', ec='black', label='вектор z')
x1_green = np.linspace(-3, 3, 100)
plt.plot(x1_green, 1/2 * x1_green, linestyle='-.', color='green', label='перпендикуляр')

plt.plot(4.87,1.874,'o', c='#DB7093')
plt.text(4.87,1.874, 'max')
plt.plot(15,12,'o', c='#DB7093')
plt.text(15,12, 'min')
plt.title('Задание 2')
plt.grid(True)
plt.legend()
plt.show()


