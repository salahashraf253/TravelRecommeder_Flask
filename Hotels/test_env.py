from Hotels.Hotels_MF_ALS import *
import pandas as pd

#TEST CODE FOR HOTELS
csvHotelInfo = "Hotels/Allhotels.csv"
csvRatingInfo = 'Hotels/user_profiling.csv'

newUser = []

newUser.append(
               {
                   'user_id': 2709,
                   'hotel_id':3,
                   'rating': 5,
                   'flag': 'F',
                   'city':'Cairo'

               })
pd.DataFrame(newUser).to_csv('Hotels/user_profile_Data/user_profiling_AlFay.csv', index=False, mode='a', header=False)
#when entering a new user we do have to retrain the entire model
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)

# recommendations(best_model,1,hotels,'Al-Fayyum')


def recommend_hotel(user_id, city):
    csvHotelInfo = "Hotels/Allhotels.csv"
    csvRatingInfo = 'Hotels/user_profiling.csv'

    # pd.DataFrame(newUser).to_csv('Hotels/user_profile_Data/user_profiling_AlFay.csv', index=False, mode='a',
    #                              header=False)
    # when entering a new user we do have to retrain the entire model
    ratingsSpark, hotels = initial_files(csvHotelInfo, csvRatingInfo)
    calculateSparsity(ratingsSpark)
    train, test = dataSplit(ratingsSpark)
    best_model = MF_ALS(train, test)
    # df=pd.DataFrame(recommendations(best_model,user_id,hotels,city))
    # arr=df.to_numpy()
    return recommendations(best_model,user_id,hotels,city)
#TEST CODE FOR RESTAURANTS

#TEST CODE FOR ATTRACTIONS