import os
import requests
from enum import Enum
from api import logger
from typing import List
from api.search.search_object import User
from api.search.search_object import HeaderInfo


def header_info(keyword, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/search/user/{}") -> HeaderInfo:
    url = base_url.format(keyword)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        # status 200 OK 

        data = response.json()
        header = HeaderInfo(data)
        return header
    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None



def get_user_info_by_keyword(keyword, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/search/user/{}") -> List[User]:
    url = base_url.format(keyword)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        # status 200 OK 

        data = response.json()
        user_list_data = data['data']['user_list']
        users = [User(user_data['user_info']) for user_data in user_list_data] 
        return users

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None