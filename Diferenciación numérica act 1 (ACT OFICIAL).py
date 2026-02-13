import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

i = 1
x = sp.Symbol("x")# hacer x un simbolo
Funcion = input("Escriba en lenguaje python la función a aproximar: ") # Cambiar a funcion
F = sp.sympify(Funcion) #hacer la expresión un símbolo
a = float(input("Deme una parte del intervalo de la funcion: ")) # INTERVALOS
b = float(input("Deme otra parte del intervalo de la funcion:")) # INTERVALOS

h = abs(float(b) - float(a)) # Calculo de h
derivadaanalítica = sp.diff(Funcion, x)

print(h)

while i < 4 :
    
    d = a-h
    c  = a+h
    
    fx = F.subs(x, a)
    fxminush = F.subs(x, d) #sustituir el valor en la función y su derivada
    fmasx = F.subs(x, c)
    derivadaC = ((fmasx-fxminush)/(2*h)).evalf()
    derivadaAd = ((fmasx-fx)/h).evalf()
    derivadaAt = ((fx-fxminush)/h).evalf()
    print("h =", h, "Derivada aproximada =", derivadaC, derivadaAd, derivadaAt)
    print("-------------------------------------------------------")
    h = h/2
    i = i+1
    
    f_num = sp.lambdify(x, Funcion, "numpy")
    df_num = sp.lambdify(x, derivadaanalítica, "numpy")

    # Dominio para graficar
    X = np.linspace(a - 10*h, a + 10*h, 4000)

    # Gráficas de función y derivada analítica
    plt.plot(X, f_num(X), label="f(x)", color="rebeccapurple")
    plt.plot(X, df_num(X), label="f'(x) analítica", linestyle="--",color="mediumorchid")
    
    # Puntos para graficar las derivadas aproximadas
    plt.scatter(a, derivadaC, color="orchid")
    plt.scatter(a, derivadaAd, color="darkmagenta")
    plt.scatter(a, derivadaAt, color="mediumvioletred")
    
    plt.xlabel("x")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid()
    plt.title("Función, derivada analítica y derivadas numéricas")
    plt.show()
    
# Hecho por Abby Ramírez López, Rachel Morera Fajardo y María José Sosa Rivero
    
   
    


