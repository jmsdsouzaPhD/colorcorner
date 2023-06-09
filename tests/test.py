import numpy as np
import matplotlib.pyplot as plt
import colorcorner.colorcorner as cc

x = np.random.normal(0,1,10000)
y = np.random.normal(0,1,10000)
z = np.random.normal(0,1,10000)

labels = ['$\\alpha$','$\\beta$','$\gamma$']

fig = cc.plot(np.transpose([x,y,z]),smooth1d=2,labels=labels,cmap='jet',CL=[30,60,90],CL_color='r',plot_scatter=False,color1d='b',scatter_color='w')
fig.savefig('fig.png')
plt.show()
