import os
from dotenv import load_dotenv
from api.user import user_api
from api.user import follower_api
from api.user import following_api 

# Load các biến môi trường từ file .env_sample
load_dotenv(dotenv_path='.env_sample')

# Lấy các giá trị từ biến môi trường
rapidapi_key = os.getenv('x-rapidapi-key')
rapidapi_host = os.getenv('x-rapidapi-host')

headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": rapidapi_host
}

if __name__ == '__main__':
    user_name =input("Nhập username của KOL: ")
    user = user_api.get_user_data_by_username(user_name, headers)
    
    if user:
        print(user.__str__())
        user_id = user.uid  # Giả sử uid là user ID cần thiết
        print('Id người dùng là:', user_id)
        # Lấy dữ liệu followers từ follower_api
        followers = follower_api.get_follower_data_by_user_id(user_id, headers)
        
        if followers:
            print("Thông tin của Followers là: ")
            print("\n")
            for follower in followers:
                print(follower)
                print("\n" + "="*40 + "\n")
        else:
            print("No followers found or API request failed.")
        
        # Lấy dữ liệu following từ following_api
        followings = following_api.get_following_data_by_user_id(user_id, headers)
        
        if followings:
            print("Thông tin của Followings là: ")
            print("\n")
            for following in followings:
                print(following)
                print("\n" + "="*40 + "\n")  
        else:
            print("No following found or API request failed.")
    else:
        print("Failed to fetch user data.")
