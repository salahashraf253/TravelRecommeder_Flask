from flask import Flask, request
from Hotels import test_env
from Hotels.test_env import *
# from Restaurants.restaruant_call import recommend_restaraurnat
# from attractions_reccommendation.test_rbm import  recommend_attraction_place
import jsonpickle
app = Flask(__name__)
from Hotels.initial_user_profiling import  user_profile
from Restaurants.restaurants_user_profiling import user_profile_restaurant

@app.route('/api/hello')
def hello_world():
    return 'Hello World!'

@app.route("/hotel/user-profile/<userId>",methods=['POST'])
def add_user_for_hotel(userId):
    assert userId == request.view_args['userId']
    print(request)
    data = request.get_json(force=True)

    print(data)

    amentaties_list = data.get('amenities', [])
    # lst=[1,5,6,9,8,7,4]

    user_profile(amentaties_list,userId)
    print("Done----------")
    return ("Done ")

@app.route("/restaurant/user-profile/<userId>",methods=['POST'])
def add_user_for_restaurant(userId):
    assert userId == request.view_args['userId']
    data = request.json
    cuisines_list = data.get('cuisines', [])
    # lst=[1,5,6,9,8,7,4]

    user_profile_restaurant(cuisines_list,userId)
    print("Done----------")
    return ("Done ")



@app.route('/hotel/<userId>/<city>', methods=['GET'])
def hotel_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    df = recommend_hotel(userId, city)
    # print("=============================================================")
    # print("Type of output: "+str(type(df)))
    return df



@app.route('/attraction/<userId>/<city>', methods=['GET'])
def attraction_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    city=city.lower()
    print(userId)
    print(type(userId))
    df = recommend_attraction_place(int(userId), city)
    return df.tolist()
#
#
@app.route('/restaurant/<userId>/<city>', methods=['GET'])
def restaurant_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    df = recommend_restaraurnat(userId, city)
    print(df)
    return df


@app.route("/attraction/user-profile/<userId>",methods=['POST'])
def add_user_for_attraction(userId):
    assert userId == request.view_args['userId']
    data = request.json
    cuisines_list = data.get('cuisines', [])
    # lst=[1,5,6,9,8,7,4]

    user_profile_restaurant(cuisines_list,userId)
    print("Done----------")
    return ("Done ")









if __name__ == '__main__':
    app.run(port=5000)


