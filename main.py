import os
from pathlib import Path
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv(Path(__file__).resolve().parent / ".env")

PROMISED_DOWN = os.getenv("PROMISED_DOWN", "1000")
PROMISED_UP = os.getenv("PROMISED_UP", "1000")
Y_EMAIL = os.getenv("Y_EMAIL")
Y_PASSWORD = os.getenv("Y_PASSWORD")
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y/login"
SPEEDTEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        sleep(2)

        accept_button = self.driver.find_element(
            By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'
        )
        accept_button.click()
        sleep(2)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(base_window)

        go_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button/h1',
        )
        go_button.click()
        sleep(100)

        self.down = self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3',
        ).text
        self.up = self.driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3',
        ).text

        print(f"down: {self.down}\nup: {self.up}")

    def tweet_at_provider(self):
        if not Y_EMAIL or not Y_PASSWORD:
            raise RuntimeError("Set Y_EMAIL and Y_PASSWORD in your .env file.")

        self.driver.get(Y_LOGIN_URL)
        sleep(2)

        wait = WebDriverWait(driver=self.driver, timeout=2)

        y_email_input = wait.until(ec.presence_of_element_located((By.ID, "email")))
        y_email_input.clear()
        y_email_input.send_keys(Y_EMAIL)

        y_password_input = wait.until(ec.presence_of_element_located((By.ID, "password")))
        y_password_input.clear()
        y_password_input.send_keys(Y_PASSWORD)

        y_login_button = self.driver.find_element(
            By.XPATH, '/html/body/div/div/form/button'
        )
        y_login_button.click()
        sleep(2)

        post_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/nav/button')
        post_button.click()

        post_input = wait.until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="modal-compose"]'))
        )
        post_input.clear()
        post_input.send_keys(
            f"Hey Internet Provider, why is my internet speed "
            f"{self.down} down/{self.up} up when I pay for "
            f"{PROMISED_DOWN} down/{PROMISED_UP} up?"
        )

        final_post_button = self.driver.find_element(
            By.XPATH, '//*[@id="modal-post-btn"]'
        )
        final_post_button.click()


if __name__ == "__main__":
    if not Y_EMAIL or not Y_PASSWORD:
        raise RuntimeError("Set Y_EMAIL and Y_PASSWORD in your .env file.")
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
