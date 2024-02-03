#导包
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_blobs
from sklearn.model_selection import cross_val_score

##创建100个类共10000个样本，每个样本10个特征,10维
X, y = make_blobs(n_samples=10000, n_features=10, centers=100,random_state=0)

## 随机森林
clf2 = RandomForestClassifier(n_estimators=10, random_state=0)
clf2.fit(X,y)
# scores2 = cross_val_score(clf2, X, y)
print(clf2.predict(X))
# print(scores2.mean())

'''
n_estimators:树的个数
max_depth：树的最大深度，为None则直到所有的叶子节点都是同一类样本，或者达到最小样本划分结束
min_samples_split：最小样本划分的数目，就是样本的数目少于等于这个值，就不能继续划分当前节点了
random_state：理解成随机数
'''