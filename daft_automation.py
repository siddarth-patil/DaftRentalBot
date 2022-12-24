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

class SetUp:
    def __init__(self):
        load_dotenv(".env")
        self.SECRET_ID = os.environ.get('secretUser')
        self.SECRET_PASSWORD = os.environ.get('secretPassword')
        self.SECRET_NAME = os.environ.get('secretName')
        self.SECRET_CONTACT = os.environ.get('secretContact')
        self.SECRET_MESSAGE = os.environ.get('secretMessage')
    #Create new txt file to log submissions
        file = open("logger.txt", "w")

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

r = SetUp()
r.login()

driver.get('https://www.daft.ie/property-for-rent/ireland?rentalPrice_to=3000&numBeds_from=3&numBeds_to=4&numBaths_from=2&sort=publishDateDesc&location=dublin&location=dublin-city')
sleep(3)
driver.maximize_window()
policy_button = driver.find_element(By.XPATH, '//*[@id="js-cookie-modal-level-one"]/div/main/div/button[2]').click()
sleep(3)
signin_button = driver.find_element(By.XPATH, '//*[@id="__next"]/header/div/div[2]/div[3]/ul/li[2]/a').click()
sleep(3)
email_id_field = driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(SECRET_ID)
sleep(3)
pass_field = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(SECRET_PASSWORD)
sleep(3)
sign_in_button = driver.find_element(By.XPATH, '//*[@id="kc-login-form"]/div[2]/input').click()



#latest_ad = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]/div').click()
latest_ad = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/ul/li[1]/a/div/div[1]/div[2]').click()

sleep(3)
temp_url = driver.current_url
log_address = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/h1').text
price = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[1]/div[1]/div/div[2]/div[1]/span').text

file.write(price + '\t' + log_address + '\t' + 'Applied' + '\n')



# click on the link that opens a new windo
driver.switch_to.active_element
# do stuff in the popup



email_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[2]/div/div[1]/div[2]/div[2]/button').click()
sleep(3)
first_name = driver.find_element(By.XPATH, '//*[@id="keyword1"]').send_keys(SECRET_NAME)
email_id = driver.find_element(By.XPATH, '//*[@id="keyword2"]').send_keys(SECRET_ID)
phone_no = driver.find_element(By.XPATH, '//*[@id="keyword3"]').send_keys(SECRET_CONTACT)
message = driver.find_element(By.XPATH, '//*[@id="message"]').send_keys(SECRET_MESSAGE)

sleep(10)


send_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[2]/form/div/div[5]/div/button').click()
sleep(2)

close_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button').click()
# close_button = driver.find_element(By.XPATH, '//*[@id="contact-form-modal"]/div[1]/button/svg').click()
# popup window closes
# and you're back

#Closing the log file
file.close()




