import sympy as sym

x, x_0, x_1, x_2, epsilon = sym.symbols('x x_0 x_1 x_2 epsilon')
p = (x - 1) * (x + 1) * (x - epsilon)

pert = p.subs(x, x_0 + epsilon * x_1 + epsilon*epsilon*x_2)

print(sym.collect(sym.expand(pert.series(epsilon, 0, 3)), epsilon))

order2 = sym.collect(sym.expand(pert.series(epsilon, 0, 3)), epsilon).removeO()
order1 = sym.collect(sym.expand(pert.series(epsilon, 0, 2)), epsilon).removeO()
order0 = sym.collect(sym.expand(pert.series(epsilon, 0, 1)), epsilon).removeO()
order2 -= order1
order2 /= epsilon**2
order1 -= order0
order1 /= epsilon

print(order0)
print(order1)
print(order2)

roots0 = sym.solve(order0, x_0)
print('roots0={0}'.format(roots0))

for root0 in roots0:
    root1 = sym.solve(order1.subs(x_0, root0))[0]
    x1 = sym.solve(order1, x_1)
    print(x1)
    x2 = sym.solve(order2, x_2)
    print(x2)

    root2 = sym.solve(order2.subs(x_0, root0).subs(x_1, root1))[0]
    print('x_0={0} x_1={1} x_2={2}'.format(root0, root1, root2))
