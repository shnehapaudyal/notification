import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import createnotif


def add(driver):
    for i in range(1, 5):
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            [By.XPATH, '//*[@id="sideBar"]']))
        menu_bar = driver.find_element_by_xpath('//*[@id="sideBar"]/div/ul/div[3]')
        menu_bar.click()
        createnotif.create(driver)
        group_type = driver.find_element_by_xpath('//*[@id="free-solo-dialog-demo"]')
        group_type.click()
        group_type.send_keys('News Group One')
        # time.sleep(3)
        # group_one = driver.find_element_by_name('News Group One')
        # group_one.click()
        review_button = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/button/span[1]')
        review_button.click()
        time.sleep(3)
        test = driver.find_element_by_xpath("//span[text()='Publish']")
        test.click()
        time.sleep(8)


