from scipy.stats import wilcoxon
import numpy as np
from math import sqrt




# 两个样本的数据
sample1 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
sample2 = [0.868421052631579, 0.7982456140350876, 0.8333333333333333, 0.8245614035087719, 0.9035087719298246, 0.8333333333333333, 0.8333333333333333, 0.763157894736842, 0.8245614035087719, 0.7807017543859649]

sample1 = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
sample2 = [0.9305555555555556, 0.9027777777777778, 0.9444444444444444, 0.9027777777777778, 0.9583333333333334, 0.9305555555555556, 0.9722222222222222, 0.8750000000000001, 0.8333333333333334, 0.888888888888889]

for i in range(len(sample1)):
    sample1[i]=sample1[i]*1000
    sample2[i]=sample2[i]*1000



wilcoxon_result = wilcoxon(sample1, sample2)
p_value = wilcoxon_result.pvalue
effect_size = wilcoxon_result.statistic / (len(sample1) * len(sample2))

# 输出结果
print("p-value:", p_value)
# 计算样本差异的平均值
mean_diff = sum(np.array(sample1) - np.array(sample2)) / len(sample1)
# 计算样本差异的标准差
var_diff = sum((np.array(sample1) - np.array(sample2) - mean_diff) ** 2) / (len(sample1) - 1)
std_diff = sqrt(var_diff)

# 计算Cohen's d效应值
cohens_d = mean_diff / std_diff
print("Cohen's d效应值为：", cohens_d)

