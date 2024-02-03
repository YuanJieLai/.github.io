import matplotlib.pyplot as plt
import numpy as np

y = np.array([5, 15,25, 40])

plt.rcParams['font.sans-serif'] = ['fangsong'] #指定字体为雅黑，解决文字乱码问题

plt.rcParams['figure.figsize'] = (3.0, 3.0)
plt.rcParams['font.size'] = '14' # 设置字体大小 = '16' # 设置字体大小
plt.pie(y,
       # 设置饼图标签

        colors=("r", (1, 0, 1), "#88c999", (1, 1, 0)),explode=[0.01, 0.01, 0.01, 0.01])

plt.show()

