import json
class AvatarThumb:
    def __init__(self, data: dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self) -> str:
        return (
            f"  URI: {self.uri}\n"
            f"  URL List: {', '.join(self.url_list) if self.url_list else 'None'}\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
        )

class VideoIcon:
    def __init__(self, data: dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self) -> str:
        return (
            f"  URI: {self.uri}\n"
            f"  URL List: {', '.join(self.url_list) if self.url_list else 'None'}\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
        )

class User:
    def __init__(self, data: dict) -> None:
        self.avatar_thumb = AvatarThumb(data['avatar_thumb']) if 'avatar_thumb' in data else None
        self.avatar_uri = data['avatar_uri'] if 'avatar_uri' in data else None
        self.language = data['language'] if 'language' in data else None
        self.nickname = data['nickname'] if 'nickname' in data else None
        self.region = data['region'] if 'region' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None
        self.short_id = data['short_id'] if 'short_id' in data else None
        self.signature = data['signature'] if 'signature' in data else None
        self.uid = data['uid'] if 'uid' in data else None
        self.unique_id = data['unique_id'] if 'unique_id' in data else None
        self.unique_id_modify_time = data['unique_id_modify_time'] if 'unique_id_modify_time' in data else None
        self.user_mode = data['user_mode'] if 'user_mode' in data else None
        self.user_rate = data['user_rate'] if 'user_rate' in data else None
        self.video_icon = VideoIcon(data['video_icon']) if 'video_icon' in data else None

class Comment:
    def __init__(self, data: dict) -> None:
        self.aweme_id = data['aweme_id'] if 'aweme_id' in data else None
        self.cid = data['cid'] if 'cid' in data else None
        self.create_time = data['create_time'] if 'create_time' in data else None
        self.digg_count = data['digg_count'] if 'digg_count' in data else None
        self.reply_id = data['reply_id'] if 'reply_id' in data else None
        self.reply_to_reply_id = data['reply_to_reply_id'] if 'reply_to_reply_id' in data else None
        self.text = data['text'] if 'text' in data else None
        self.text_extra = data['text_extra'] if 'text_extra' in data else []
        self.user = User(data['user']) if 'user' in data else None

    def __str__(self) -> str:
        user_info = (
            f"- Avatar Thumb:\n{self.user.avatar_thumb if self.user and self.user.avatar_thumb else 'None'}\n"
            f"  Avatar URI: {self.user.avatar_uri if self.user else 'None'}\n"
            f"  Nickname: {self.user.nickname if self.user else 'None'}\n"
            f"  Region: {self.user.region if self.user else 'None'}\n"
            f"  Sec UID: {self.user.sec_uid if self.user else 'None'}\n"
            f"  Short ID: {self.user.short_id if self.user else 'None'}\n"
            f"  Signature: {self.user.signature if self.user else 'None'}\n"
            f"  UID: {self.user.uid if self.user else 'None'}\n"
            f"  Unique ID: {self.user.unique_id if self.user else 'None'}\n"
            f"  Unique ID Modify Time: {self.user.unique_id_modify_time if self.user else 'None'}\n"
            f"  User Mode: {self.user.user_mode if self.user else 'None'}\n"
            f"  User Rate: {self.user.user_rate if self.user else 'None'}\n"
            f"- Video Icon:\n{self.user.video_icon if self.user and self.user.video_icon else 'None'}\n"
        )
        return (
            f"Comment:\n"
            f"  Aweme ID: {self.aweme_id}\n"
            f"  CID: {self.cid}\n"
            f"  Create Time: {self.create_time}\n"
            f"  Digg Count: {self.digg_count}\n"
            f"  Reply ID: {self.reply_id}\n"
            f"  Reply to Reply ID: {self.reply_to_reply_id}\n"
            f"  Text: {self.text}\n"
            f"\n"
            f"User Info: \n"
            f"{user_info}"
        )


class ReviewResult:
    def __init__(self, data: dict) -> None:
        self.review_status = data['review_status'] if 'review_status' in data else None

    def __str__(self) -> str:
        return (
            f"  Review Status: {self.review_status}\n"
        )


#Class liên quan tới Video Details
class VideoMute:
    def __init__(self, data: dict) -> None:
        self.is_mute = data['is_mute'] if 'is_mute' in data else False
        self.mute_desc = data['mute_desc'] if 'mute_desc' in data else ''

    def __str__(self) -> str:
        return (
            f"  Is Mute: {self.is_mute}\n"
            f"  Mute Description: {self.mute_desc}\n"
        )

class Status:
    def __init__(self, data: dict) -> None:
        self.aweme_id = data['aweme_id'] if 'aweme_id' in data else None
        self.is_delete = data['is_delete'] if 'is_delete' in data else False
        self.allow_share = data['allow_share'] if 'allow_share' in data else True
        self.allow_comment = data['allow_comment'] if 'allow_comment' in data else True
        self.private_status = data['private_status'] if 'private_status' in data else 0
        self.in_reviewing = data['in_reviewing'] if 'in_reviewing' in data else False
        self.reviewed = data['reviewed'] if 'reviewed' in data else 1
        self.self_see = data['self_see'] if 'self_see' in data else False
        self.is_prohibited = data['is_prohibited'] if 'is_prohibited' in data else False
        self.download_status = data['download_status'] if 'download_status' in data else 0
        self.review_result = ReviewResult(data['review_result']) if 'review_result' in data else ReviewResult({})
        self.video_mute = VideoMute(data['video_mute']) if 'video_mute' in data else VideoMute({})

    def __str__(self) -> str:
        return (
            f"Status:\n"
            f"  Aweme ID: {self.aweme_id}\n"
            f"  Is Delete: {self.is_delete}\n"
            f"  Allow Share: {self.allow_share}\n"
            f"  Allow Comment: {self.allow_comment}\n"
            f"  Private Status: {self.private_status}\n"
            f"  In Reviewing: {self.in_reviewing}\n"
            f"  Reviewed: {self.reviewed}\n"
            f"  Self See: {self.self_see}\n"
            f"  Is Prohibited: {self.is_prohibited}\n"
            f"  Download Status: {self.download_status}\n"
            f"{self.review_result}"
            f"{self.video_mute}"
        )


class CoverImage:
    def __init__(self, data: dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self) -> str:
        return (
            f"  URI: {self.uri}\n"
            f"  URL List: {', '.join(self.url_list)}\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
        )

class PlayUrl:
    def __init__(self, data: dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self) -> str:
        return (
            f"  URI: {self.uri}\n"
            f"  URL List: {', '.join(self.url_list)}\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
        )

class Music:
    def __init__(self, data: dict) -> None:
        self.id = data['id'] if 'id' in data else None
        self.id_str = data['id_str'] if 'id_str' in data else None
        self.title = data['title'] if 'title' in data else None
        self.author = data['author'] if 'author' in data else None
        self.album = data['album'] if 'album' in data else ''
        self.cover_large = CoverImage(data['cover_large']) if 'cover_large' in data else CoverImage({})
        self.cover_medium = CoverImage(data['cover_medium']) if 'cover_medium' in data else CoverImage({})
        self.cover_thumb = CoverImage(data['cover_thumb']) if 'cover_thumb' in data else CoverImage({})
        self.play_url = PlayUrl(data['play_url']) if 'play_url' in data else PlayUrl({})
        self.source_platform = data['source_platform'] if 'source_platform' in data else None
        self.duration = data['duration'] if 'duration' in data else None
        self.extra = data['extra'] if 'extra' in data else ''
        self.user_count = data['user_count'] if 'user_count' in data else 0
        self.status = data['status'] if 'status' in data else None
        self.owner_id = data['owner_id'] if 'owner_id' in data else None
        self.owner_nickname = data['owner_nickname'] if 'owner_nickname' in data else None
        self.is_original = data['is_original'] if 'is_original' in data else False
        self.mid = data['mid'] if 'mid' in data else None
        self.owner_handle = data['owner_handle'] if 'owner_handle' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None
        self.avatar_thumb = CoverImage(data['avatar_thumb']) if 'avatar_thumb' in data else CoverImage({})
        self.avatar_medium = CoverImage(data['avatar_medium']) if 'avatar_medium' in data else CoverImage({})
        self.preview_start_time = data['preview_start_time'] if 'preview_start_time' in data else None
        self.preview_end_time = data['preview_end_time'] if 'preview_end_time' in data else None
        self.is_commerce_music = data['is_commerce_music'] if 'is_commerce_music' in data else False
        self.is_original_sound = data['is_original_sound'] if 'is_original_sound' in data else False
        self.audition_duration = data['audition_duration'] if 'audition_duration' in data else None
        self.shoot_duration = data['shoot_duration'] if 'shoot_duration' in data else None
        self.is_author_artist = data['is_author_artist'] if 'is_author_artist' in data else False
        self.matched_song = data['matched_song'] if 'matched_song' in data else {}
        self.video_duration = data['video_duration'] if 'video_duration' in data else None
        self.aweme_type = data['aweme_type'] if 'aweme_type' in data else None

    def __str__(self) -> str:
        return (
            f"Music:\n"
            f"  ID: {self.id}\n"
            f"  ID String: {self.id_str}\n"
            f"  Title: {self.title}\n"
            f"  Author: {self.author}\n"
            f"  Album: {self.album}\n"
            f"  Cover Large:\n{self.cover_large}"
            f"  Cover Medium:\n{self.cover_medium}"
            f"  Cover Thumb:\n{self.cover_thumb}"
            f"  Play URL:\n{self.play_url}"
            f"  Source Platform: {self.source_platform}\n"
            f"  Duration: {self.duration}\n"
            f"  Extra: {self.extra}\n"
            f"  User Count: {self.user_count}\n"
            f"  Status: {self.status}\n"
            f"  Owner ID: {self.owner_id}\n"
            f"  Owner Nickname: {self.owner_nickname}\n"
            f"  Is Original: {self.is_original}\n"
            f"  MID: {self.mid}\n"
            f"  Owner Handle: {self.owner_handle}\n"
            f"  Sec UID: {self.sec_uid}\n"
            f"  Avatar Thumb:\n{self.avatar_thumb}"
            f"  Avatar Medium:\n{self.avatar_medium}"
            f"  Preview Start Time: {self.preview_start_time}\n"
            f"  Preview End Time: {self.preview_end_time}\n"
            f"  Is Commerce Music: {self.is_commerce_music}\n"
            f"  Is Original Sound: {self.is_original_sound}\n"
            f"  Audition Duration: {self.audition_duration}\n"
            f"  Shoot Duration: {self.shoot_duration}\n"
            f"  Is Author Artist: {self.is_author_artist}\n"
            f"  Matched Song: {self.matched_song}\n"
            f"  Video Duration: {self.video_duration}\n"
            f"  Aweme Type: {self.aweme_type}\n"
        )

class VideoControl:
    def __init__(self, data: dict) -> None:
        self.allow_download = data['allow_download'] if 'allow_download' in data else None
        self.share_type = data['share_type'] if 'share_type' in data else None
        self.show_progress_bar = data['show_progress_bar'] if 'show_progress_bar' in data else None
        self.draft_progress_bar = data['draft_progress_bar'] if 'draft_progress_bar' in data else None
        self.allow_duet = data['allow_duet'] if 'allow_duet' in data else None
        self.allow_react = data['allow_react'] if 'allow_react' in data else None
        self.prevent_download_type = data['prevent_download_type'] if 'prevent_download_type' in data else None
        self.allow_dynamic_wallpaper = data['allow_dynamic_wallpaper'] if 'allow_dynamic_wallpaper' in data else None
        self.timer_status = data['timer_status'] if 'timer_status' in data else None
        self.allow_music = data['allow_music'] if 'allow_music' in data else None
        self.allow_stitch = data['allow_stitch'] if 'allow_stitch' in data else None

    def __str__(self) -> str:
        return (
            f"Video Control:\n"
            f"  Allow Download: {self.allow_download}\n"
            f"  Share Type: {self.share_type}\n"
            f"  Show Progress Bar: {self.show_progress_bar}\n"
            f"  Draft Progress Bar: {self.draft_progress_bar}\n"
            f"  Allow Duet: {self.allow_duet}\n"
            f"  Allow React: {self.allow_react}\n"
            f"  Prevent Download Type: {self.prevent_download_type}\n"
            f"  Allow Dynamic Wallpaper: {self.allow_dynamic_wallpaper}\n"
            f"  Timer Status: {self.timer_status}\n"
            f"  Allow Music: {self.allow_music}\n"
            f"  Allow Stitch: {self.allow_stitch}\n"
        )

class Statistics:
    def __init__(self, data: dict) -> None:
        self.aweme_id = data['aweme_id'] if 'aweme_id' in data else None
        self.collect_count = data['collect_count'] if 'collect_count' in data else None
        self.comment_count = data['comment_count'] if 'comment_count' in data else None
        self.digg_count = data['digg_count'] if 'digg_count' in data else None
        self.download_count = data['download_count'] if 'download_count' in data else None
        self.play_count = data['play_count'] if 'play_count' in data else None
        self.share_count = data['share_count'] if 'share_count' in data else None
        self.forward_count = data['forward_count'] if 'forward_count' in data else None
        self.lose_count = data['lose_count'] if 'lose_count' in data else None
        self.lose_comment_count = data['lose_comment_count'] if 'lose_comment_count' in data else None
        self.whatsapp_share_count = data['whatsapp_share_count'] if 'whatsapp_share_count' in data else None

    def __str__(self) -> str:
        return (
            f"Statistics:\n"
            f"  Aweme ID: {self.aweme_id}\n"
            f"  Collect Count: {self.collect_count}\n"
            f"  Comment Count: {self.comment_count}\n"
            f"  Digg Count: {self.digg_count}\n"
            f"  Download Count: {self.download_count}\n"
            f"  Play Count: {self.play_count}\n"
            f"  Share Count: {self.share_count}\n"
            f"  Forward Count: {self.forward_count}\n"
            f"  Lose Count: {self.lose_count}\n"
            f"  Lose Comment Count: {self.lose_comment_count}\n"
            f"  Whatsapp Share Count: {self.whatsapp_share_count}\n"
        )


class LabelTop:
    def __init__(self, data: dict) -> None:
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self) -> str:
        return (
            f"LabelTop:\n"
            f"  URI: {self.uri}\n"
            f"  URL List: {', '.join(self.url_list) if self.url_list else None}\n"
            f"  Width: {self.width}\n"
            f"  Height: {self.height}\n"
        )

class Avatar:
    def __init__(self, data: dict):
        self.uri = data['uri'] if 'uri' in data else ''
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else 0
        self.height = data['height'] if 'height' in data else 0

class Author:
    def __init__(self, data: dict):
        self.avatar_168x168 = Avatar(data['avatar_168x168']) if 'avatar_168x168' in data else Avatar({})
        self.avatar_300x300 = Avatar(data['avatar_300x300']) if 'avatar_300x300' in data else Avatar({})
        self.avatar_larger = Avatar(data['avatar_larger']) if 'avatar_larger' in data else Avatar({})
        self.avatar_medium = Avatar(data['avatar_medium']) if 'avatar_medium' in data else Avatar({})
        self.avatar_thumb = Avatar(data['avatar_thumb']) if 'avatar_thumb' in data else Avatar({})
        self.avatar_uri = data['avatar_uri'] if 'avatar_uri' in data else ''
        self.custom_verify = data['custom_verify'] if 'custom_verify' in data else ''
        self.download_prompt_ts = data['download_prompt_ts'] if 'download_prompt_ts' in data else 0
        self.download_setting = data['download_setting'] if 'download_setting' in data else 0
        self.duet_setting = data['duet_setting'] if 'duet_setting' in data else 0
        self.language = data['language'] if 'language' in data else ''
        self.nickname = data['nickname'] if 'nickname' in data else ''
        self.region = data['region'] if 'region' in data else ''
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else ''
        self.share_info = data['share_info'] if 'share_info' in data else {}
        self.short_id = data['short_id'] if 'short_id' in data else ''
        self.signature = data['signature'] if 'signature' in data else ''
        self.uid = data['uid'] if 'uid' in data else ''
        self.unique_id = data['unique_id'] if 'unique_id' in data else ''
        self.unique_id_modify_time = data['unique_id_modify_time'] if 'unique_id_modify_time' in data else 0
        self.user_mode = data['user_mode'] if 'user_mode' in data else 0
        self.user_rate = data['user_rate'] if 'user_rate' in data else 0
        self.verification_type = data['verification_type'] if 'verification_type' in data else 0
        self.video_icon = Avatar(data['video_icon']) if 'video_icon' in data else Avatar({})
        self.youtube_channel_id = data['youtube_channel_id'] if 'youtube_channel_id' in data else ''
        self.youtube_channel_title = data['youtube_channel_title'] if 'youtube_channel_title' in data else ''

class Cover:
    def __init__(self, data):
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self):
        return f"Cover(uri={self.uri}, url_list={self.url_list}, width={self.width}, height={self.height})"

class OriginCover:
    def __init__(self, data):
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None

    def __str__(self):
        return f"OriginCover(uri={self.uri}, url_list={self.url_list}, width={self.width}, height={self.height})"
    
class PlayAddr:
    def __init__(self, data):
        self.uri = data['uri'] if 'uri' in data else None
        self.url_list = data['url_list'] if 'url_list' in data else []
        self.width = data['width'] if 'width' in data else None
        self.height = data['height'] if 'height' in data else None
        self.data_size = data['data_size'] if 'data_size' in data else None
        self.file_hash = data['file_hash'] if 'file_hash' in data else None
        self.file_cs = data['file_cs'] if 'file_cs' in data else None
        self.url_key = data['url_key'] if 'url_key' in data else None

    def __str__(self):
        return (f"PlayAddr(uri={self.uri}, url_list={self.url_list}, width={self.width}, "
                f"height={self.height}, data_size={self.data_size}, file_hash={self.file_hash}, "
                f"file_cs={self.file_cs}, url_key={self.url_key})")


class BitRate:
    def __init__(self, data):
        self.bit_rate = data['bit_rate'] if 'bit_rate' in data else None
        self.play_addr = PlayAddr(data['play_addr']) if 'play_addr' in data else None
        self.is_bytevc1 = data['is_bytevc1'] if 'is_bytevc1' in data else None
        self.dub_infos = data['dub_infos'] if 'dub_infos' in data else None
        self.gear_name = data['gear_name'] if 'gear_name' in data else None
        self.quality_type = data['quality_type'] if 'quality_type' in data else None

    def __str__(self):
        return (f"BitRate(bit_rate={self.bit_rate}, play_addr={self.play_addr}, "
                f"is_bytevc1={self.is_bytevc1}, dub_infos={self.dub_infos}, "
                f"gear_name={self.gear_name}, quality_type={self.quality_type})")
    

