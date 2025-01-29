import numpy as np
import pylab as plt
import matplotlib
from matplotlib import gridspec

#####get data and downsize matrix#####

def equalize(matrix,size=50):
    matrix_reduced = np.zeros((int(NE/size),int(NE/size)))
    for i in np.arange(0,int(NE/size),1):
        for j in np.arange(0,int(NE/size),1):
            matrix_reduced[i,j] = np.mean(matrix[i*size:(i+1)*size,j*size:(j+1)*size])
    return matrix_reduced


NE = 10000
times = [750000.0,907500.0,1050000.0,1500000.0]


def cm2inch(value):
    return value/2.54

plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["lines.linewidth"]=1.
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=6
plt.rcParams["ytick.labelsize"]=6
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams["legend.fontsize"] = 6

memory_color= '#C6710A'
color1 =  '#5599FF' #blue #tDCS


fig = plt.figure(figsize=(cm2inch(16), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 4)
gs1.update(top=0.92,bottom=0.2,left=0.08,right=0.85,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[0,3])


axes = [ax1,ax2,ax3,ax4]
vmin=0.075
vmax=0.16
averagesize=50
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/learning-only/EE-matrix/'
for idx in [0,1,2]:
    time = times[idx]
    matrix = np.load(T+"EE_matrix_step_"+str(time)+".npy")*10.
    matrix_reduced = equalize(matrix)
    axes[idx].imshow(matrix_reduced,vmin=vmin,vmax=vmax)
    axes[idx].set_title(str(time/1000.)+"s",fontsize=8.)
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])
    
ax1.set_xticks(np.arange(-0.5,200,50))
ax1.set_xticklabels(np.arange(0,201,50)*averagesize)
ax1.set_yticks(np.arange(-0.5,200,50))
ax1.set_yticklabels(np.arange(0,201,50)*averagesize)
ax1.set_xlabel("pre- neurons")
ax1.set_ylabel("post- neurons")

img = ax4.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
cax4 = fig.add_axes([0.86,0.2,0.01,0.72])
cbar = plt.colorbar(img,cax=cax4)
cbar.set_ticks((np.linspace(vmin,vmax,5)))
cbar.set_label("Connectivity "+r'$\Gamma$')


ax3.plot([-0.5,-0.5],[-0.5,29.5],'w-')
ax3.plot([29.5,29.5],[-0.5,29.5],'w-')
ax3.plot([-0.5,29.5],[-0.5,-0.5],'w-')
ax3.plot([-0.5,29.5],[29.5,29.5],'w-')



ax4.imshow(equalize(matrix,size=10)[0:150,0:150],vmin=vmin,vmax=vmax)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_xticks(np.arange(-0.5,150,30))
ax4.set_xticklabels(np.arange(0,151,30)*10)
ax4.set_title(str(time/1000.)+"s",fontsize=8.)


plt.savefig("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/Figures/Figure1-learning/matrix-memory-only.svg")
plt.show()
