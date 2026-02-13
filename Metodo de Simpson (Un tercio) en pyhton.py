import numpy as np
import matplotlib.pyplot as plt

# Definir funcion
def f(x):
    return (np.log(x))**3 # CAMBIAR !!

# Limites
a=2
b=4

# Cantidad de subintervalos (PAR)
n = 1000 # Cambiar !!

h = (b - a) / n
suma = f(a)+f(b)

print(f"a = {a} , f(a) = {f(a)}")
for i in range(1,n-1):
    x= a+ i*h
    print(f"x{i} = {x} , f(x{i}) = {f(x)}")
    if (i%2==0):
        suma= suma + (2*f(x))
    else:
        suma= suma + (4*f(x))
print(f"b = {b} , f(b) = {f(b)}")
 
integral = suma*h/3.0 # Formula
print("")
print("I=", integral)

# Grafica
x_range = np.linspace(a - 0.5, b + 0.5, 100)
x_fill = np.linspace(a, b, 100)

plt.figure(figsize=(10, 5))
plt.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)
plt.axhline(0, color='purple', lw=2) 
plt.axvline(0, color='purple', lw=2)
plt.fill_between(x_fill, f(x_fill), color='pink', alpha=0.25)
plt.vlines([a, b], 0, [f(a), f(b)], colors='pink', linestyles='--')

plt.plot(x_range, f(x_range), color='coral', lw=2, label='f(x)')
plt.title('Método de Simpson 1/3')
plt.legend()

plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()