# this file is for initializing a driver in each test,
# giving opportunities for different environments, browsers, etc.

import re
import traceback
from chromedriver_py import binary_path
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def driver_init():
    service = ChromeService(executable_path=binary_path)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=service,
                              options=chrome_options)
    driver.maximize_window()
    return driver


def handle_exception(driver,
                     custom_exception='',
                     raise_exception=True,
                     screenshot_name='Error_' + str(randint(1, 1000)).zfill(4) + '.png'):

    screenshot_pattern = "\w+.(jpg|JPG|png|PNG)$"

    exception = traceback.format_exc()

    if screenshot_name != '':
        scr_path = "./" + screenshot_name
        match = re.match(pattern=screenshot_pattern, string=screenshot_name)
        if match is None:
            raise Exception("Please specify a valid screenshot name --> ABC_Z_abc_z_012_9.(jpg|JPG|png|PNG)")
        try:
            driver.save_screenshot(scr_path)
            print("Screenshot taken: " + screenshot_name)
        except:
            print(screenshot_name + " could not be generated")

    full_exception = custom_exception + '\n' + exception

    if raise_exception:
        raise Exception(full_exception)
    else:
        print(full_exception)