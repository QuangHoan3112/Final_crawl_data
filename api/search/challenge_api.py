import os
import requests
from typing import List
from enum import Enum
from api import logger

# Sửa đổi import để không gây lỗi import
from api.search.search_object import ChallengeData 

def get_challenge_info_by_keyword(keyword, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/search/challenge/{}") -> List['ChallengeData']:
    url = base_url.format(keyword)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        challenges = [ChallengeData(challenge_data) for challenge_data in data['data']['challenge_list']]
        return challenges

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None