import os
from dotenv import load_dotenv
from api.video import comment_api

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
    video_id = input("Nhập ID video cần tìm: ")

    comments = comment_api.get_comment_by_id(video_id,headers)
    if comments:
        for comment in comments:
            print(comment)
            print("\n" + "="*40 + "\n")
    else:
        print("No comment found or API request failed.")

    