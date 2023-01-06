import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

def ET (p_dir,np_dir):
    puddle_np_2D = np.load(p_dir)
    puddle_np_2D= puddle_np_2D.reshape(-1,256*256)
    print(puddle_np_2D.shape)
    nonpuddle_np_2D = np.load(np_dir)
    nonpuddle_np_2D=nonpuddle_np_2D.reshape(-1,256*256)
    print(nonpuddle_np_2D.shape)

    training_data = np.concatenate((puddle_np_2D,nonpuddle_np_2D), axis=0)
    training_target = np.array(["P"] * 926 + ["N"] *992)
    print(training_data.shape)

    train_input, test_input, train_target, test_target = train_test_split(training_data, training_target, test_size=0.30, shuffle=True)

    et = ExtraTreesClassifier(n_jobs=-1)
    et.fit(train_input, train_target)
    print(et.score(test_input, test_target))

    answer = et.predict(nonpuddle_np_2D[2].reshape(1,-1))
    if answer[0]=='P':
        return 1
    elif answer[0] == 'N':
        return 0


p_dir = '/Users/kimjuhwan/Desktop/npderivatives/pg2.npy'
np_dir = '/Users/kimjuhwan/Desktop/npderivatives/npg2.npy'

print(ET(p_dir,np_dir))
