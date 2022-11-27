import time, sys
from random import randint
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
# For Webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.headless=True

browser = webdriver.Chrome(options=chrome_options)
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

wait = WebDriverWait(browser, 20)

video_list = []

with open(sys.argv[1], "r") as vlf:
    vlst = vlf.readlines()
    for v in vlst:
        video_list.append(v.strip())

# url = "https://www.youtube.com/watch?v=mF2BHtQh4EI"
# parentGUID = browser.current_window_handle

for url in video_list:
    
    print("=================================================================")
    print(f"Watching video {url}")
    browser.get(url)
    time.sleep(2)

    try:
        play_button = browser.find_element(By.XPATH,  "//button[@data-title-no-tooltip='Play']")
        ActionChains(browser).move_to_element(play_button).click().perform()
#         play_button.click()
        
        print("Play button clicked..!\nVideo playing..!")
        
        wait_time = randint(30, 90)
        print(f"Going to play video for {wait_time} ")
        
        time.sleep(wait_time)
        print(Fore.GREEN+Style.BRIGHT+" >> Success"+Style.RESET_ALL)
        
    except Exception as err:
        print("Play Button not found..!")
        print(f"[+] ERROR: {err}")


print("All video watching complete..!")

browser.quit()

