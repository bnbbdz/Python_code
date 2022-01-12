#import thu vien
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
from datetime import datetime, timedelta
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
import datetime as dt
import shutil, os

#dien ngay muon download/Luu y dinh dang ngay cua may tinh 
begin_date = dt.date(2020,5,29) #Nam,Thang,Ngay
end_date = dt.date(2020,6,1) #Lay them 1 ngay so voi ngay dinh xuat du lieu
# today = datetime.today().date()
# previous_day = today - timedelta(1)
# today_formatted = today.strftime('%d/%m/%Y')
# previous_day_formatted = previous_day.strftime('%d/%m/%Y')

#tao list ngay muon download
day_list = []
while begin_date < end_date :
    x = begin_date.strftime('%m/%d/%Y')
    day_list.append(x)
    begin_date = begin_date + timedelta(1)

#Bat dau vong lap
for day_download in day_list :
    #Thay doi vi tri download
    chromeOptions = Options()
    prefs = {
    "download.default_directory": r"R:\1. DATABASE\1. Bank\2020\Bank 2005\Cuong Data\Giro 05_2020",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True }
    chromeOptions.add_experimental_option('prefs', prefs)
    #Khoi tao chrome
    driver = webdriver.Chrome(executable_path = r'C:\webdriver\chromedriver',chrome_options=chromeOptions)
    driver.get('https://................')
    driver.maximize_window()
    time.sleep(3)
    
    #Dang nhap email
    driver.find_element_by_id('identifierId').send_keys('..........')
    driver.find_element_by_id('identifierNext').send_keys(Keys.ENTER)
    time.sleep(3)
    
    #Dang nhap mat khau
    pw = driver.find_element_by_id('password')
    pw.click()
    pyautogui.typewrite('.............')
    pyautogui.press('enter')
    time.sleep(3)
    
    #Dien ngay
    driver.find_element_by_id('id_from_date').send_keys(day_download)
    driver.find_element_by_id('id_to_date').send_keys(day_download)
    time.sleep(1)
    
    #Doi dinh dang download
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID "id_export_format")))
    # export_element = WebDriverWait(driver, 10).until(lambda driver:Select(driver.find_element_by_id('id_export_format')))
    export_element = Select(driver.find_element_by_id("id_export_format"))
    export_element.select_by_visible_text('CSV')
    
    #Download
    driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div[13]/input[1]').click()

    
    #Thiet lap ten file
    m = int(day_download[:2])
    d = int(day_download[3:5])
    file_name = r'R:\1. DATABASE\1. Bank\2020\Bank 20{0:0>2d}\Cuong Data\Giro {0:0>2d}_2020\bank_giro_transaction_query_2020{0:0>2d}{1:0>2d}_2020{0:0>2d}{1:0>2d}.csv'.format(m,d)
    print(file_name)
    # kiem tra file da download xong chua và thoat cua so
    while True :
        if os.path.exists(file_name) :
            break
        else :
            time.sleep(20)    
    
    driver.switch_to_window(driver.current_window_handle)
    time.sleep(10)
    driver.quit()