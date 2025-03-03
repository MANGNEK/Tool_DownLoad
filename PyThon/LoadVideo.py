from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import logging
from Down import download_video

# Ẩn log của Selenium
logging.getLogger("selenium").setLevel(logging.CRITICAL)

def setup_driver(use_profile=False):
    options = Options()
    options.add_argument("--log-level=3")        # Tắt log trình duyệt
    options.add_argument("--mute-audio")         # Tắt âm thanh của Chrome
    #options.add_argument("--headless=new")       # Chạy Chrome ẩn (tùy chọn)
    
    if use_profile:
        options.add_argument("--user-data-dir=C:/Users/trung/AppData/Local/Google/Chrome/User Data")
        options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)
    return driver

def download_single_video(driver):
    time.sleep(5)
    try:
        video_element = driver.find_element(By.CSS_SELECTOR, ".kwai-player-container-video video")
        video_src = video_element.get_attribute("src")
        if video_src:
            download_video(video_src)
            print("✅ Đã tải xong video!")
        else:
            print("❌ Không tìm thấy video.")
    except Exception as e:
        print("❌ Lỗi khi tải video:", e)

def download_batch_videos(driver, count):
    try:
        first_video = driver.find_element(By.CLASS_NAME, "video-card-main")
        first_video.click()
    except:
        print("❌ Không tìm thấy video đầu tiên.")
        return
    
    while count > 0:
        time.sleep(2)
        try:
            # Tìm thẻ video trong class "kwai-player-container-video"
            video_element = driver.find_element(By.CSS_SELECTOR, ".kwai-player-container-video video")
            video_src = video_element.get_attribute("src")
            if video_src:
                download_video(video_src)
                print(f"✅ Đã tải video {count}")

            # Click vào nút "Next"
            next_button = driver.find_element(By.CSS_SELECTOR, ".switch-item.video-switch-next")
            next_button.click()
        except Exception as e:
            print("❌ Không tìm thấy video hoặc đã hết danh sách.", e)
            break

        count -= 1

def main():
    while True:
        print("\n🔹 Chọn chế độ tải video:")
        print("1 - Tải 1 video")
        print("2 - Tải hàng loạt")
        print("0 - Thoát")
        choice = input("Nhập số (0, 1, 2): ")

        if choice == "0":
            print("👋 Thoát chương trình!")
            break

        url = input("Nhập vào URL muốn tải: ")  # Nhập URL trước
        print(f"🌐 Đang mở URL: {url}")

        driver = setup_driver(use_profile=True)
        driver.get(url)  # Mở trang web trước
        time.sleep(5)  # Chờ trang tải xong

        if choice == "1":
            download_single_video(driver)
        elif choice == "2":
            count = int(input("📌 Nhập số lượng video muốn tải: "))
            download_batch_videos(driver, count)
        else:
            print("❌ Lựa chọn không hợp lệ!")

        driver.quit()
        print("✅ Hoàn thành!")

if __name__ == "__main__":
    main()
