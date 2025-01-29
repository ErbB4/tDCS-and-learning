import numpy as np
import pylab as plt
import matplotlib
from matplotlib import gridspec



time = 1200000.0
#####get data and downsize matrix#####

def equalize(matrix,size=50):
    matrix_reduced = np.zeros((int(NE/size),int(NE/size)))
    for i in np.arange(0,int(NE/size),1):
        for j in np.arange(0,int(NE/size),1):
            matrix_reduced[i,j] = np.mean(matrix[i*size:(i+1)*size,j*size:(j+1)*size])
    return matrix_reduced


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

memory_color= '#9681B7'
color1 =  '#007849' #green #tDCS


NE = 10000


########################plot after seed1######################

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.92,bottom=0.2,left=0.08,right=0.85,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])


vmin=0.075
vmax=0.16
averagesize=50
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/strong-tDCS/two-cases/after-learning/data/'

matrix = np.load(T+"EE_matrix_step_1200000.0_seed_1.npy")*10.
matrix_reduced = equalize(matrix,size=10)[0:150,0:150]
ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
ax1.set_title(r'$\Delta \mathrm{V_m}=-2.8 \mathrm{mV}$',fontsize=8.)


ax1.set_xticks(np.arange(-0.5,150,30))
ax1.set_xticklabels(np.arange(0,151,30)*10)
ax1.set_yticks(np.arange(-0.5,150,30))
ax1.set_yticklabels(np.arange(0,151,30)*10)


img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
cax1 = fig.add_axes([0.86,0.2,0.035,0.72])
cbar = plt.colorbar(img,cax=cax1)
cbar.set_ticks((np.linspace(vmin,vmax,5)))
cbar.set_label("Connectivity "+r'$\Gamma$')


ax1.plot([-0.5,-0.5],[-0.5,99.5],'-',color=color1)
ax1.plot([99.5,99.5],[-0.5,99.5],'-',color=color1)
ax1.plot([-0.5,99.5],[-0.5,-0.5],'-',color=color1)
ax1.plot([-0.5,99.5],[99.5,99.5],'-',color=color1)

ax1.plot([49.5,49.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([149.5,149.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[49.5,49.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[149.5,149.5],'-',color=memory_color)


plt.savefig("matrix-after-seed1.svg")


########################plot after seed2######################

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.92,bottom=0.2,left=0.08,right=0.85,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])


vmin=0.075
vmax=0.16
averagesize=50
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/strong-tDCS/two-cases/after-learning/data/'

matrix = np.load(T+"EE_matrix_step_1200000.0_seed_2.npy")*10.
matrix_reduced = equalize(matrix,size=10)[0:150,0:150]
ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
ax1.set_title(r'$\Delta \mathrm{V_m}=2.8 \mathrm{mV}$',fontsize=8.)


ax1.set_xticks(np.arange(-0.5,150,30))
ax1.set_xticklabels(np.arange(0,151,30)*10)
ax1.set_yticks(np.arange(-0.5,150,30))
ax1.set_yticklabels(np.arange(0,151,30)*10)


img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
cax1 = fig.add_axes([0.86,0.2,0.035,0.72])
cbar = plt.colorbar(img,cax=cax1)
cbar.set_ticks((np.linspace(vmin,vmax,5)))
cbar.set_label("Connectivity "+r'$\Gamma$')


ax1.plot([-0.5,-0.5],[-0.5,99.5],'-',color=color1)
ax1.plot([99.5,99.5],[-0.5,99.5],'-',color=color1)
ax1.plot([-0.5,99.5],[-0.5,-0.5],'-',color=color1)
ax1.plot([-0.5,99.5],[99.5,99.5],'-',color=color1)

ax1.plot([49.5,49.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([149.5,149.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[49.5,49.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[149.5,149.5],'-',color=memory_color)


plt.savefig("matrix-after-seed2.svg")


########################plot after seed3######################

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.92,bottom=0.2,left=0.08,right=0.85,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])


vmin=0.075
vmax=0.16
averagesize=50
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/strong-tDCS/two-cases/after-learning/data/'

matrix = np.load(T+"EE_matrix_step_1200000.0_seed_3.npy")*10.
matrix_reduced = equalize(matrix,size=10)[0:150,0:150]
ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
ax1.set_title(r'$\Delta \mathrm{V_m}=0 \mathrm{mV}$',fontsize=8.)


ax1.set_xticks(np.arange(-0.5,150,30))
ax1.set_xticklabels(np.arange(0,151,30)*10)
ax1.set_yticks(np.arange(-0.5,150,30))
ax1.set_yticklabels(np.arange(0,151,30)*10)


img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax)
cax1 = fig.add_axes([0.86,0.2,0.035,0.72])
cbar = plt.colorbar(img,cax=cax1)
cbar.set_ticks((np.linspace(vmin,vmax,5)))
cbar.set_label("Connectivity "+r'$\Gamma$')


ax1.plot([-0.5,-0.5],[-0.5,99.5],'-',color=color1)
ax1.plot([99.5,99.5],[-0.5,99.5],'-',color=color1)
ax1.plot([-0.5,99.5],[-0.5,-0.5],'-',color=color1)
ax1.plot([-0.5,99.5],[99.5,99.5],'-',color=color1)

ax1.plot([49.5,49.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([149.5,149.5],[49.5,149.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[49.5,49.5],'-',color=memory_color)
ax1.plot([49.5,149.5],[149.5,149.5],'-',color=memory_color)


plt.savefig("matrix-after-seed3.svg")


plt.show()
