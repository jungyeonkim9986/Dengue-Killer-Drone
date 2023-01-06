from sklearn.cluster import KMeans
import numpy as np
import sklearn
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
import random
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import ExtraTreesClassifier

puddle_np_2D = np.load('/Users/kimjuhwan/Desktop/npderivatives/pg2.npy')
# print(puddle_np_2D.shape)
puddle_np_2D= puddle_np_2D.reshape(-1,256*256)
print(puddle_np_2D.shape)
nonpuddle_np_2D = np.load('/Users/kimjuhwan/Desktop/npderivatives/npg2.npy')
# print(nonpuddle_np_2D.shape)
nonpuddle_np_2D=nonpuddle_np_2D.reshape(-1,256*256)
print(nonpuddle_np_2D.shape)


training_data = np.concatenate((puddle_np_2D,nonpuddle_np_2D), axis=0)
training_target = np.array(["P"] * 926 + ["N"] *992 )
print(training_data.shape)

train_input, test_input, train_target, test_target = train_test_split(training_data, training_target, test_size=0.10, shuffle=True)

# ss = StandardScaler()
# ss.fit(train_input)
#
# train_scaled = ss.transform(train_input)
# test_scaled = ss.transform(test_input)

et = ExtraTreesClassifier(n_jobs=-1)
et.fit(train_input, train_target)
print(et.score(test_input, test_target))

print(et.predict(nonpuddle_np_2D[5].reshape(1,-1))) # 하나의 이미지 파일도 구분 가능! 
