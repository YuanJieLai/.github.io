# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:48:15 2022

@author: Administrator
"""
import matplotlib.pyplot as plt
# #30m
# _alg_b=[2.857,6.000,3.000,3.405,3.095,2.643]
# _alg_a=[3.000,6.000,2.571,4.714,2.714,2.000]
# _alg_w=[2.929,6.000,2.881,4.810,2.262,2.119]
# #2h
# _alg_b=[2.976,6.000,3.071,3.238,2.881,2.833]
# _alg_a=[3.381,6.000,2.714,4.619,2.310,1.976]
# _alg_w=[3.310,6.000,2.690,4.762,2.238,2.000]
#30m
_alg_b=[2.857,6.000,3.000,3.405,3.095,2.643]
_alg_a=[3.071,6.000,2.762,4.714,2.857,1.595]
_alg_w=[3.024,6.000,2.929,4.810,2.500,1.738]
#2h
_alg_b=[2.976,6.000,3.071,3.238,2.881,2.833]
_alg_a=[3.381,6.000,2.810,4.619,2.405,1.786]
_alg_w=[3.357,6.000,2.714,4.762,2.357,1.810]



strr='w'
# strt='30m'
strt='2h'
if strr=='b':
    _alg_=_alg_b
    filename='BPD'+strt
elif strr=='a':
    _alg_=_alg_a
    filename='APD'+strt
else:
    _alg_=_alg_w
    filename='WPD'+strt
tit=strt
# y=[1,2,3,4,5,6]#PTWO(本文)	FPBS-QAP	PACO-DM	BMA	EGATS	KMM	BLS	GHA	DBA
# y=[1,2,3,4]
y=[1,2,3,4,5,6]
CD=1.645
h_CD=CD/2
plt.figure(figsize=(10,6))
plt.scatter(_alg_,y,s=100,c='black')
clo=['b','peru','lime','aqua','fuchsia','r']
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg_[i]-h_CD,_alg_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0,color=clo[i])

plt.grid(False)
# plt.yticks(range(0,10,1),labels=['','FPBS-QAP','PACO_DM','BMA','PTWO(ours)','EGATS','KMM','GHA','DBA',''],size=20)
plt.yticks(range(0,7,1),labels=['','FPBS-QAP','PACO-DM','BMA','EGATS','GHA','PTWO'],size=20)
# plt.yticks(range(0,8,1),labels=['','PTWO-C1','PTWO-C2','PTWO-C3','PTWO-C4','PTWO-C5','PTWO(ours)',''],size=20)
plt.xticks(range(0,7,1),labels=['0','1','2','3','4','5','6'],size=20)

plt.ylim(0.3,6.6)
plt.xlabel("Rank",size=20)

plt.title(tit,size=25)

# fig, ax = plt.subplots(1, 1)

x_l=[_alg_[-1]-h_CD,_alg_[-1]+h_CD]
plt.vlines(x_l, 0, 7, linestyles='dashed', colors='r')

# plt.savefig('figs/5_1_'+filename+'.eps',format='eps',dpi=500,bbox_inches='tight', pad_inches = +0.1)

plt.show()