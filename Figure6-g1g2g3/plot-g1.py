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

fig = plt.figure(figsize=(cm2inch(12), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.92,bottom=0.52,left=0.12,right=0.99,hspace=0.1,wspace=0.1)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
        
gs2 = gridspec.GridSpec(1, 3)
gs2.update(top=0.48,bottom=0.08,left=0.12,right=0.99,hspace=0.1,wspace=0.1)
ax4 = plt.subplot(gs2[0,0])
ax5 = plt.subplot(gs2[0,1])
ax6 = plt.subplot(gs2[0,2])

red          = '#E54B4B'
black        = '#16528E'
yellow       = '#FECB00'

memory_color= '#BFB1D3'
DCS_color= '#BBDB88'

alphas = [0.75,0.5,0.25,1,0.25,0.5,0.75]
t = np.load("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/t_plotx.npy")/1000.
elec_field_strens = [-0.6,-0.4,-0.2,0,0.2,0.4,0.6]



T1 = "/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/before-learning/before-learning-50%/data/"
T2 = "/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/during-learning/during-learning-50%/data/"
T3 = "/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/after-learning/after-learning-50%/data/"


#####################plot before learning#####################
for ii in [0,1,2]:
    rate = np.load(T1+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T1+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax1.plot(t,rate,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax4.plot(t,conn,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    
    
for ii in [3]:
    rate = np.load(T1+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T1+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax1.plot(t,rate,color=yellow,label=str(elec_field_strens[ii])+"mV")
    ax4.plot(t,conn,color=yellow,label=str(elec_field_strens[ii])+"mV")    


for ii in [4,5,6]:
    rate = np.load(T1+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T1+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax1.plot(t,rate,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax4.plot(t,conn,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV") 
    
    


#####################plot during learning#####################
for ii in [0,1,2]:
    rate = np.load(T2+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T2+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax2.plot(t,rate,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax5.plot(t,conn,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    
    
for ii in [3]:
    rate = np.load(T2+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T2+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax2.plot(t,rate,color=yellow,label="without tDCS")
    ax5.plot(t,conn,color=yellow,label="without tDCS")    


for ii in [4,5,6]:
    rate = np.load(T2+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T2+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax2.plot(t,rate,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax5.plot(t,conn,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV") 
    


#####################plot after learning#####################

for ii in [0,1,2]:
    rate = np.load(T3+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T3+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax3.plot(t,rate,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax6.plot(t,conn,black,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    
    
for ii in [3]:
    rate = np.load(T2+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T2+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax3.plot(t,rate,color=yellow,label=str(elec_field_strens[ii])+"mV")
    ax6.plot(t,conn,color=yellow,label=str(elec_field_strens[ii])+"mV")    


for ii in [4,5,6]:
    rate = np.load(T3+"1000rates1_seed_"+str(ii)+".npy")
    conn = np.load(T3+"1000g1g1_seed_"+str(ii)+".npy")*10.
    ax3.plot(t[0:len(rate)],rate,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV")
    ax6.plot(t[0:len(conn)],conn,red,alpha=alphas[ii],label=str(elec_field_strens[ii])+"mV") 



for ax in [ax1,ax2,ax3]:
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_ylim(1,27)
    ax.set_xlim(700,1600)


for ax in [ax4,ax5,ax6]:
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_ylim(0.04,0.20)
    ax.set_xlim(700,1600)
    

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')
        
for ax in [ax1,ax4]:
    ax.axvspan(750,900,color=DCS_color,alpha=0.2)
    ax.axvspan(900,1050,color=memory_color,alpha=0.2)
    
for ax in [ax2,ax5]:
    ax.axvspan(750,900,color=DCS_color,alpha=0.2)
    ax.axvspan(750,900,color=memory_color,alpha=0.2)
    
for ax in [ax3,ax6]:
    ax.axvspan(750,900,color=memory_color,alpha=0.2)
    ax.axvspan(900,1050,color=DCS_color,alpha=0.2)
    
ax1.set_ylabel("Firing\nrate(Hz)")
ax1.set_yticks(np.arange(0,27,8))
ax1.text(825,22,'DC',fontsize=5,ha='center',va='bottom')
ax1.text(975,22,'ML',fontsize=5,ha='center',va='bottom')
ax2.text(825,22,'DC+ML',fontsize=5,ha='center',va='bottom')
ax3.text(825,22,'ML',fontsize=5,ha='center',va='bottom')
ax3.text(975,22,'DC',fontsize=5,ha='center',va='bottom')
ax4.set_ylabel('$\Gamma_\mathrm{sti}$')
ax4.set_yticks(np.arange(0.04,0.20,0.05))
ax5.set_xlabel("Time (s)")
ax5.set_xticks(np.arange(700,1600,200))
ax2.legend(bbox_to_anchor=(0.2, 0.4, 0.9, 0.5), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)


plt.savefig("/home/hanlu/Desktop/Freiburg/tDCS-and-learning-NEST2.16/Figures/Figure6-g1g2g3/g1g1curves.svg")
plt.show()
