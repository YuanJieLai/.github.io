import matplotlib.pyplot as plt
#算法平均排名
_alg1_=[1.65,2.725,2.025,3.6]
_alg2_=[1.475,2.85,2.35,3.325]
_alg3_=[1.45,3.275,2.7,2.575]
CD=1.048
h_CD=CD/2
y=[1,2,3,4]#alg1,alg2,alg3,alg4
plt.rcParams['font.sans-serif'] = ['SimHei']#正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#正常显示负号
plt.rc('font',family='Times New Roman')
plt.figure(figsize=(24,7.5))
#第一幅图
plt.subplot(131)
plt.scatter(_alg1_,y,s=100,c='black')
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg1_[i]-h_CD,_alg1_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0)
plt.yticks(range(0,6,1),labels=['','TSOA','CB','BOCA','FOGA',''],size=20)
plt.xticks(range(0,5,1),labels=['0','1','2','3','4'],size=20)
plot_x=[]
plot_x.append(_alg1_[0]+h_CD)
plot_x.append(_alg1_[0]+h_CD)
plt.plot(plot_x,[0.5,4.5],color="black",linewidth=2,linestyle='--')
plt.xlabel("Rank",size=20)
plt.title("I$_{T_{1/3}}$",size=20)
#第二幅图
plt.subplot(132)
plt.scatter(_alg2_,y,s=100,c='black')
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg2_[i]-h_CD,_alg2_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0)

plt.yticks(range(0,6,1),labels=['','TSOA','CB','BOCA','FOGA',''],size=20)
plt.xticks(range(0,5,1),labels=['0','1','2','3','4'],size=20)
plot_x=[]
plot_x.append(_alg2_[0]+h_CD)
plot_x.append(_alg2_[0]+h_CD)
plt.plot(plot_x,[0.5,4.5],color="black",linewidth=2,linestyle='--')
plt.xlabel("Rank",size=20)
plt.title("I$_{T_{2/3}}$",size=20)
#第三幅图
plt.subplot(133)
plt.scatter(_alg3_,y,s=100,c='black')
for i in range(len(y)):
    yy=[y[i],y[i]]
    xx=[_alg3_[i]-h_CD,_alg3_[i]+h_CD]
    plt.plot(xx, yy,linewidth=3.0)

plt.yticks(range(0,6,1),labels=['','TSOA','CB','BOCA','FOGA',''],size=20)
plt.xticks(range(0,5,1),labels=['0','1','2','3','4'],size=20)
plot_x=[]
plot_x.append(_alg3_[0]+h_CD)
plot_x.append(_alg3_[0]+h_CD)
plt.plot(plot_x,[0.5,4.5],color="black",linewidth=2,linestyle='--')
plt.xlabel("Rank",size=20)
plt.title("I$_{T_{3/3}}$",size=20)
#plt.savefig('C:/picture/图4(I_T).jpg')
plt.show()