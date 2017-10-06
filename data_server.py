import numpy
from catboost import CatBoostRegressor
from flask import Flask, json, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    dataset = numpy.array([[1, 4, 5, 6], [4, 5, 6, 7], [30, 40, 50, 60], [20, 15, 85, 60]])
    train_labels = [1.2, 3.4, 9.5, 24.5]
    model = CatBoostRegressor(learning_rate=1, depth=6, loss_function='RMSE')
    fit_model = model.fit(dataset, train_labels)

    print(fit_model.get_params())

    return Response(json.dumps(fit_model.get_params()), mimetype="application/json")


if __name__ == '__main__':
    app.run()
