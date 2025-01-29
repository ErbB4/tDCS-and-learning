import numpy as np
import pylab as plt
import matplotlib
from matplotlib import gridspec

def cm2inch(value):
    return value/2.54

def equalize(matrix,size=50):
    matrix_reduced = np.zeros((int(NE/size),int(NE/size)))
    for i in np.arange(0,int(NE/size),1):
        for j in np.arange(0,int(NE/size),1):
            matrix_reduced[i,j] = np.mean(matrix[i*size:(i+1)*size,j*size:(j+1)*size])
    return matrix_reduced

plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["lines.linewidth"]=1.
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=6
plt.rcParams["ytick.labelsize"]=6
plt.rcParams["font.family"] = "serif"
plt.rcParams['mathtext.fontset'] = 'dejavuserif'
plt.rcParams["legend.fontsize"] = 6

fig = plt.figure(figsize=(cm2inch(16), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 4)
gs1.update(top=0.92,bottom=0.2,left=0.08,right=0.85,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[0,3])

memory_color= '#9681B7'
color1 =  '#007849' #green #tDCS

NE = 10000
times = [750000.0,900000.0,1200000.0]
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/after-learning-50%/EE_matrix/'


        
axes = [ax1,ax2,ax3,ax4]
for idx in [0,1,2]:
    time = times[idx]
    matrix = np.load(T+"EE_matrix_step_"+str(time)+".npy")*10.
    matrix_reduced = equalize(matrix)
    axes[idx].imshow(matrix_reduced,vmin=0.075,vmax=0.16)
    axes[idx].set_title(str(time/1000.)+"s",fontsize=8.)
    axes[idx].set_xticks([])
    axes[idx].set_yticks([])

ax1.set_xticks(np.arange(-0.5,200,50))
ax1.set_xticklabels(np.arange(0,201,50)*50)
ax1.set_yticks(np.arange(-0.5,200,50))
ax1.set_yticklabels(np.arange(0,201,50)*50)

ax1.set_xlabel("pre-")
ax1.set_ylabel("post-")

img = ax3.imshow(matrix_reduced,vmin=0.075,vmax=0.16)
cax3 = fig.add_axes([0.86,0.2,0.01,0.72])
cbar = plt.colorbar(img,cax=cax3)
cbar.set_ticks((np.linspace(0.075,0.16,5)))
cbar.set_label("Connectivity "+r'$\Gamma$')

ax3.plot([-0.5,-0.5],[-0.5,29.5],'w-')
ax3.plot([29.5,29.5],[-0.5,29.5],'w-')
ax3.plot([-0.5,29.5],[-0.5,-0.5],'w-')
ax3.plot([-0.5,29.5],[29.5,29.5],'w-')

ax4.imshow(equalize(matrix,size=10)[0:150,0:150],vmin=0.075,vmax=0.16)
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_title(str(time/1000.)+"s",fontsize=8.)

ax4.plot([-0.5,-0.5],[-0.5,99.5],'-',color=color1)
ax4.plot([99.5,99.5],[-0.5,99.5],'-',color=color1)
ax4.plot([-0.5,99.5],[-0.5,-0.5],'-',color=color1)
ax4.plot([-0.5,99.5],[99.5,99.5],'-',color=color1)

ax4.plot([49.5,49.5],[49.5,149.5],'-',color=memory_color)
ax4.plot([149.5,149.5],[49.5,149.5],'-',color=memory_color)
ax4.plot([49.5,149.5],[49.5,49.5],'-',color=memory_color)
ax4.plot([49.5,149.5],[149.5,149.5],'-',color=memory_color)


ax4.set_xticks(np.arange(-0.5,150,30))
ax4.set_xticklabels(np.arange(0,151,30)*10)



plt.savefig("matrix.svg")
plt.show()
