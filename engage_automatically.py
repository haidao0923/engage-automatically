from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:/Users/haixd/AppData/Local/Programs/Python/Python36-32/Scripts/chromedriver')
url = 'https://gatech.campuslabs.com/engage/submitter/organization/boardgameclub/eventsubmission/create'

# Remember to fullscreen automated page for correct image resize
username = [INSERT USERNAME HERE]
password = [INSERT PASSWORD HERE]
phone_number = [INSERT PHONE NUMBER HERE]
discord_link = [INSERT DISCORD LINK HERE]

isOnline = True  # Change this to generate online or alternative meeting information

start_time = '2pm'
end_time = '5pm'
event_date = '07/10/22'  # Remember to change this
image_link = [INSERT PATH TO IMAGE HERE]  # Remember to change this
event_name = 'Board Game Club Summer Meeting'
event_description = 'Join us this Sunday 2-5pm on Crosland Tower 2nd Floor to play board games! This event is open to all students and faculties at Georgia Tech. No previous gaming experience necessary, we will teach you how to play. Join our discord for announcements and game requests: https://discord.gg/5jWHwFaJFX'
event_location = 'Crosland Tower 2nd Floor'
if isOnline:
    start_time = '8pm'
    end_time = '10pm'
    event_date = '07/07/22'  # Remember to change this
    image_link = [INSERT PATH TO IMAGE HERE]  # Remember to change this
    event_name = 'Board Game Club Virtual Meeting'
    event_description = 'Join us this Thursday 8-10pm on our Discord server to play board games! This event is open to all students and faculties at Georgia Tech. No previous gaming experience necessary, we will teach you how to play. Join our Discord to play: https://discord.gg/5jWHwFaJFX'
    event_location = 'Discord Voice Chat - Online at https://discord.gg/5jWHwFaJFX'

driver.get(url)

driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'btn-submit').click()
driver.switch_to.frame('duo_iframe')  # make sure if element is in iframe that you switch to it
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.push-label button")))
driver.find_element(By.CSS_SELECTOR, "div.push-label button").click()
WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "form-section-container")))

# Page 1
driver.find_element(By.ID, 'Name').send_keys(event_name)
Select(driver.find_element(By.ID, 'Theme')).select_by_value('Social')
driver.switch_to.frame('Description_ifr')
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'tinymce')))
driver.find_element(By.ID, 'tinymce').click()
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys(event_description)
driver.switch_to.default_content()
driver.find_element(By.CLASS_NAME, 'instance-location-button').click()
driver.find_element(By.CLASS_NAME, 'btn-hide-map').click()
driver.find_element(By.ID, 'Instances[0].ExternalLocation').send_keys(event_location)
driver.find_element(By.CLASS_NAME, 'locationModal-savebutton').click()
driver.find_element(By.ID, 'Instances[0]_StartDate').send_keys(Keys.CONTROL, 'a')
driver.find_element(By.ID, 'Instances[0]_StartDate').send_keys(event_date)
driver.find_element(By.ID, 'Instances[0]_StartTime').clear()
driver.find_element(By.ID, 'Instances[0]_StartTime').send_keys(start_time)
driver.find_element(By.ID, 'Instances[0]_EndDate').send_keys(Keys.CONTROL, 'a')
driver.find_element(By.ID, 'Instances[0]_EndDate').send_keys(event_date)
driver.find_element(By.ID, 'Instances[0]_EndTime').clear()
driver.find_element(By.ID, 'Instances[0]_EndTime').send_keys(end_time)
Select(driver.find_element(By.ID, 'bsmSelectbsmContainer0')).select_by_visible_text('Arts & Entertainment')
Select(driver.find_element(By.ID, 'bsmSelectbsmContainer0')).select_by_visible_text('General')
Select(driver.find_element(By.ID, 'bsmSelectbsmContainer0')).select_by_visible_text('Grad-Student Friendly')
Select(driver.find_element(By.ID, 'bsmSelectbsmContainer0')).select_by_visible_text('Technology & Gaming')
driver.find_element(By.CLASS_NAME, 'mdl-button').click()  # Click Next
# Page 2
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'ShouldAllowGuests')))
driver.find_element(By.ID, 'ShouldAllowGuests').click()
driver.find_element(By.ID, 'submitRsvpSettings').click()  # Click Next
# Page 3
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pull-right')))
driver.find_element(By.ID, 'submitPostEventSettings').click()  # Click Next
# Page 4
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'skip-cover-photo-button')))
driver.find_element(By.ID, 'file').send_keys(image_link)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'image_width')))
driver.find_element(By.ID, 'image_width').clear()
driver.find_element(By.ID, 'image_width').send_keys('613')  # Resize Image
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'MuiButton-contained')))
driver.find_element(By.CLASS_NAME, 'MuiButton-contained').click()  # Crop Image
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'next-photo-button')))
driver.find_element(By.ID, 'next-photo-button').click()  # Click Next
# Page 5
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, '35475824')))
driver.find_element(By.ID, '35475824').click()
driver.find_element(By.ID, '37263821').click()
driver.find_element(By.ID, '37263822').click()
driver.find_element(By.ID, '35975470').click()
driver.find_element(By.ID, '35975471').click()
driver.find_element(By.ID, '35475861').click()
driver.find_element(By.ID, '36006097').click()
driver.find_element(By.ID, 'answerTextBox-35975512-free').send_keys('Hai')
driver.find_element(By.ID, 'answerTextBox-35975516-free').send_keys('Dao')
driver.find_element(By.ID, 'answerTextBox-35975514-free').send_keys('hdao35@gatech.edu')
driver.find_element(By.ID, 'answerTextBox-35975550-free').send_keys(phone_number)
driver.find_element(By.ID, '41342632').click()
driver.find_element(By.CLASS_NAME, 'right').click()  # Click Next
# Page 6
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'answerTextBox-37263729-free')))
driver.find_element(By.ID, 'answerTextBox-37263729-free').send_keys(discord_link)
driver.find_element(By.CLASS_NAME, 'right').click()  # Click Next
# Page 7
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, '37263685')))
driver.find_element(By.ID, '37263685').click()
driver.find_element(By.ID, '37263682').click()
driver.find_element(By.ID, '37263720').click()
driver.find_element(By.CLASS_NAME, 'right').click()  # Click Next
# Page 8
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, '41443708')))
driver.find_element(By.ID, '41443708').click()
driver.find_element(By.ID, '41444508').click()
driver.find_element(By.CLASS_NAME, 'right').click()  # Click Next
# Page 9
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'review-btn')))
driver.find_element(By.ID, 'review-btn').click()