import matplotlib.pyplot as plt

#算法平均排名
_alg_=[1.7,3.4,2.6,2.3]

y=[1,2,3,4]#alg1,alg2,alg3,alg4
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rc('font',family='Times New Roman')
CD=1.048
h_CD=CD/2
plt.figure(figsize=(10,8))
plt.scatter(_alg_,y,s=100,c='black')
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg_[i]-h_CD,_alg_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0)


plt.yticks(range(0,6,1),labels=['','TSOAGOS','CB','FOGA','BOCA',''],size=20)
plt.xticks(range(0,5,1),labels=['0','1','2','3','4'],size=20)


plot_x=[]
plot_x.append(_alg_[0]+h_CD)
plot_x.append(_alg_[0]+h_CD)
plt.plot(plot_x,[0.5,4.5],color="black",linewidth=2,linestyle='--')


plt.xlabel("Rank",size=20)
plt.savefig('C:/picture/DS3.png',bbox_inches = 'tight',)
#plt.title("Friedman和Nemenyi检验图",size=20)



plt.show()
