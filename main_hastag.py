import os
from dotenv import load_dotenv
from api.hastag import hastag_challenge_api

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
    hastag_challenge = input("Nhập hastag cần tìm: ")

    challenge_info = hastag_challenge_api.get_challenge_info_by_hashtag(hastag_challenge,headers)
    if challenge_info:
        print("Thông tin Challenge: \n")
        print(challenge_info)
    else:
        print("No challenge info found or API request failed.")