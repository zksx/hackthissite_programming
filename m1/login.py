from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass


class UserInfo:
    def ___init___(self, username, password):
        self.username = username
        self.password = password


class HackThisSiteInfo():
    def ___init___(self, username_field, password_field):
        self.username_field = username_field
        self.password_field = password_field

def main():
    login_to_hackthissite()

def login_to_hackthissite():
    URL = "https://www.hackthissite.org/missions/prog/1/index.php"
    driver = webdriver.Firefox()
    driver.get(URL)

    user_info = UserInfo()
    website_info = HackThisSiteInfo()

    user_info = get_user_info()
    website_info = get_website_info(driver)

    send_info(user_info, website_info)

    return driver


def get_website_info(driver):
    temp_user_info = HackThisSiteInfo()
    inner_login = driver.find_element(By.ID, "innerlogin")

    username_field = inner_login.find_element(By.NAME, "username")
    password_field = inner_login.find_element(By.NAME, "password")

    temp_user_info.username_field = username_field
    temp_user_info.password_field = password_field

    return temp_user_info


def get_user_info():
    temp_user_info = UserInfo()

    temp_user_info.username = input_hackthissite_username()
    temp_user_info.password = input_hackthissite_password()
    return temp_user_info


def input_hackthissite_username():
    username = input("Enter username:")
    return username


def input_hackthissite_password():
    password = getpass()
    return password


def send_info(user_info, website_info):
    website_info.password_field.clear()
    website_info.username_field.send_keys(user_info.username)

    website_info.password_field.clear()
    website_info.password_field.send_keys(user_info.password)
    website_info.password_field.send_keys(Keys.RETURN)

if __name__ == "__main__":
    main()
