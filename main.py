# Importando librerías
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Definiendo la función
def f(x):
    return (x - 1.5) ** 3 + 0.4


# Creando los rectángulos
def generate_rectangles(n):
    x = np.linspace(1, 2, 2 * n + 1)
    y = f(x)
    rectangles = []
    for i in range(1, 2 * n, 2):
        rectangle = plt.Rectangle(
            (x[i - 1], 0), x[i + 1] - x[i - 1], y[i], alpha=0.5, color="blue"
        )
        rectangles.append(rectangle)

    return rectangles


# Obteniendo la suma inferior
def low_sum(n):
    x = np.linspace(1, 2, n + 1)
    y = f(x)
    rectangles = []
    # Como tomamos a conveniencia una función monótona creciente se fumple que f(x)<=f(x+1) por tanto x ínfimo del intervalo [x,x+1]
    for i in range(n):
        rectangle = plt.Rectangle(
            (x[i], 0), (x[i + 1] - x[i]), y[i], alpha=0.5, color="blue"
        )
        rectangles.append(rectangle)
    return rectangles


# obteniendo la suma superior
def upper_sum(n):
    x = np.linspace(1, 2, n + 1)
    y = f(x)
    rectangles = []
    for i in range(n):
        rectangle = plt.Rectangle(
            (x[i], 0), (x[i + 1] - x[i]), y[i + 1], alpha=0.5, color="blue"
        )
        rectangles.append(rectangle)
    return rectangles


# Definiendo el intervalo
a = 0
b = 3

# Creando arreglo de x para evaluar la función
x = np.linspace(1, 2, 101)
x1 = np.linspace(a, b, 303)
# Creando arreglo de y para evaluar la función
y = f(x)
y1 = f(x1)
# Creando la figura y el eje
fig, ax = plt.subplots()
# Definiendo la función para la animación
def refresh_animate(i):
    ax.clear()
    ax.set_xlim(a, b)
    ax.set_ylim(0, 1.1)
    ax.plot(x1, y1, color="black")
    ax.plot([1, 1], [0, f(1)], linestyle="--", color="black", label="a")
    ax.plot([2, 2], [0, f(2)], linestyle="--", color="black", label="b")
    rectangles = generate_rectangles(i)
    supRects = upper_sum(i)
    infRects = low_sum(i)
    ax.set_title(
        f" Azul: \u03c3(f,P,{{\u03bei}}) = Σf(\u03bei)*\u0394xi, i = 1, 2,..., n"
        + f"\nAzul claro: S(f,P) =ΣMi*\u0394xi  i = 1, 2,..., n;"
        + r"\nAzul oscuro: s(f,P)= Σmi*\u0394xi  i = 1, 2,..., n;"
        + f" con mi = inf(f(x), x \u2208[xi-1, xi]), Mi =sup(f(x), x \u2208[xi-1, xi])"
        + f"\nn = {i}"
    )
    for rectangle in rectangles:
        ax.add_patch(rectangle)
    for infRect in infRects:
        ax.add_patch(infRect)
    for supRect in supRects:
        ax.add_patch(supRect)


# Creando animación

ani = animation.FuncAnimation(fig, refresh_animate, frames=150, interval=100)

# Mostrando la animación
plt.show()
