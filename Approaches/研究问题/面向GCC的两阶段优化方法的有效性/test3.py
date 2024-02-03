import matplotlib.pyplot as plt

_alg1_=[1,2]

#CD=0.438
CD=0.876
h_CD=CD/2
y=[1,3]#alg1,alg2,alg3,alg4
plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#正常显示负号
plt.rc('font',family='Times New Roman')
plt.figure(figsize=(10,8))
#plt.suptitle('My Figure',fontsize=36)
plt.scatter(_alg1_,y,s=100,c='black')
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg1_[i]-h_CD,_alg1_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0)

plt.yticks(range(1,4,2),labels=['OSEA',r'OSEA$\regular^{-nsg}$'],fontfamily='Times New Roman',size=20)
plt.xticks(range(0,5,1),labels=['0','1','2','3','4'],size=20)
plot_x=[]
plot_x.append(_alg1_[0]+h_CD)
plot_x.append(_alg1_[0]+h_CD)
plt.plot(plot_x,[0.5,4.5],color="black",linewidth=2,linestyle='--')
plt.xlabel("Rank",size=20)
plt.savefig('C:/picture/OSEA和OSEA-nsg.jpg')
plt.show()