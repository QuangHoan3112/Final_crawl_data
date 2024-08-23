import requests
import json

url = "https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/challenge/instachallenge"

headers = {
	"x-rapidapi-key": "fc80ad0c27msh51eb21aa4e1e953p16e60djsndc05cf095673",
	"x-rapidapi-host": "tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())




# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    # Lấy dữ liệu JSON từ phản hồi
    data = response.json()
    
    # Tạo file JSON và lưu dữ liệu vào
    output_file = "tiktok_hastag_challenge_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Dữ liệu đã được lưu vào {output_file}")
else:
    print(f"Lỗi khi yêu cầu dữ liệu: {response.status_code}")
