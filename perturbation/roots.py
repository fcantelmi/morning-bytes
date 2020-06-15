import sympy as sym

x, x_0, x_1, x_2, epsilon = sym.symbols('x x_0 x_1 x_2 epsilon')
p = (x - 1) * (x + 1) * (x - epsilon)

print(sym.poly(p))

pert = p.subs(x, x_0 + epsilon * x_1 + epsilon*epsilon*x_2)

print(sym.collect(sym.expand(pert.series(epsilon, 0, 3)), epsilon))
