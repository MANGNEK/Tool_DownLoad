from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Down import download_video
import time

#get url video from file txt
def getlinkfromtxt():
    file_path = "C:\\Users\\ADMIN\\Desktop\\Tool_DownLoad\\PyThon\\Link\\LinkTikTok.txt"
    with open(file_path, "r") as file:
        link = file.read()
    return(link)

#click vào video đầu tiên của kênh
def clickfistvideo(driver):
    try:
        first_video = driver.find_element(By.CLASS_NAME, "video-card")
        first_video.click()
    except Exception as e:
        print("Không tìm thấy phần tử hoặc đã xảy ra lỗi:", e)

#lấy link của video 
def getvideo(video_src):
    #call function download video 
    download_video(video_src)
    print("đa tai xong video")

#open new tab
def opennewtap(driver):
    driver.execute_script("window.open('', '_blank');")

#switch to new tab
def switchtotab(driver):
    driver.switch_to.window(driver.window_handles[-1])
  
#function login
def login(driver):
    driver.get("https://studio.kuaishou.com/user/login?redirect=%2F")

#function get url video after return url video
def getandclicknextvideo(driver):
    time.sleep(2)
    try:
        nextclick = driver.find_element(By.CLASS_NAME, "video-switch-next")
        nextclick.click()
        #time.sleep(2)
    except Exception as e:
        print("Không tìm thấy video tiếp theo hoặc đã xảy ra lỗi:", e)
    player_video = driver.find_element(By.CLASS_NAME,"player-video")       
    # Lấy giá trị của thuộc tính "src"
    video_src = player_video.get_attribute("src")
    download_video(video_src)

#function get count video
def getcountvideo():
    file_path ="C:\\Users\\ADMIN\\Desktop\\Tool_DownLoad\\PyThon\\Link\\CountVideo.txt"
    with open(file_path,"r") as file:
        count = file.read()
    return(count)

def main(): 
    # call function get link url video
    link = getlinkfromtxt()

    # Tạo driver sử dụng Chrome Driver
    driver = webdriver.Chrome()

    #login by Qr code
    login(driver)

    #open tab with link after reload tab 
    driver.get(link)
    driver.refresh()
    time.sleep(5)
    # Tìm và click vào phần tử đầu tiên có class name là "video-card video-item vertical"
    try:
        first_video = driver.find_element(By.CLASS_NAME, "video-card")
        first_video.click()
    except Exception as e:
        print("Không tìm thấy video đầu tiên")
    count =int(getcountvideo())
    while count != 0:
       getandclicknextvideo(driver)
       count =count-1              
    driver.close()
    driver.quit()
    print("Đã tải xong video")
if __name__ =="__main__":
    main()
