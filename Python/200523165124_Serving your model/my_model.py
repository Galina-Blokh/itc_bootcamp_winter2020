import pickle
import pandas as pd
import numpy as np

FILEPATH = 'my_knn_model.pkl'
MY_SET = 'my_Test_set.csv'


def load_model(filepath=FILEPATH):
    """the func gets .pkl file path
    :returns  model"""
    with open(filepath, 'rb') as f:
        model = pickle.load(f)
    return model


def predict_all(knn, data_set):
    """
    make a prediction for whole X_test
    :param knn: model classifier
    :param data_set: X_test set
    :return: list of predictions
    """
    return list(knn.predict(data_set))


def predict_one(mod, instance):
    """
    make a prediction for one instance
    :param mod: model classifier
    :param instance: X_test 1 row
    :return: prediction str(int)
    """
    return str(int(mod.predict(instance)))


if __name__ == '__main__':

    knn = load_model()
    X_test = pd.read_csv(MY_SET)
    instance10 = X_test[10:11].to_numpy()

    keys = X_test.columns

    # print one instance
    predict_one(knn, instance10)
    print(predict_one(knn, instance10))

    # print random 10 instances
    ans = []
    for indx in np.random.randint(0, len(X_test), 10):
        ans.append(predict_one(knn, X_test[indx:indx + 1].to_numpy()))
    print(ans)

    #print whole X_test predict
    print(predict_all(knn, X_test))
