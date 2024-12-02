from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
with open ('large.txt','r') as f:
    s=f.read().split('\n')
    a=[]
    for i in range(int(s[0])):
        a.append(s[i+1].split())
        for j in range(int(s[0])):
            a[i][j]=float(a[i][j])
    b=s[-1].split()
    for i in range(int(s[0])):
        b[i]=float(b[i])
    x = linalg.solve(a, b)
    y=np.arange(int(s[0]))
    fig, ax = plt.subplots()
    ax.bar(y,x)
    ax.set_xticks(y)
    ax.set_xticklabels('')
    plt.savefig('without_labels.png')
    plt.show()

