import numpy as np
import pylab as plt
import matplotlib
from matplotlib import gridspec


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


fig = plt.figure(figsize=(cm2inch(16), cm2inch(7.5)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.92,bottom=0.1,left=0.08,right=0.99,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

x1 = np.arange(-6,7,1)*2.5*40000000.0/(10**9)
x2 = x1[::2]
    
####################plot before learning##############

super_global = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/unspecific/super.npy")
super_specific = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/specific/super.npy")
overlap1 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/before-learning-50%/data/super_g2g2.npy")
overlap2 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/before-learning-50%/data/super_g3g3.npy")


ax1.plot(x1,super_global[2:-2],'k-',label=r"$\mathrm{non-focal}$")
ax1.plot(x1,super_specific[2:-2],'r-',label=r"$\mathrm{focal}$")

ax4.plot(x2,overlap1,'b-',label=r"$\mathrm{overlap\_pop}$")
ax4.plot(x2,overlap2,'b--',label=r"$\mathrm{L\_pop}$")

ax1.set_title("DCS before learning")
ax1.legend(bbox_to_anchor=(0.01, 0.7, 1., 0.2), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax4.legend(bbox_to_anchor=(0.01, 0.7, 1., 0.2), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)





####################plot during learning##############

super_global = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/unspecific/super.npy")
super_specific = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/specific/super.npy")
overlap1 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/during-learning-50%/data/super_g2g2.npy")
overlap2 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/during-learning-50%/data/super_g3g3.npy")

ax2.plot(x1,super_global[2:-2],'k-',label="non-focal")
ax2.plot(x1,super_specific[2:-2],'r-',label="focal")
ax5.plot(x2,overlap1,'b-',label="overlap1")
ax5.plot(x2,overlap2,'b--',label="overlap2")

ax2.set_title("DCS during learning")


####################plot after learning##############

super_global = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/unspecific/super.npy")
super_specific = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/specific/super.npy")
overlap1 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/after-learning-50%/data/super_g2g2.npy")
overlap2 = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/after-learning-50%/data/super_g3g3.npy")

ax3.plot(x1,super_global[2:-2],'k-',label="non-focal")
ax3.plot(x1,super_specific[2:-2],'r-',label="focal")
ax3.set_title("DCS after learning")
ax6.plot(x2,overlap1,'b-',label="overlap1")
ax6.plot(x2,overlap2,'b--',label="overlap2")


for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.set_ylim(50,450)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.axhline(y=super_global[8],color='grey',linestyle='-',alpha=0.5)
    ax.axvline(x=0,color='grey',linestyle='-',alpha=0.5)


    ax.set_yticks(np.arange(50,450,100))
    ax.set_xticks(np.arange(-0.6,0.7,0.2))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax4.set_xlabel(r'$\Delta V_m$ (mV)')
ax4.set_ylabel(r'$\Gamma$')
ax1.set_ylabel(r'$\Gamma$')

for ax in [ax1,ax2,ax3]:
    ax.set_xticks(())
for ax in [ax2,ax3,ax5,ax6]:
    ax.set_yticks(())


plt.savefig("gamma.svg")
plt.show()
