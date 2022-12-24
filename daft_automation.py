"""
import webbrowser

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

webbrowser.get('edge').open('https://www.daft.ie/property-for-rent/ireland?rentalPrice_to=3000&numBeds_from=3&numBeds_to=4&numBaths_from=2&sort=publishDateDesc&location=dublin&location=dublin-city')
"""
# importing required package of webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import os
import csv
import time

from generate_data import generateFilterLink
from generate_data import generateEndTime

class SetUp:
    def __init__(self):
        load_dotenv(".env")
        self.SECRET_ID = os.environ.get('secretUser')
        self.SECRET_PASSWORD = os.environ.get('secretPassword')
        self.SECRET_NAME = os.environ.get('secretName')
        self.SECRET_CONTACT = os.environ.get('secretContact')
        self.SECRET_MESSAGE = os.environ.get('secretMessage')
    
        #Create new csv file to log submissions
        self.file = open("logger.csv", "a")
        self.writer = csv.writer(self.file)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('http://www.daft.ie')
        sleep(3)
        
        self.driver.maximize_window()
        #Policy Button
        self.driver.find_element(By.XPATH, '//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').click()
        sleep(3)
        #Sign-in Button
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/header/div/div[2]/div[3]/ul/li[2]/a').click()
        sleep(3)
        #EmailID field
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(self.SECRET_ID)
        sleep(3)
        #Password field
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.SECRET_PASSWORD)
        sleep(3)
        #Sign-in button
        self.driver.find_element(By.XPATH, '//*[@id="kc-login-form"]/div[2]/input').click()

        print("Logged in successfully!")

# r = SetUp()
# r.login()

class Apply(SetUp):
    def apply(self):
        self.login()
        self.applied_url = None
        self.link = generateFilterLink()
        self.applicationProcess()

        #Run automation for this interval of time
        end_time = generateEndTime()

        while time.time() < end_time:
            self.driver.get(self.link)
            sleep(3)

            #Click the latest ad on the page.
            self.latest_ad = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]').click()
            if self.applied_url != None and self.applied_url != self.driver.current_url:
                self.applicationProcess()
        
        print("Finishing up the process!")
        
        self.driver.quit()
        self.file.close()


    def applicationProcess(self):
        self.driver.get(self.link)
        sleep(3)

        #Click the latest ad on the page.
        self.latest_ad = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]').click()

        sleep(3)
        self.applied_url = self.driver.current_url
        log_address = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/h1').text
        log_price = self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/div[1]/span').text
        log_price = 'EUR ' + log_price[1:]
        log_entry = [log_price, log_address, self.applied_url, 'Applied']

        
        # self.file.write('EUR ' + log_price[1:] + '/-' + '\t' + log_address + '\t' + 'Applied' + '\n')

        # click on the link that opens a new window
        self.driver.switch_to.active_element
        # Fill the application in pop-up
        #Click on email_button
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/button').click()
        sleep(3)
        #Enter First Name
        self.driver.find_element(By.XPATH, '//*[@id="keyword1"]').send_keys(self.SECRET_NAME)
        #Enter Email-ID
        self.driver.find_element(By.XPATH, '//*[@id="keyword2"]').send_keys(self.SECRET_ID)
        #Enter Contact Number
        self.driver.find_element(By.XPATH, '//*[@id="keyword3"]').send_keys(self.SECRET_CONTACT)
        #Enter Application text
        self.driver.find_element(By.XPATH, '//*[@id="message"]').send_keys(self.SECRET_MESSAGE)

        sleep(10)

        #Send the applicaiton
        self.driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[2]/form/div/div[5]/div/button').click()
        sleep(2)

        #Close the window    
        self.driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button').click()

        try:
            text = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div').text
            if text == 'Sorry, something went wrong.':
                print("Already applied for this house!")
        except:
            self.writer.writerow(log_entry)
            print("Applied for a house!")
        #Wait 30 seconds till you apply for the next one
        sleep(30)
            

r = Apply()
r.apply()


# driver.get('https://www.daft.ie/property-for-rent/ireland?rentalPrice_to=3000&numBeds_from=3&numBeds_to=4&numBaths_from=2&sort=publishDateDesc&location=dublin&location=dublin-city')
# sleep(3)
# driver.maximize_window()
# policy_button = driver.find_element(By.XPATH, '//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').click()
# sleep(3)
# signin_button = driver.find_element(By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[3]/ul/li[2]/a').click()
# sleep(3)
# email_id_field = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(SECRET_ID)
# sleep(3)
# pass_field = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(SECRET_PASSWORD)
# sleep(3)
# sign_in_button = driver.find_element(By.XPATH, '//*[@id="kc-login-form"]/div[2]/input').click()



# #latest_ad = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]/div').click()
# latest_ad = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]').click()

# sleep(3)
# temp_url = driver.current_url
# log_address = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/h1').text
# price = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/div[1]/span').text

# file.write(price + '\t' + log_address + '\t' + 'Applied' + '\n')



# # click on the link that opens a new windo
# driver.switch_to.active_element
# # do stuff in the popup



# email_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/button').click()
# sleep(3)
# first_name = driver.find_element(By.XPATH, '//*[@id="keyword1"]').send_keys(SECRET_NAME)
# email_id = driver.find_element(By.XPATH, '//*[@id="keyword2"]').send_keys(SECRET_ID)
# phone_no = driver.find_element(By.XPATH, '//*[@id="keyword3"]').send_keys(SECRET_CONTACT)
# message = driver.find_element(By.XPATH, '//*[@id="message"]').send_keys(SECRET_MESSAGE)

# sleep(10)


# send_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[2]/form/div/div[5]/div/button').click()
# sleep(2)

# close_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button').click()
# # close_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button/svg').click()
# # popup window closes
# # and you're back

# #Closing the log file
# file.close()




