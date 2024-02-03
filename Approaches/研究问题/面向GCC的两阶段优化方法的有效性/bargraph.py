import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10,8))
plt.rc('font',family='Times New Roman')
# 构造x轴刻度标签、数据
labels = ['I$_{Q_{1/3}}$', 'I$_{Q_{2/3}}$', 'I$_{Q_{3/3}}$', ]
first = [1,2,4]
second = [6,7,6]
third = [5,2,0]
fourth = [8,9,10]
# 四组数据
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 1.5*width, first, width, label='FOGA')
plt.bar(x - 0.5*width, second, width, label='BOCA')
plt.bar(x + 0.5*width, third, width, label='CB')
plt.bar(x + 1.5*width, fourth, width, label='TSOA')
plt.ylabel('The count of problem instances',size=20)
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels,size=20)

plt.legend()
#plt.savefig('C:/picture/图七.jpg')
plt.show()

