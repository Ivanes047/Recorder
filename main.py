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

def recording(url, name):
    s = Service(executable_path='C:\\Users\\IvanS\\OneDrive\\Документы\\Я\\Записи лекций\\Recorder\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    try:
        driver.set_window_position(0, 0)
        driver.maximize_window()
        driver.get(url)
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
        
        ffmpeg = rec.start_record(name)
        time.sleep(5700) # Длительность вебинара
        rec.end_record(ffmpeg)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        
def main():
    # Расписание
    schedule.every().wednesday.at('14:30').do(recording, name='third', url='https://events.webinar.ru/19396923/1092481784/session/161488321')
    schedule.every().wednesday.at('16:10').do(recording, name='fourth', url='https://events.webinar.ru/19396587/1933155138/session/2006684246')
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()