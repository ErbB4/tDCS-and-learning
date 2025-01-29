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




################### plot bar1 ###################
fig = plt.figure(figsize=(cm2inch(2), cm2inch(3)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.99,bottom=0.15,left=0.15,right=0.95,hspace=0.1,wspace=0.25)
ax1 = plt.subplot(gs1[0,0])
        
ax1.bar(1,2.8,width=0.5,color=DCS_color,alpha=0.2)
ax1.bar(2,1.5,width=0.5,color=memory_color,alpha=0.2)


ax1.set_xlim(0,3)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xticks([1,2])
ax1.set_xticklabels(["DC","ML"])
ax1.set_yticks(())

plt.savefig("bar1.svg")

################### plot bar2 ###################
fig = plt.figure(figsize=(cm2inch(2), cm2inch(3)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.99,bottom=0.15,left=0.15,right=0.95,hspace=0.1,wspace=0.25)
ax1 = plt.subplot(gs1[0,0])
        
ax1.bar(1,1.5,width=0.5,color=memory_color,alpha=0.2)
ax1.bar(2,2.8,width=0.5,color=DCS_color,alpha=0.2)


ax1.set_xlim(0,3)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_xticks([1,2])
ax1.set_xticklabels(["ML","DC"])
ax1.set_yticks(())
plt.savefig("bar2.svg")


plt.show()
