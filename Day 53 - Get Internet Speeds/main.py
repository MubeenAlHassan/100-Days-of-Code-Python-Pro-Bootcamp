from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
