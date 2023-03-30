from flask import Flask, request
from Hotels import test_env
from Hotels.test_env import recommend_hotel
import jsonpickle
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    return 'Hello World!'


@app.route('/hotel/<userId>/<city>', methods=['POST'])
def hotel_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    df = recommend_hotel(userId, city)
    print(df)
    return df

if __name__ == '__main__':
    app.run(port=5000)


