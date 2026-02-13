import numpy as np
import matplotlib.pyplot as plt

# Definir funcion
def f(x):
    return 1/(np.sqrt(5-(7*x**2))) # CAMBIAR !!

# Limites
a=0
b=0.8

# Cantidad de subintervalos (MULTIPLO DE 3)
n = 60 # Cambiar !!

h = (b - a) / n
suma = f(a)+f(b)

print(f"a = {a} , f(a) = {f(a)}")
for i in range(1,n-1):
    x= a+ i*h
    print(f"x{i} = {x} , f(x{i}) = {f(x)}")
    if (i%3==0):
        suma= suma + (2*f(x))
    else:
        suma= suma + (3*f(x))
print(f"b = {b} , f(b) = {f(b)}")
 
integral = suma*((3*h)/8.0) # Formula
print("")
print("I=", integral)

# Grafica
x_range = np.linspace(a - 0.5, b + 0.5, 100)
x_fill = np.linspace(a, b, 100)

plt.figure(figsize=(10, 5))
plt.grid(True, which='both', linestyle='--', color='gray', alpha=0.7)
plt.axhline(0, color='skyblue', lw=2) 
plt.axvline(0, color='skyblue', lw=2)
plt.fill_between(x_fill, f(x_fill), color='slateblue', alpha=0.25)
plt.vlines([a, b], 0, [f(a), f(b)], colors='slateblue', linestyles='--')

plt.plot(x_range, f(x_range), color='purple', lw=2, label='f(x)')
plt.title('Método de Simpson 3/8')
plt.legend()

plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()