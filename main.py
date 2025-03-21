# Importando librerías
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Definiendo la función
def f(x):
    return (x - 1.5) ** 3 + 0.4


def f3(x):
    return (x - 1.5) ** 2 + 0.4


def f2(x):
    return np.sin(x)


# Creando los rectángulos
def generate_rectangles(n, x, y):
    rectangles = []
    for i in range(1, 2 * n, 2):
        rectangle = plt.Rectangle(
            (x[i - 1], 0), x[i + 1] - x[i - 1], y[i], alpha=0.5, color="blue"
        )
        rectangles.append(rectangle)

    return rectangles


# Obteniendo la suma inferior
def low_sum(n, x, y):

    rectangles = []
    # Como tomamos a conveniencia una función monótona creciente se fumple que f(x)<=f(x+1) por tanto x ínfimo del intervalo [x,x+1]
    for i in range(n):
        rectangle = plt.Rectangle(
            (x[i], 0), (x[i + 1] - x[i]), y[i], alpha=0.5, color="blue"
        )
        rectangles.append(rectangle)
    return rectangles


# obteniendo la suma superior
def upper_sum(n, x, y):
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
y1 = [f(x1), f2(x1), f3(x1)]
# Creando la figura y el eje
fig, ax = plt.subplots(3, figsize=(8, 6))
arr = [[0,f(1)], [0,f2(1)],[0,f3(1)]]
arr2 = [[0,f(2)], [0,f2(2)],[0,f3(2)]]

# Definiendo la función para la animación
def refresh_animate(i):
    for z in range(3):
        ax[z].clear()
        ax[z].set_xlim(a, b)
        ax[z].set_ylim(0, 1.1)
        ax[z].plot(x1, y1[z], color="black")
        ax[z].plot([1, 1], arr[z], linestyle="--", color="black", label="a")
        ax[z].plot([2, 2], arr[z], linestyle="--", color="black", label="b")
        if z == 0:
            rectangles = generate_rectangles(
                i, np.linspace(1, 2, 2 * i + 1), f(np.linspace(1, 2, 2 * i + 1))
            )
            supRects = upper_sum(i, np.linspace(1, 2, i + 1), f(np.linspace(1, 2, i + 1)))
            infRects = low_sum(i, np.linspace(1, 2, i + 1), f(np.linspace(1, 2, i + 1)))
        elif z==1:
            rectangles = generate_rectangles(
                i, np.linspace(1, 2, 2 * i + 1), f2(np.linspace(1, 2, 2 * i + 1))
            )
            supRects = upper_sum(i, np.linspace(1, 2, i + 1), f2(np.linspace(1, 2, i + 1)))
            infRects = low_sum(i, np.linspace(1, 2, i + 1), f2(np.linspace(1, 2, i + 1)))
        elif z ==2:
            rectangles = generate_rectangles(
                i, np.linspace(1, 2, 2 * i + 1), f3(np.linspace(1, 2, 2 * i + 1))
            )
            supRects = upper_sum(i, np.linspace(1, 2, i + 1), f3(np.linspace(1, 2, i + 1)))
            infRects = low_sum(i, np.linspace(1, 2, i + 1), f3(np.linspace(1, 2, i + 1)))
        ax[0].set_title(
            "Autoras: Ana Laura Oliva y Karen Negrín Mazario   Grupo: C111"
            + f" Azul: \u03c3(f,P,{{\u03bei}}) = Σf(\u03bei)*\u0394xi, i = 1, 2,..., n"
            + f" Azul claro: S(f,P) =ΣMi*\u0394xi  i = 1, 2,..., n;"
            + f" Azul oscuro: s(f,P)= Σmi*\u0394xi  i = 1, 2,..., n;"
            + f" con mi = inf(f(x), x \u2208[xi-1, xi]), Mi =sup(f(x), x \u2208[xi-1, xi])"
            + f" n = {i}", fontsize=7
        )

        for rectangle in rectangles:
            ax[z].add_patch(rectangle)
        for infRect in infRects:
            ax[z].add_patch(infRect)
        for supRect in supRects:
            ax[z].add_patch(supRect)


# Creando animación

ani = animation.FuncAnimation(fig, refresh_animate, frames=150, interval=100)

# Mostrando la animación
plt.tight_layout()
plt.show()
