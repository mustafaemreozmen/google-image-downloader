from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import sys
import time
import urllib.request

def seleniumProcesses(passedArgs):
    options = webdriver.ChromeOptions()
    #Headless field is create the automation with no display.
    options.add_argument('headless')
    browser = webdriver.Chrome(executable_path="../driver/chromedriver", options=options)
    browser.get('https://google.com')
    loadingControl = WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'btnK')))
    #This variable takes the search bar at the Google Search
    searchBar = browser.find_element_by_name('q')
    searchBar.send_keys(str(passedArgs.keyword).replace('-', ' '), Keys.ENTER)
    #This variable click the 'Images' bar at the Google Search Result. Some results 
    linkImages = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
    #Second link is not always for Images. This control can be pass that problem. This is very hardcoded. I will update this soon.
    if (linkImages.text == 'Haritalar'):
        linkImages = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[3]/a')
    elif(linkImages.text == 'Uçuş Arama'):
            linkImages = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[3]/a')
    #Click for Images link.
    linkImages.get_attribute('href')
    linkImages.click()
    #Scrolls for more image.
    value = 0
    for i in range(passedArgs.scrollQuantity):
        browser.execute_script("scrollBy("+ str(value) +",+1000);")
        value += 1000
        time.sleep(2)
    #This section creates a folder if there is no folder.
    try:
        os.mkdir('../downloads')
    except FileExistsError:
        pass
   #For loop for downloading.
    for i in range(1,passedArgs.quantity+1):
        try:
            test = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]')
            test.click()
            time.sleep(3)
            img = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/a/img')
            src = img.get_attribute('src')
            if src != None:
                src  = str(src)
                print('Image'+str(i)+'.jpg downloading...')
                urllib.request.urlretrieve(src, os.path.join('../downloads','image'+str(i)+'.jpg'))
                print('Image'+str(i)+'.jpg downloaded.')
            else:
                raise TypeError
        except:
            print('Image'+str(i)+'.jpg is not downloaded.')
            continue
    #Closes the browser.
    browser.quit()
        
    