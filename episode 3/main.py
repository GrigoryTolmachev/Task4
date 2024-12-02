from sympy import symbols, sqrt, dsolve, Function, Eq
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
x = symbols('x')
y = Function('y')
diff_eq = Eq(y(x).diff(x), -2*y(x))
solution = dsolve(diff_eq, y(x), ics={y(0): sqrt(2)})
xrr=[]
yrr=[]
for i in range(100):
    xrr.append(i/10)
    yrr.append(float(str(solution.evalf(subs={x : i/10})).split()[1].split(')')[0]))
plt.plot(xrr,yrr,label='sympy')
def returns_dydt(y, t):
    dydt = -y * 2
    return dydt
y0 = np.sqrt(2)
t = np.linspace(0, 10,100)
y1 = odeint(returns_dydt, y0, t)
plt.plot(t, y1,label='scipy')
plt.legend()
plt.savefig('plots.png')
plt.show()
print(y1[4],yrr[4])
for i in range (100):
    y1[i]=yrr[i]-y1[i]
plt.plot(t,y1)
plt.title('y.simpy-y.scipy')
plt.savefig('difference.png')
plt.show()

