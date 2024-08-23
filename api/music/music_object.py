import json

# Định nghĩa các lớp
class LabelTop:
    def __init__(self, data:dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else -1
        self.height = data['height'] if 'height' in data else -1

    def __str__(self) -> str:
        urls = "\n".join(self.url_list)  # Join each URL with a newline
        return (
            f"URI: {self.uri}\n"
            f"URL List:\n{urls}\n"  # Print URL list with each URL on a new line
            f"Width: {self.width}\n"
            f"Height: {self.height}\n"
        )

class ShareInfo:
    def __init__(self, data:dict) -> None:
        self.share_url = data['share_url'] if 'share_url' in data else None
        self.share_desc = data['share_desc'] if 'share_desc' in data else None
        self.share_title = data['share_title'] if 'share_title' in data else None
        self.share_desc_info = data['share_desc_info'] if 'share_desc_info' in data else None

    def __str__(self) -> str:
        return (
            f"Share URL: {self.share_url}\n"
            f"Share Desc: {self.share_desc}\n"
            f"Share Title: {self.share_title}\n"
            f"Share Desc Info: {self.share_desc_info}\n"
        )

class Music:
    def __init__(self, data:dict) -> None:
        self.id = data['id'] if 'id' in data else -1
        self.id_str = data['id_str'] if 'id_str' in data else None
        self.title = data['title'] if 'title' in data else None
        self.author = data['author'] if 'author' in data else None
        self.album = data['album'] if 'album' in data else None
        self.cover_large = LabelTop(data['cover_large']) if 'cover_large' in data else LabelTop({})
        self.cover_medium = LabelTop(data['cover_medium']) if 'cover_medium' in data else LabelTop({})
        self.cover_thumb = LabelTop(data['cover_thumb']) if 'cover_thumb' in data else LabelTop({})
        self.play_url = LabelTop(data['play_url']) if 'play_url' in data else LabelTop({})
        self.source_platform = data['source_platform'] if 'source_platform' in data else None
        self.duration = data['duration'] if 'duration' in data else -1
        self.extra = json.loads(data['extra']) if 'extra' in data else {}
        self.user_count = data['user_count'] if 'user_count' in data else -1
        self.share_info = ShareInfo(data['share_info']) if 'share_info' in data else ShareInfo({})
        self.status = data['status'] if 'status' in data else -1
        self.owner_id = data['owner_id'] if 'owner_id' in data else -1
        self.owner_nickname = data['owner_nickname'] if 'owner_nickname' in data else None
        self.is_original = data['is_original'] if 'is_original' in data else None
        self.mid = data['mid'] if 'mid' in data else -1
        self.owner_handle = data['owner_handle'] if 'owner_handle' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None
        self.avatar_thumb = LabelTop(data['avatar_thumb']) if 'avatar_thumb' in data else LabelTop({})
        self.avatar_medium = LabelTop(data['avatar_medium']) if 'avatar_medium' in data else LabelTop({})
        self.preview_start_time = data['preview_start_time'] if 'preview_start_time' in data else -1
        self.preview_end_time = data['preview_end_time'] if 'preview_end_time' in data else -1
        self.is_commerce_music = data['is_commerce_music'] if 'is_commerce_music' in data else None
        self.is_original_sound = data['is_original_sound'] if 'is_original_sound' in data else None
        self.audition_duration = data['audition_duration'] if 'audition_duration' in data else -1
        self.shoot_duration = data['shoot_duration'] if 'shoot_duration' in data else -1
        self.is_allow_shoot = data['is_allow_shoot'] if 'is_allow_shoot' in data else -1
        self.is_author_artist = data['is_author_artist'] if 'is_author_artist' in data else -1
        self.matched_song = data['matched_song'] if 'matched_song' in data else {}
        self.video_duration = data['video_duration'] if 'video_duration' in data else -1
        self.aweme_type = data['aweme_type'] if 'aweme_type' in data else -1
        self.msg = data['msg'] if 'msg' in data else None
        self.rec_list = data['rec_list'] if 'rec_list' in data else None
        self.similar_music = data['similar_music'] if 'similar_music' in data else None
        self.similar_music_ids = data['similar_music_ids'] if 'similar_music_ids' in data else None

    def __str__(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"ID Str: {self.id_str}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Album: {self.album}\n"
            f"Cover Large: {self.cover_large}\n"
            f"Cover Medium: {self.cover_medium}\n"
            f"Cover Thumb: {self.cover_thumb}\n"
            f"Play URL: {self.play_url}\n"
            f"Source Platform: {self.source_platform}\n"
            f"Duration: {self.duration}\n"
            f"Extra: {self.extra}\n"
            f"User Count: {self.user_count}\n"
            f"Share Info: {self.share_info}\n"
            f"Status: {self.status}\n"
            f"Owner ID: {self.owner_id}\n"
            f"Owner Nickname: {self.owner_nickname}\n"
            f"Is Original: {self.is_original}\n"
            f"MID: {self.mid}\n"
            f"Owner Handle: {self.owner_handle}\n"
            f"Sec UID: {self.sec_uid}\n"
            f"Avatar Thumb: {self.avatar_thumb}\n"
            f"Avatar Medium: {self.avatar_medium}\n"
            f"Preview Start Time: {self.preview_start_time}\n"
            f"Preview End Time: {self.preview_end_time}\n"
            f"Is Commerce Music: {self.is_commerce_music}\n"
            f"Is Original Sound: {self.is_original_sound}\n"
            f"Audition Duration: {self.audition_duration}\n"
            f"Shoot Duration: {self.shoot_duration}\n"
            f"Is Allow Shoot: {self.is_allow_shoot}\n"
            f"Is Author Artist: {self.is_author_artist}\n"
            f"Matched Song: {self.matched_song}\n"
            f"Video Duration: {self.video_duration}\n"
            f"Aweme Type: {self.aweme_type}\n"
            f"MSG : {self.msg}\n"
            f"Rec list: {self.rec_list}\n"
            f"Similar music: {self.similar_music}\n"
            f"Similar music ids: {self.similar_music_ids}\n"
        )