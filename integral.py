import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла за допомогою методу Монте-Карло

N = 100000  # Кількість випадкових точок
points = [(random.uniform(a, b), random.uniform(0, f(b))) for _ in range(N)]

# Відбір точок, що знаходяться під кривою
under_curve_points = [point for point in points if point[1] <= f(point[0])]

# Обчислення площі
integral_monte_carlo = (len(under_curve_points) / N) * (b - a) * f(b)

# Обчислення інтеграла за допомогою функції quad
integral_quad, _ = spi.quad(f, a, b)

# Виведення результатів
print("Інтеграл методом Монте-Карло:", integral_monte_carlo)
print("Інтеграл з функції quad:", integral_quad)
