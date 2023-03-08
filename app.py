from flask import Flask, request

app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    return 'Hello World!'


@app.route('/hotel', methods=['POST'])
def hotel_recommednation():
    print(request.get_json())
    return "Hotel Recommender"


if __name__ == '__main__':
    app.run(port=5000)
