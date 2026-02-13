import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

a = 0
b = 6

ESCALA = 1e8  # Escala para visualización

while True:
    while True:
        n = int(input('Valor de n (par y >= 2): '))
        if n % 2 == 0 and n >= 2:
            break
        print("n debe ser par y >= 2")

    # Definir función seccionada en tres tramos 
    #(tuvimos que recurrir a IA para consultar la documentación de la función seccionada)
    def f_seccionada(x_vals):
        y = np.empty_like(x_vals)
        mask_exp1 = (x_vals >= 0) & (x_vals <= 2)
        mask_lin  = (x_vals > 2) & (x_vals <= 4)
        mask_exp2 = (x_vals > 4) & (x_vals <= 6)
        y[mask_exp1] = -1.59e-8 * np.exp(-0.5 * x_vals[mask_exp1])
        y[mask_lin] = -1.59e-8 * x_vals[mask_lin]
        y[mask_exp2] = -1.59e-8 * np.exp(-0.5 * (x_vals[mask_exp2] - 4))
        return y

    # Función simbólica para integración con Piecewise
    #(tuvimos que recurrir a IA para consultar la documentación SymPy de la función seccionada)
    expr = sp.Piecewise(
        (-1.59e-8 * sp.exp(-0.5 * x), (x >= 0) & (x <= 2)),
        (-1.59e-8 * x, (x > 2) & (x <= 4)),
        (-1.59e-8 * sp.exp(-0.5 * (x - 4)), (x > 4) & (x <= 6))
    )

    f = sp.lambdify(x, expr, 'numpy')

    valor_analitico = float(sp.integrate(expr, (x, a, b)))

    # Puntos para trapecios (n+1)
    x_trap = np.linspace(a, b, n + 1)
    y_trap = f_seccionada(x_trap)
    h = (b - a) / n

    valor_numerico = np.sum((y_trap[:-1] + y_trap[1:]) * h / 2)

    print('\nINTEGRACIÓN POR TRAPECIOS')
    print('--------------------------------')
    print('Resultado analítico:', valor_analitico)
    print('Resultado numérico :', valor_numerico)

    # Gráfica función continua con buena resolución
    x_continuo = np.linspace(a, b, 600)
    y_continuo = f_seccionada(x_continuo)

    plt.figure(figsize=(12, 6))

    # Graficar función continua
    plt.plot(x_continuo, ESCALA * y_continuo, label='Función seccionada', color='magenta', linewidth=2)

    # Graficar trapecios sombreados
    for i in range(n):
        xs = [x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]]
        ys = [0, ESCALA * y_trap[i], ESCALA * y_trap[i+1], 0]
        plt.fill(xs, ys, 'orchid', alpha=0.4)


    # Líneas verticales que marcan cambios de tramo
    plt.axvline(2, color='mediumorchid', linestyle='--', linewidth=2, label='Cambio en x=2')
    plt.axvline(4, color='mediumorchid', linestyle='--', linewidth=2, label='Cambio en x=4')

    # Líneas de referencia
    plt.axhline(0, color='gray')
    plt.axvline(a, color='black', linestyle='--')
    plt.axvline(b, color='black', linestyle='--')

    plt.xlabel('x')
    plt.ylabel(r'$10^8 f(x)$')
    plt.title('Función seccionada en tres tramos y método del trapecio')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    op = int(input('\n¿Modificar n? [1-Sí / 2-No]: '))
    if op == 2:
        break

print('Fin del programa --------')

