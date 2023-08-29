import subprocess
import os
def download_video(video_url):
    current_dir = os.path.dirname(os.path.abspath(__file__))                                
    file_path = os.path.join(current_dir, 'Link', 'Output.txt')
    with open(file_path, "r") as file:
        link = file.read()
    print(link)
    output_directory = link
    print("url video in download :",video_url)
    # Sử dụng subprocess để thực thi lệnh youtube-dl trong Command Prompt
    command = f"youtube-dl -o '{output_directory}/%(title)s.%(ext)s' {video_url}"
    subprocess.call(command, shell=True)