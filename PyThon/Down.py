import subprocess
import os
import re

def download_video(video_url):
    # Xác định thư mục chứa video ngay tại nơi chạy script
    video_dir = os.path.join(os.getcwd(), 'Video')

    # Kiểm tra và tạo thư mục nếu chưa tồn tại
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)
    
    print("🎥 Đang tải video...")

    # Lệnh tải video
    command = f'yt-dlp -o "{video_dir}/%(title)s.%(ext)s" "{video_url}"'

    # Chạy lệnh và lọc chỉ hiển thị tiến trình % tải
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    # Đọc log từ yt-dlp theo từng dòng
    for line in process.stdout:
        match = re.search(r'(\d+.\d+)%', line)  # Tìm phần trăm tải về
        if match:
            print(f"📥 Đã tải: {match.group(1)}%", end='\r')  # In ra cùng một dòng

    process.wait()  # Chờ tải xong

    print("\n✅ Tải video hoàn tất!")

# Ví dụ sử dụng:
# download_video("https://www.example.com/video-url")
