import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d as gf
from scipy.ndimage import gaussian_filter as gf2
from scipy.interpolate import interp1d, interp2d

def plot(
		data, 
		bins=None, 
		smooth1d=None, 
		labels=None, 
		cmap=None,
		color1d=None,
		plot_scatter=None,
		scatter_color=None,
		CL = None,
		CL_color = None
):
	data = np.array(data)
	P = data.T
	ndim = len(P)
	print("\n\t ndim =", ndim,"\n")
	plt.rcParams.update({'font.family':'serif','font.size':12})
	
	fig = plt.figure(figsize=(10,10))
	
	if(cmap==None): cmap='hot'
	if(plot_scatter==None): True
	if(smooth1d==None): smooth1d = 1
	if(scatter_color==None): scatter_color='w'
	if(bins==None): bins = 20
	if(labels==None): 
		labels = ['$p_%d$' % i for i in range(1,ndim+1)]
	
	if(ndim>1):
		for i in range(ndim): # rows (y)
			for j in range(ndim): # columns (x)
				if(i>j): # Off Diagonal
					
					p1 = P[j]
					p2 = P[i]
					
					ax = plt.subplot(ndim,ndim,ndim*i+j+1)

					h, x, y = np.histogram2d(p2,p1,bins=20)
					h /= np.matrix.max(np.matrix(h))
					
					c = ax.imshow(h,extent=[min(p1),max(p1),min(p2),max(p2)],cmap=cmap,interpolation='bilinear',aspect='auto',origin='lower')
					if(plot_scatter):
						ax.scatter(p1,p2,marker='.',color=scatter_color,lw=0,alpha=0.5,s=10)
					
					#===================================================
					# Plot Confidence Levels Contours
					#===================================================

					if(CL!=None):
						CLx = CL.copy()
						CLx.sort()
						CLx.reverse()
						CLx = np.array(CLx)/100
						h_smooth = gf(h,1)
						func_interp = interp2d(x[0:-1],y[0:-1],h_smooth.T,kind='linear',bounds_error=False)
						u = np.linspace(min(x),max(x),100)
						v = np.linspace(min(y),max(y),100)
						du = u[1]-u[0]
						dv = v[1]-v[0]
						F = func_interp(u,v)
						F = gf2(F,2)
						F/=np.matrix.sum(np.matrix(F*du*dv))

						nval = 1000
						values = np.linspace(0,np.matrix.max(np.matrix(F)),nval)
						Cum = ( (F>=values[:,None,None])*F ).sum(axis=(1,2))*du*dv
						func_cum = interp1d(Cum,values)
						ax.contour(F.T, func_cum(CLx), extent=[min(p1),max(p1),min(p2),max(p2)],colors=CL_color)
						#ax.set_xlim(min(p1),max(x))
						#ax.set_ylim(min(y),max(y))

					if(i!=ndim-1):
						ax.xaxis.set_ticklabels([])
						
					if(j!=0):
						ax.yaxis.set_ticklabels([])
						
					plt.grid(color='w',ls='--',alpha=0.3)
					
				elif(i==j): # Diagonal
					print("\t axis:",labels[i])
					ax = plt.subplot(ndim,ndim,ndim*i+j+1)

					h, b = np.histogram(P[i],bins=bins)
					x = b[0:-1] ; y=h
					
					if(smooth1d!=0): 
						y = gf(h,smooth1d)
					
					func = interp1d(x,y)
					x = np.linspace(min(x),max(x),100)
					y = func(x) 
					
					if(smooth1d!=0): 
						y = gf(y,smooth1d)
					
					plt.plot(x,y,color='k',lw=2)
					zeros = np.ones(len(x))*min(y)
					if(color1d!=None):
						plt.fill_between(x,zeros,y,color=color1d,alpha=1)
					#plt.hist(P[i],histtype='step',color='r',lw=2)
					#plt.plot(b[0:-1],h)
					plt.xlim(min(P[i]),max(P[i]))
					
					ax.set_title(labels[i],size=12)
					if(i!=ndim-1): ax.xaxis.set_ticklabels([])
					ax.yaxis.set_ticklabels([])
					plt.grid(alpha=0.5,ls='--',color='k')
					
				if(i==ndim-1):
					ax.set_xlabel(labels[j])
				if(j==0):
					ax.set_ylabel(labels[i])

		plt.tight_layout()
		plt.subplots_adjust(left=None, bottom=0.13, right=None, top=None, wspace=0.05, hspace=0.05)
		cax = plt.axes([0.1,0.05,0.8,0.02])
		plt.colorbar(c,label='Points Density',orientation='horizontal',cax=cax)
		return fig
