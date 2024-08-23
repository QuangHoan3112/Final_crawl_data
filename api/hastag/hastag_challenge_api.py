import os
import requests
from enum import Enum
from api import logger
from api.hastag.hastag_object import Hastag

def get_challenge_info_by_hashtag(hashtag, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/challenge/{}") -> Hastag:
    url = base_url.format(hashtag)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        challenge_info = Hastag(data)  # Giả sử class ChallengeInfo có thể nhận dữ liệu từ phần 'data' của JSON trả về
        return challenge_info

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None
