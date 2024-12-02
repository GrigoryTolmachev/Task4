from sympy import symbols, det, Matrix, eye, Eq, solve
l,r,m,x=symbols('lambda, rho, mu, x')
a=Matrix([[0,0,0,-1/r,0,0,0,0,0],
              [0,0,0,0,-1/r,0,0,0,0],
              [0,0,0,0,0,-1/r,0,0,0],
              [-(l+2*m),0,0,0,0,0,0,0,0],
              [0,-m,0,0,0,0,0,0,0],
              [0,0,-m,0,0,0,0,0,0],
              [-l,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [-l,0,0,0,0,0,0,0,0]])
e=eye(9)
f=det(a-x*e)
q=Eq(f,0)
y=solve(q,x)
for i, root in enumerate(y):
    print(f'Root {i}: {root}')