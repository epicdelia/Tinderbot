from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import openai
import random
from selenium.common.exceptions import StaleElementReferenceException
import time

from config import email, password, api_key

openai.api_key = api_key # your api key
prompt = "write a haiku about "

def generate_tinder_message():
    prompts = [
        "write a haiku about ",
        "write a great pick up line for someone named ",
        "Compose a message of love for ",
        "Write a tinder message to ",
        "Write an icebreaker to "
    ]
    return random.choice(prompts)

def generate_intro(prompt, name):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt= prompt + name,
            temperature=0.5,
            max_tokens=500
        )
        quote = response.choices[0].text.strip()
        return quote

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_tinder(self):
        sleep(2)
        self.driver.get('https://tinder.com')
        login_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Log in")]')))
        login_button.click()
        sleep(5)
        self.facebook_login()
        sleep(6)
        try:
            allow_location_button = self.driver.find_element('xpath', '//*[@id="t-1917074667"]/main/div/div/div/div[3]/button[1]')
            allow_location_button.click()
        except:
            print('no location popup')

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[2]')
            notifications_button.click()
        except:
            print('no notification popup')
    
    def facebook_login(self):
        # find and click FB login button
        login_with_facebook = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Log in with Facebook")]')))
        login_with_facebook.click()

        # save references to main and FB windows
        sleep(8)
        base_window = self.driver.window_handles[0]
        fb_popup_window = self.driver.window_handles[1]
        # switch to FB window
        self.driver.switch_to.window(fb_popup_window)

        try:
            cookies_accept_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Accept Cookies")]')))
            cookies_accept_button.click()
        except:
            print('no cookies')
        sleep(10)
        email_field = self.driver.find_element(By.NAME, 'email')
        pw_field = self.driver.find_element(By.NAME, 'pass')
        login_button = self.driver.find_element(By.NAME, 'login')
        email_field.send_keys(email)
        pw_field.send_keys(password)
        login_button.click()
        self.driver.switch_to.window(base_window)
        try:
            allow_location_button_again = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Allow")]')))
            allow_location_button_again.click()
        except:
            print('no location popup')
        try:
            enable_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Enable")]')))
            enable_button.click()
        except:
            print('no location enable')

    def right_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_RIGHT)
    def left_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.right_swipe()
            except:
                self.close_match()

    def close_match(self):
        match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    
    def get_matches(self):
        match_profiles = self.driver.find_elements('class name', 'matchListItem')
        print(str(match_profiles))
        message_links = []
        for profile in match_profiles:
            if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
                continue
            match_name = profile.find_element(By.CLASS_NAME, 'Ell')
            name = match_name.text
            print("got matches")
            print(name)
            message_links.append((name, profile.get_attribute('href')))
        return message_links

    def send_messages_to_matches(self):
        links = self.get_matches()
        for name, link in links:
            self.send_message(name, link)

    def send_message(self, name, link):
        self.driver.get(link)
        sleep(5)
        text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
        print("sending message")
        message = generate_intro(generate_tinder_message(), name)
        text_area.send_keys(message)
        sleep(10)
        # text_area.send_keys(Keys.ENTER)

bot = TinderBot()
bot.open_tinder()
sleep(10)
# bot.auto_swipe()
# bot.send_messages_to_matches()