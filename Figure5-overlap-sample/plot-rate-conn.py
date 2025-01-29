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

red = '#E54B4B'
black = '#16528E'
yellow= '#FECB00'


memory_color= '#BFB1D3' #span
DCS_color= '#BBDB88' #span

c1 = '#9681B7' #purple #for learning
c2 = '#007849' #green #for tDCS
overlap_color = '#E97117'

color2 = '#4D4D4D' #dark grey
color3 = '#999999' #light grey#

colors = np.hstack((np.ones(3),np.linspace(1,0,5),1,np.linspace(0,1,5),np.ones(3)))

#########################plot before######################

fig = plt.figure(figsize=(cm2inch(10), cm2inch(5)))
gs1 = gridspec.GridSpec(2, 1)
gs1.update(top=0.99,bottom=0.15,left=0.15,right=0.95,hspace=0.1,wspace=0.25)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0])
        
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/before-learning-50%/data/'

t = np.load(T+"t_plotx.npy")/1000.

elec_field_strens = np.arange(-8,9,1)*2.5
elec_field_strens = elec_field_strens*40000000.0/(10**9)



rate1 = np.load(T+"1000rates1_seed_6.npy")
rate2 = np.load(T+"1000rates2_seed_6.npy")
rate3 = np.load(T+"1000rates3_seed_6.npy")
rate4 = np.load(T+"1000rates4_seed_6.npy")
conn1 = np.load(T+"1000g1g1_seed_6.npy")*10.
conn2 = np.load(T+"1000g2g2_seed_6.npy")*10.
conn3 = np.load(T+"1000g3g3_seed_6.npy")*10.
conn4 = np.load(T+"1000g4g4_seed_6.npy")*10.

ax1.plot(t,rate4,color=color2,label=r'$\mathrm{exc}$')
ax1.plot(t,rate1,color=c2,label=r'$\mathrm{sti}$')
ax1.plot(t,rate3,color=c1,label=r'$\mathrm{engram}$')
ax1.plot(t,rate2,'--',color=overlap_color,label=r'$\mathrm{engram+sti}$')

ax2.plot(t,conn4,color=color2,label=r'$\mathrm{exc} \leftrightarrow  \mathrm{exc}$')  
ax2.plot(t,conn1,color=c2,label=r'$\mathrm{sti} \leftrightarrow  \mathrm{sti}$')
ax2.plot(t,conn3,color=c1,label=r'$\mathrm{engram} \leftrightarrow  \mathrm{engram}$') 
ax2.plot(t,conn2,'--',color=overlap_color,label=r'$\mathrm{engram+sti} \leftrightarrow  \mathrm{engram+sti}$') 
    
ax1.set_ylabel("Firing rate (Hz)")
ax1.set_xticks(())
ax1.legend(bbox_to_anchor=(0.02, 0.65, 0.4, 0.25), loc=2,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax1.set_ylim(0,17)
ax1.set_xlim(0,1600)

ax2.set_ylabel(r"$\Gamma$")
ax2.set_ylim(0.02,0.17)
ax2.set_xlim(0,1600)
ax2.set_xlabel('Time (s)')

ax2.plot([1200],conn3[np.where(t==1200.)],'.',color='#353A90')
ax1.text(825,14,'DC',fontsize=5,ha='center',va='bottom')
ax1.text(998,14,'ML',fontsize=5,ha='center',va='bottom')


for ax in [ax1,ax2]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.axvspan(750,900,color=DCS_color,alpha=0.2)
    ax.axvspan(900,1050,color=memory_color,alpha=0.2)

plt.savefig("rate-conn-before-seed6.svg")




#########################plot after######################

fig = plt.figure(figsize=(cm2inch(10), cm2inch(5)))
gs1 = gridspec.GridSpec(2, 1)
gs1.update(top=0.99,bottom=0.15,left=0.15,right=0.95,hspace=0.1,wspace=0.25)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0])
        
T = '/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/after-learning-50%/data/'

t = np.load(T+"t_plotx.npy")/1000.

elec_field_strens = np.arange(-8,9,1)*2.5
elec_field_strens = elec_field_strens*40000000.0/(10**9)



rate1 = np.load(T+"1000rates1_seed_6.npy")
rate2 = np.load(T+"1000rates2_seed_6.npy")
rate3 = np.load(T+"1000rates3_seed_6.npy")
rate4 = np.load(T+"1000rates4_seed_6.npy")
conn1 = np.load(T+"1000g1g1_seed_6.npy")*10.
conn2 = np.load(T+"1000g2g2_seed_6.npy")*10.
conn3 = np.load(T+"1000g3g3_seed_6.npy")*10.
conn4 = np.load(T+"1000g4g4_seed_6.npy")*10.

ax1.plot(t,rate4,color=color2,label=r'$\mathrm{exc}$')
ax1.plot(t,rate1,color=c2,label=r'$\mathrm{sti}$')
ax1.plot(t,rate3,color=c1,label=r'$\mathrm{engram}$')
ax1.plot(t,rate2,'--',color=overlap_color,label=r'$\mathrm{engram+sti}$')

ax2.plot(t,conn4,color=color2,label=r'$\mathrm{exc} \leftrightarrow  \mathrm{exc}$')  
ax2.plot(t,conn1,color=c2,label=r'$\mathrm{sti} \leftrightarrow  \mathrm{sti}$')
ax2.plot(t,conn3,color=c1,label=r'$\mathrm{engram} \leftrightarrow  \mathrm{engram}$') 
ax2.plot(t,conn2,'--',color=overlap_color,label=r'$\mathrm{engram+sti} \leftrightarrow  \mathrm{engram+sti}$')   
    
ax1.set_ylabel("Firing rate (Hz)")
ax1.set_xticks(())
ax1.legend(bbox_to_anchor=(0.02, 0.65, 0.4, 0.25), loc=2,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax1.set_ylim(0,17)
ax1.set_xlim(0,1600)

ax2.set_ylabel(r"$\Gamma$")
ax2.set_ylim(0.02,0.17)
ax2.set_xlim(0,1600)
ax2.set_xlabel('Time (s)')

ax2.plot([750],conn3[np.where(t==750.)],'.',color='#353A90')
ax2.plot([900],conn3[np.where(t==900)],'.',color='#353A90')
ax2.plot([1200],conn3[np.where(t==1200.)],'.',color='#353A90')
ax1.text(825,14,'ML',fontsize=5,ha='center',va='bottom')
ax1.text(998,14,'DC',fontsize=5,ha='center',va='bottom')


for ax in [ax1,ax2]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.axvspan(750,900,color=memory_color,alpha=0.2)
    ax.axvspan(900,1050,color=DCS_color,alpha=0.2)

plt.savefig("rate-conn-after-seed6.svg")
plt.show()
