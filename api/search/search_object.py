
class ChallengeData:
    def __init__(self, data: dict) -> None:
        self.view_count = data['challenge_info']['view_count'] if 'view_count' in data['challenge_info'] else None
        self.type = data['challenge_info']['type'] if 'type' in data['challenge_info'] else None
        self.user_count = data['challenge_info']['user_count'] if 'user_count' in data['challenge_info'] else None
        self.cid = data['challenge_info']['cid'] if 'cid' in data['challenge_info'] else None
        self.cha_name = data['challenge_info']['cha_name'] if 'cha_name' in data['challenge_info'] else None
        self.items = data['items'] if 'items' in data else None
        self.position = data['position'] if 'position' in data else None

    def __str__(self) -> str:
        output_string = (
            f"Challenge Info: \n"
            f"View Count: {self.view_count}\n" +
            f"Type: {self.type}\n" +
            f"User Count: {self.user_count}\n" +
            f"CID: {self.cid}\n" +
            f"Challenge Name: {self.cha_name}\n" +
            f"Items: {self.items}\n" +
            f"Position: {self.position}\n"
        )
        return output_string
    

class User:
    def __init__(self, data: dict) -> None:
        self.__get_avatar(data)
        self.challenges = data['challenges'] if 'challenges' in data else None
        self.effects = data['effects'] if 'effects' in data else None
        self.items = data['items'] if 'items' in data else None
        self.mix_list = data['mix_list'] if 'mix_list' in data else None
        self.musics = data['musics'] if 'musics' in data else None
        self.position = data['position'] if 'position' in data else None
        self.uniqid_position = data['uniqid_position'] if 'uniqid_position' in data else None
        self.follower_count = data['follower_count'] if 'follower_count' in data else -1
        self.search_user_name = data['search_user_name'] if 'search_user_name' in data else None
        self.following_count = data['following_count'] if 'following_count' in data else -1
        self.nickname = data['nickname'] if 'nickname' in data else None
        self.original_musician = data['original_musician'] if 'original_musician' in data else None
        self.sec_uid = data['sec_uid'] if 'sec_uid' in data else None
        self.aweme_count = data['aweme_count'] if 'aweme_count' in data else -1
        self.short_id = data['short_id'] if 'short_id' in data else None
        self.total_favorited = data['total_favorited'] if 'total_favorited' in data else None
        self.uid = data['uid'] if 'uid' in data else None
        self.unique_id = data['unique_id'] if 'unique_id' in data else None
        self.user_mode = data['user_mode'] if 'user_mode' in data else -1
        self.user_rate = data['user_rate'] if 'user_rate' in data else -1
        self.verification_type = data['verification_type'] if 'verification_type' in data else -1
        self.video_icon = Avatar(**data['video_icon']) if 'video_icon' in data else None

    def __get_avatar(self, data: dict):
        if 'avatar_larger' in data:
            self.avatar = Avatar(**data['avatar_larger'])
        elif 'avatar_medium' in data:
            self.avatar = Avatar(**data['avatar_medium'])
        elif 'avatar_300x300' in data:
            self.avatar = Avatar(**data['avatar_300x300'])
        elif 'avatar_168x168' in data:
            self.avatar = Avatar(**data['avatar_168x168'])
        elif 'avatar_thumb' in data:
            self.avatar = Avatar(**data['avatar_thumb'])
        else:
            self.avatar = None

    def __str__(self) -> str:
        output_list = [
            f"Challenges: {self.challenges}",
            f"Effects: {self.effects}",
            f"Items: {self.items}",
            f"Mix list: {self.mix_list}",
            f"Musics: {self.musics}",
            f"Position: {self.position}",
            f"Uniqid position: {self.uniqid_position}\n",
            f"User Info : ",
            f"Follower count: {self.follower_count}",
            f"Search user name: {self.search_user_name}",
            f"Following count: {self.following_count}",
            f"Nickname: {self.nickname}",
            f"Original musician: {self.original_musician}",
            f"Sec UID: {self.sec_uid}",
            f"Aweme count: {self.aweme_count}",
            f"Short ID: {self.short_id}",
            f"Total favorited: {self.total_favorited}",
            f"UID: {self.uid}",
            f"Unique ID: {self.unique_id}",
            f"User mode: {self.user_mode}",
            f"User rate: {self.user_rate}",
            f"Verification type: {self.verification_type}",
            "Avatar:",
            (f"URI: {self.avatar.uri}\nURL list:\n" + "\n".join(self.avatar.url_list)) if self.avatar else "None",
            "Video icon:",
            (f"URI: {self.video_icon.uri}\nURL list:\n" + "\n".join(self.video_icon.url_list)) if self.video_icon else "None"
        ]
        return "\n".join(output_list)


class Avatar:
    def __init__(self, uri=None, url_list=None,width=None, height=None):
        self.uri = uri
        self.url_list = url_list if url_list is not None else []
        self.width = width
        self.height = height

class HeaderInfo:
    def __init__(self, data: dict) -> None:
        self.status = data['status'] if 'status' in data else None
        self.cursor = data['data']['cursor'] if 'cursor' in data['data'] else -1
        self.has_more = data['data']['has_more'] if 'has_more' in data['data'] else None
        self.input_keyword = data['data']['input_keyword'] if 'input_keyword' in data['data'] else None
        self.qc = data['data']['qc'] if 'qc' in data['data'] else None
        self.type = data['data']['type'] if 'type' in data['data'] else -1

    def __str__(self) -> str:
        header_info = [
            f"Status: {self.status}",
            f"Cursor: {self.cursor}",
            f"Has more: {self.has_more}",
            f"Input keyword: {self.input_keyword}",
            f"QC: {self.qc}",
            f"Type: {self.type}"
        ]
        return "\n".join(header_info)



