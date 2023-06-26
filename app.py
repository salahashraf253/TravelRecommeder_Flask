from flask import Flask, request, jsonify
from Hotels import test_env
from Hotels.test_env import *
# from Restaurants.restaruant_call import recommend_restaraurnat
# from attractions_reccommendation.test_rbm import  recommend_attraction_place
import jsonpickle
app = Flask(__name__)
from Hotels.initial_user_profiling import  user_profile
from Restaurants.restaurants_user_profiling import user_profile_restaurant
from attractions_reccommendation.profiling_new_user import profiling_new_user
from attractions_reccommendation.cosine_sim_attraction import get_recommendations
from Hotels.cosine_similiarity_hotels import get_recommendation
from Restaurants.cosine_sim_restaurants import get_recommendations
@app.route('/api/hello')
def hello_world():
    return 'Hello World!'

@app.route("/hotel/user-profile/<userId>",methods=['POST'])
def add_user_for_hotel(userId):
    assert userId == request.view_args['userId']
    print(request)
    data = request.get_json(force=True)

    print(data)

    # amentaties_list = data.get('amenities', [])
    # lst=[1,5,6,9,8,7,4]

    user_profile(data,userId)
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


## attractions                  #########################
@app.route('/attraction/<userId>/<city>', methods=['GET'])
def attraction_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    city=city.lower()
    # print(userId)
    # print(type(userId))
    df = recommend_attraction_place(int(userId), city)
    return df.tolist()


@app.route("/attraction/user-profile/<userId>",methods=['POST'])
def add_user_for_attraction(userId):
    assert userId == request.view_args['userId']
    data = request.json
    print("Data: ")
    print(data)
    # preferences = data.get('userPreferences', [])
    # lst=[1,5,6,9,8,7,4]

    profiling_new_user(userId , data)
    print("Done----------")
    return ("Done ")


@app.route('/restaurant/<userId>/<city>', methods=['GET'])
def restaurant_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    df = recommend_restaraurnat(userId, city)
    print("Data restaurant: ---------------------------------------------------------------------")
    print(df)
    try:
        return df.tolist()
    except:
        return df



@app.route("/restaurant/user-profile/<userId>",methods=['POST'])
def add_user_for_restaurant(userId):
    assert userId == request.view_args['userId']
    data = request.json
    # cuisines_list = data.get('cuisines', [])

    user_profile_restaurant(data,userId)
    print("Done----------")
    return ("Done ")



# COSINE SIMILARITY
@app.route('/attraction/cosine/<int:attraction_id>', methods=['GET'])
def attraction_recommednation_cosine(attraction_id):
    assert attraction_id == request.view_args['attraction_id']
    # print(type(userId))
    df = get_recommendations(attraction_id)
    return df


@app.route('/hotel/cosine/<int:hotel_id>', methods=['GET'])
def hotel_recommednation_cosine(hotel_id):
    assert hotel_id == request.view_args['hotel_id']
    # print(type(userId))
    df = get_recommendation(hotel_id)
    return df

@app.route('/restaurant/cosine/<int:restaurant_id>', methods=['GET'])
def restaurant_recommednation_cosine(restaurant_id):
    assert restaurant_id == request.view_args['restaurant_id']
    # print(type(userId))
    df = get_recommendations(restaurant_id)
    return df

from Plan.planMultipleDays import plan_multiple_days

@app.route('/recommend/plan/<userId>/<city>', methods=['POST'])
def plan_recommednation(userId,city):
    assert userId == request.view_args['userId']
    assert city == request.view_args['city']
    data = request.get_json()
    start_time = data.get('startTime', str)
    end_time = data.get('endTime', str)
    long = data.get('longitude', float)
    lat = data.get('latitude', float)
    no_days=data.get('noOfDays',int)
    # print(plan_multiple_days(no_days, city,(lat,long),userId, start_time, end_time))
    print("=============================================================")
    return jsonify(plan_multiple_days(no_days, city,(lat,long),userId, start_time, end_time))


if __name__ == '__main__':
    app.run(port=5000)
    # app.config["SPARK_MASTER_URL"] = "local[*]"
    # app.run(debug=True,host='0.0.0.0')


