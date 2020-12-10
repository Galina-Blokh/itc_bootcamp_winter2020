import pandas as pd
import numpy as np
from flask import Flask, request
import my_model
import json

app = Flask(__name__)



@app.route('/pred_one')
def predict_for_one():
    """ the function gets
    index of instance
    set and model
    to  predict for one instance by it index
    :returns int prediction """
    args = []
    for key in keys:
        args.append(str((request.args.get(key))))
    return str(my_model.predict_one(knn, np.array(args).reshape(1, -1)))


@app.route('/pred', methods=['POST'])
def predict_json():
    """
    predict for any instanses from json request
    :return: predictions: str
    """
    reqs = str(request.data.decode())
    from_json = pd.DataFrame.from_dict(json.loads(reqs))
    answer = knn.predict(from_json)
    return str(answer)


if __name__ == '__main__':
    knn = my_model.load_model()

    X_test = pd.read_csv(my_model.MY_SET)

    keys = X_test.columns

    app.run(debug=True)
