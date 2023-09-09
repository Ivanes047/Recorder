import time
import os
import json
import schedule

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import recorder as rec

def recording():
    s = Service(executable_path='C:\\Users\\IvanS\\OneDrive\\Документы\\Я\\Записи лекций\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    try:
        driver.set_window_position(0, 0)
        driver.maximize_window()
        driver.get('https://events.webinar.ru/57009101/2125390510/session/1641136281')
        time.sleep(10)
        flag = 1
        while flag:
            try:
                name_surname= driver.find_element(By.ID, 'name')
                name_surname.clear()
                name_surname.send_keys("Иван Борисов")
                name_surname.submit()
                flag = 0
            except Exception as ex:
                pass
        
        ffmpeg = rec.start_record('analytic')
        time.sleep(6000)
        rec.end_record(ffmpeg)
        # btn PrepareVCSButtons-module__mainAction___ziopu btn_material
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        
def main():
    # schedule.every().wednesday.at('14:25').do(recording)
    recording()
    # while True:
    #     schedule.run_pending()
    
if __name__ == "__main__":
    main()