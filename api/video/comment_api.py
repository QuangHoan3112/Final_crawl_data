import os
from typing import List
import requests
from enum import Enum
from api import logger
from api.video.video_object import Comment

def get_comment_by_id(video_id, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/comments/{}") -> List[Comment]:
    url = base_url.format(video_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        comments = [Comment(comment_data) for comment_data in data['data']['comments']]
        return comments
    except requests.exceptions.RequestException as err:
        logger.info(f"API request failed for video {video_id} with error: {err}")
    except Exception as err:
        logger.info(f"An unexpected error occurred: {err}")
    return None
