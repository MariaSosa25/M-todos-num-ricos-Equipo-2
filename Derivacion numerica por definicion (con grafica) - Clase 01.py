
import numpy as np
import matplotlib.pyplot as plt

# Calcula el resultado de la funcion establecida
def f(x):
    return np.sin(x) # Cambiar aqui!

# Se grafican las funciones
xinf= int(input('Limite inferior de grafica:\n'))
xsup= int(input('\nLimite superior de grafica:\n'))

# Crea los intervalos espaciados por 0.1 dentro del limite
x= np.arange(xinf, xsup, 0.1)

# Grafica con coordenadas x y f(x)
plt.plot(x, f(x), 'pink')


h= float(0.1) # h= x2-x1, valor lo mas pequeño posible
i=1
x0= float(input('En que punto quieres evaluar la derivada x0: '))
n= int(input('\n Cuantas veces se divide el intervalo?: '))

# Encuentra el limite cuando h --> 0
for i in range(1,n):
    # der --> derivada 
    der = (f(x0+h)-f(x0))/h # Derivada por definicion
    h= h/2

print('\nEl valor de la derivada es: ', der)
# Grafica x0 y la derivada
plt.plot(x0,der, 'ro') # 'ro' = circulo rojo

# x pasada?
xpas= np.abs(xsup-xinf)/ float(n)
i=0

# Grafica cada punto de la derivada
for i in range(xinf, n, 1):
    x0= xinf + i*xpas
    # der = (f(x0+h)-f(x0-h))/(2.0*h)
    der = (f(x0+h)-f(x0))/h
    h= h/2.0
    plt.plot(x0, der, 'c.') # Color azul con punto

plt.show()
