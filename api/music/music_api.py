import os
import requests
from enum import Enum
from api import logger
from api.music.music_object import Music  

def get_music_info_by_music_id(music_id, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/music/{}") -> Music:
    url = base_url.format(music_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        music_info = Music(data['data']['music_info'])  # Giả sử class Music có thể nhận dữ liệu từ phần 'data' của JSON trả về
        return music_info

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None