import numpy as np
import pylab as pl
import matplotlib
from matplotlib import gridspec

def cm2inch(value):
    return value/2.54

pl.rcParams["axes.titlesize"]=10
pl.rcParams["axes.labelsize"]=8
pl.rcParams["lines.linewidth"]=1.
pl.rcParams["lines.markersize"]=5
pl.rcParams["xtick.labelsize"]=6
pl.rcParams["ytick.labelsize"]=6
pl.rcParams["font.family"] = "serif"
pl.rcParams['mathtext.fontset'] = 'dejavuserif'
pl.rcParams["legend.fontsize"] = 6

T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/tDCS-only-np/'

g1g1 = np.load(T+"1000g1g1_seed_1.npy")*10.
g1g2 = np.load(T+"1000g1g2_seed_1.npy")*10.
g2g2 = np.load(T+"1000g2g2_seed_1.npy")*10.

rates1 = np.load(T+"1000rates1_seed_1.npy")
rates2 = np.load(T+"1000rates2_seed_1.npy")

t = np.load(T+"t_plotx.npy")/1000.


c1 = '#007849' #green #for tDCS
c2 = '#4D4D4D' #dark grey #for background
c3 = '#999999' #light grey #for interconnections
DCS_color= '#BBDB88' #darkyellow for span of DCS process


fig = pl.figure(figsize=(cm2inch(6), cm2inch(5)))
gs1 = gridspec.GridSpec(2, 1)
gs1.update(top=0.99,bottom=0.15,left=0.2,right=0.95,hspace=0.1,wspace=0.25)
ax1 = pl.subplot(gs1[0,0])
ax2 = pl.subplot(gs1[1,0])



ax1.plot(t,rates1,'-',color=c1,label=r'$\mathrm{sti\ (depolarizing \ DC)}$')
ax1.plot(t,rates2,'-',color=c2)

ax1.axvspan(750,900,color=DCS_color,alpha=0.2)
ax1.set_ylabel("Firing rate (Hz)")
ax1.set_xticks(())
ax1.legend(loc='lower right',frameon=False)
ax1.set_xlim(0,2000)
ax1.set_ylim(0,16)


ax2.plot(t,g1g1,'-',color=c1,label=r'$\mathrm{sti} \rightarrow \mathrm{sti}$')
ax2.plot(t,g1g2,'-',color=c3)
ax2.plot(t,g2g2,'-',color=c2)
ax2.set_xlim(0,2000)
ax2.set_ylim(0,0.16)
ax2.axvspan(750,900,color=DCS_color,alpha=0.2)
ax2.set_ylabel('$\Gamma$')
ax2.legend(loc='lower right',frameon=False)

times = [750000.0,907500.0,1050000.0,1500000.0]
ax2.plot(times[0]/1000.,g1g1[np.where(t==times[0]/1000.)],'.',color='#353A90')
ax2.plot(times[1]/1000.,g1g1[np.where(t==times[1]/1000.)],'.',color='#353A90')
ax2.plot(times[2]/1000.,g1g1[np.where(t==times[2]/1000.)],'.',color='#353A90')
ax2.plot(times[3]/1000.,g1g1[np.where(t==times[3]/1000.)],'.',color='#353A90')

ax2.set_xlabel("Time (s)")

for ax in [ax1,ax2]:
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        

pl.savefig("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/Figures/Figure2-tDCS/rate-conn-positive-DC.svg")
pl.show()


