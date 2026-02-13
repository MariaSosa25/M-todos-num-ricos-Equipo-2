
import sympy as sp

x = sp.Symbol('x')
# Expresión se cambia de acuerdo con la función
f = 1/(sp.sqrt(5-7*x**2))
integral_expr = sp.Integral(f, (x, 0, 0.8))

resultado = integral_expr.evalf()

print(f"I = {resultado}")