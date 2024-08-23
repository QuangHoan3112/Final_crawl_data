import os
from dotenv import load_dotenv
from api.music import music_api

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
    music_id = input("Nhập id music cần tìm: ")

    music = music_api.get_music_info_by_music_id(music_id,headers)
    if music:
        print(music.__str__())
    else:
        print("No music info found or API request failed.")