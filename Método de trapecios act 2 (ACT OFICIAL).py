import numpy as np
import matplotlib.pyplot as plt
import sympy

x = sympy.symbols('x')

# Funcion f(x)
expr = (x**3)/(1+sympy.sqrt(x)) # CAMBIAAR!!

# Funcion que calcula valores de la funcion
f = sympy.lambdify(x, expr, 'numpy')

# Limites
a = float(input('Limite inferior (a): ')) # Cambiar!
b = float(input('Limite superior (b): ')) # cambiar!

while True:
    while True:
        n = int(input('Valor de n: '))
        if n%2==0: # Debe ser impar
            break
    # Resultado analitico para comparacion
    valor_analitico = float(sympy.integrate(expr, (x, a, b)))

    x_trap = np.linspace(a, b, n + 1)
    y_trap = f(x_trap)
    h = (b - a) / n # Calculo de h

    valor_numerico = 0 # Inicializa la suma

    for i in range(n):
        # Fromula del trapecio
        area_trapecio = (y_trap[i] + y_trap[i+1]) * h / 2
        valor_numerico += area_trapecio
    
    print('\nINTEGRACION POR TRAPECIOS:')
    print('---------------------------------------------------')
    print('Resultado analitico: ', valor_analitico)
    print('Resultado numerico: ', valor_numerico)

    # Grafica
    x_rango = np.linspace(a - 1, b + 1, 100) 
    plt.figure(figsize=(10, 5))

    plt.plot(x_rango, f(x_rango), label='f(x)', color='cornflowerblue')

    plt.fill_between(x_trap, y_trap, color='thistle', alpha=0.4, label='Trapecios')

    for i in range(len(x_trap)):
        plt.vlines(x_trap[i], 0, y_trap[i], color='orchid', linestyle='--')

    plt.axvline(a, color='darkmagenta', linestyle='-', label=f'a={a}')
    plt.axvline(b, color='darkmagenta', linestyle='-', label=f'b={b}')

    plt.title('Método de Trapecios - Evidencia 2')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.show()
    
    op = int(input('\nQuiere modificar el valor de n? [1-Si/2-No] '))
    if op==2:
        break
    
print('Fin del programa --------')

# Hecho por Abby Ramírez López, Rachel Morera Fajardo y María José Sosa Rivero
