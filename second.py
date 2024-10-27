import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

a = 0
b = 2

x = np.linspace(a - 0.5, b + 0.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x^2')
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Область інтегрування')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік функції f(x) = x^2 та область інтегрування')
ax.legend()
ax.grid(True)
plt.show()

N = 1000000  
x_random = np.random.uniform(a, b, N)
f_random = f(x_random)
f_mean = np.mean(f_random)
integral_mc = (b - a) * f_mean
print(f"Значення інтеграла методом Монте-Карло: {integral_mc}")

integral_quad, error = spi.quad(f, a, b)
print(f"Значення інтеграла за допомогою quad: {integral_quad}")
print(f"Абсолютна похибка quad: {error}")

y_max = f(b)
y_random = np.random.uniform(0, y_max, N)
under_curve = y_random < f(x_random)
area_estimate = (b - a) * y_max * np.sum(under_curve) / N
print(f"Оцінка інтеграла методом Монте-Карло (точки під кривою): {area_estimate}")

N_visual = 5000
x_visual = np.random.uniform(a, b, N_visual)
y_visual = np.random.uniform(0, y_max, N_visual)
under_curve_visual = y_visual < f(x_visual)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, 'r', linewidth=2, label='f(x) = x^2')
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Область інтегрування')
ax.scatter(x_visual[under_curve_visual], y_visual[under_curve_visual], color='green', s=1, label='Точки під кривою')
ax.scatter(x_visual[~under_curve_visual], y_visual[~under_curve_visual], color='blue', s=1, label='Точки над кривою')
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, y_max + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для обчислення інтеграла')
ax.legend(loc='upper left')
ax.grid(True)
plt.show()
