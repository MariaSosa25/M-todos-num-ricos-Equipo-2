import matplotlib.pyplot as plt
import sympy
import numpy as np


# Se define el simbolo x para tarbajar con sympy
x= sympy.symbols('x')
funcion= sympy.exp(-x**2) # Cambiar funcion aqui

# Derivada analitica
d_analitica= sympy.diff(funcion, x) # Se saca el valor con sympy

# Crea una funcion para calcular f(x) usando numpy
f = sympy.lambdify(x, funcion, 'numpy')

# Calcula la derivada con respecto al valor de x
derivada_a = sympy.lambdify(x, d_analitica, 'numpy')

# Establecer limites aqui!!! Asegurarse de que son float
xinf = float(input('Limite inferior: '))
xsup = float(input('Limite superior: '))
x0 = float(input('En que punto quieres evaluar la derivada x0: '))
h = float(input('Valor de h: '))

# El valor analitico sera valor_comp
valor_comp = derivada_a(x0)

# Formula de la derivada hacia delante
der_delante = (f(x0 + h) - f(x0)) / h

# Formula de la derivada hacia atras
der_atras = (f(x0) - f(x0 - h)) / h

# Formula de la derivada central
der_central = (f(x0 + h) - f(x0 - h)) / (2 * h)

# Errores
error_d = (abs(der_delante-valor_comp)/abs(valor_comp))*100
error_a = (abs(der_atras-valor_comp)/abs(valor_comp))*100
error_c = (abs(der_central-valor_comp)/abs(valor_comp))*100

print('Valor analitico: ', valor_comp)
print('')
print('Hacia delante: ', der_delante)
print('error= ', error_d, '%')
print('')
print('Hacia atras: ', der_atras)
print('error= ', error_a, '%')
print('')
print('Central: ', der_central)
print('error= ', error_c, '%')

# Grafica 
plt.figure(figsize=(10, 5))
x_plot = np.linspace(xinf-5, xsup+5, 100) # Division de 200 
y_plot = f(x_plot)
plt.plot(x_plot, y_plot, 'pink', label="f(x)" )
plt.plot(x_plot, derivada_a(x_plot), 'purple', label="f'(x)")
plt.plot(valor_comp,  derivada_a(valor_comp), 'ro', label='Valor analitico')
plt.plot(der_delante, derivada_a(der_delante), 'g>', label='Hacia delante')
plt.plot(der_atras, derivada_a(der_atras) ,'b<', label='Hacia atras')
plt.plot(der_central, derivada_a(der_central) ,'mx', markersize=10, label='Central')

plt.axvline(x=x0, color='r', linestyle='--')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Derivadas: Hacia delante, atras y central')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.show()
