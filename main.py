import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Определение функции f(x, y)
def f(x, y):
    return x**2 + y**2

# Частные производные функции
def df_dx(x, y):
    return 2 * x

def df_dy(x, y):
    return 2 * y

# Точка касания
x0, y0 = 1, 2
z0 = f(x0, y0)

N = 20

# Функции для построения касательных линий
def tangent_x_line(x0, y0):
    slope = df_dx(x0, y0)
    x_vals = np.linspace(-3, 3, N)
    y_vals_tangent = np.full_like(x_vals, y0)
    z_vals_tangent = z0 + slope * (x_vals - x0)
    return x_vals, y_vals_tangent, z_vals_tangent

def tangent_y_line(x0, y0):
    slope = df_dy(x0, y0)
    y_vals = np.linspace(-3, 3, N)
    x_vals_tangent = np.full_like(y_vals, x0)
    z_vals_tangent = z0 + slope * (y_vals - y0)
    return x_vals_tangent, y_vals, z_vals_tangent

# Функция для касательной плоскости
def tangent_plane(x0, y0):
    slope_x = df_dx(x0, y0)
    slope_y = df_dy(x0, y0)
    
    x_plane = np.linspace(x0 - 1, x0 + 1, N)
    y_plane = np.linspace(y0 - 1, y0 + 1, N)
    Xp, Yp = np.meshgrid(x_plane, y_plane)
    
    Zp = z0 + slope_x * (Xp - x0) + slope_y * (Yp - y0)
    return Xp, Yp, Zp

# Создаём сетку для поверхности
x_vals_2d = np.linspace(-3, 3, N)
y_vals_2d = np.linspace(-3, 3, N)
X, Y = np.meshgrid(x_vals_2d, y_vals_2d)
Z = f(X, Y)

# Создаём фигуру
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Функция обновления анимации
def update(frame):
    ax.view_init(elev=30, azim=frame)  # Меняем угол обзора
    return ax,

# Отрисовка поверхности
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

# Касательные линии
ax.plot(*tangent_x_line(x0, y0), color='r', linewidth=2, label='Касательная по X')
ax.plot(*tangent_y_line(x0, y0), color='b', linewidth=2, label='Касательная по Y')

# Касательная плоскость
Xp, Yp, Zp = tangent_plane(x0, y0)
ax.plot_surface(Xp, Yp, Zp, color='orange', alpha=0.5)

# Точка касания
ax.scatter(x0, y0, z0, color='green', s=100, label='Точка касания')

# Анимация вращения
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 3), interval=500)

# Сохранение в GIF
ani.save("graph.gif", writer="pillow", fps=15)

plt.show()
