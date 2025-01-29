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


fig = plt.figure(figsize=(cm2inch(14), cm2inch(6)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.92,bottom=0.1,left=0.08,right=0.99,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

T1 = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/'
T2 = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/'
T3 = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/'

x1 = np.arange(-6,7,1)*2.5*40000000.0/(10**9)
x2 = x1[::2]


################plot T1####################
unspecific_conn = []
specific_conn   = []
overlap_conn1   = []
overlap_conn2   = []

seeds = [2,4,6,8,10,12,14]
for seed in seeds:
    unspecific = np.load(T1+'/unspecific/1000g1g1_seed_'+str(seed)+'.npy')
    specific   = np.load(T1+'/specific/1000g1g1_seed_'+str(seed)+'.npy')
    
    unspecific_conn.append(unspecific[-1])
    specific_conn.append(specific[-1])

seeds = [0,1,2,3,4,5,6]
for seed in seeds:
    overlap1    = np.load(T1+'/before-learning-50%/data/1000g2g2_seed_'+str(seed)+'.npy')
    overlap2    = np.load(T1+'/before-learning-50%/data/1000g3g3_seed_'+str(seed)+'.npy')

    overlap_conn1.append(overlap1[-1])
    overlap_conn2.append(overlap2[-1])



ax1.plot(x2,unspecific_conn,'k-',label=r"$\mathrm{non-focal}$")
ax1.plot(x2,specific_conn,'r-',label=r"$\mathrm{focal}$")

ax4.plot(x2,overlap_conn1,'b-',label=r"$\mathrm{overlap\_pop}$")
ax4.plot(x2,overlap_conn2,'b--',label=r"$\mathrm{L\_pop}$")

ax1.set_title("tDCS before learning")
ax1.legend(bbox_to_anchor=(0.01, 0.7, 1., 0.2), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax4.legend(bbox_to_anchor=(0.01, 0.7, 1., 0.2), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)


################plot T2####################
unspecific_conn = []
specific_conn   = []
overlap_conn1   = []
overlap_conn2   = []

seeds = [2,4,6,8,10,12,14]
for seed in seeds:
    unspecific = np.load(T2+'/unspecific/1000g1g1_seed_'+str(seed)+'.npy')
    specific   = np.load(T2+'/specific/1000g1g1_seed_'+str(seed)+'.npy')
    
    unspecific_conn.append(unspecific[-1])
    specific_conn.append(specific[-1])

seeds = [0,1,2,3,4,5,6]
for seed in seeds:
    overlap1    = np.load(T2+'/during-learning-50%/data/1000g2g2_seed_'+str(seed)+'.npy')
    overlap2    = np.load(T2+'/during-learning-50%/data/1000g3g3_seed_'+str(seed)+'.npy')

    overlap_conn1.append(overlap1[-1])
    overlap_conn2.append(overlap2[-1])


ax2.plot(x2,unspecific_conn,'k-',label="non-focal")
ax2.plot(x2,specific_conn,'r-',label="focal")
ax5.plot(x2,overlap_conn1,'b-',label="overlap1")
ax5.plot(x2,overlap_conn2,'b--',label="overlap2")

ax2.set_title("tDCS during learning")



################plot T3####################
unspecific_conn = []
specific_conn   = []
overlap_conn1   = []
overlap_conn2   = []

seeds = [2,4,6,8,10,12,14]
for seed in seeds:
    unspecific = np.load(T3+'/unspecific/1000g1g1_seed_'+str(seed)+'.npy')
    specific   = np.load(T3+'/specific/1000g1g1_seed_'+str(seed)+'.npy')
    
    unspecific_conn.append(unspecific[-1])
    specific_conn.append(specific[-1])

seeds = [0,1,2,3,4,5,6]
for seed in seeds:
    overlap1    = np.load(T3+'/after-learning-50%/data/1000g2g2_seed_'+str(seed)+'.npy')
    overlap2    = np.load(T3+'/after-learning-50%/data/1000g3g3_seed_'+str(seed)+'.npy')

    overlap_conn1.append(overlap1[-1])
    overlap_conn2.append(overlap2[-1])


ax3.plot(x2,unspecific_conn,'k-',label="non-focal")
ax3.plot(x2,specific_conn,'r-',label="focal")
ax3.set_title("tDCS after learning")
ax6.plot(x2,overlap_conn1,'b-',label="overlap1")
ax6.plot(x2,overlap_conn2,'b--',label="overlap2")

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.set_ylim(0.01,0.016)
    ax.set_xticks(())
    ax.set_yticks(())
    ax.axhline(y=unspecific_conn[3],color='grey',linestyle='-',alpha=0.5)
    ax.axvline(x=0,color='grey',linestyle='-',alpha=0.5)


    ax.set_yticks(np.arange(0.01,0.017,0.002))
    ax.set_xticks(np.arange(-0.6,0.7,0.2))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

ax4.set_xlabel(r'$\Delta V_m$ (mV)')
ax4.set_ylabel(r'Connectivity ($\Gamma$)')
ax1.set_ylabel(r'Connectivity ($\Gamma$)')


for ax in [ax1,ax2,ax3]:
    ax.set_xticks(())
for ax in [ax2,ax3,ax5,ax6]:
    ax.set_yticks(())

plt.savefig("final-conn-replace-presentation.svg")
plt.show()
