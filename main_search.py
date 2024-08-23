import os
from dotenv import load_dotenv
from api.search import challenge_api, user_data_api

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
    key_word = input("Nhập keyword cần tìm: ")
    challenge_list = challenge_api.get_challenge_info_by_keyword(key_word, headers)
   

    if challenge_list:
        print("Thông tin về Challenge: \n")
        for challenge in challenge_list:
           print(challenge)
    else:
        print("Failed to fetch challenge data.")

    user_info = user_data_api.get_user_info_by_keyword(key_word, headers)
    header = user_data_api.header_info(key_word, headers)

    if header:
        print(header)
        if user_info:
             for user in user_info:
                 print(user)
    else:
        print("Failed to fetch user data.")
