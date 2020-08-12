import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create(driver):
    wizard_button = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/span[1]')
    wizard_button.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            [By.XPATH, '//*[@id="scroll-dialog-description"]/div[1]/div[2]/div[2]/button/span[1]']))
    select_wizard = driver.find_element_by_xpath(
        '//*[@id="scroll-dialog-description"]/div[1]/div[2]/div[2]/button/span[1]')
    select_wizard.click()
    select_android = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div/div[3]/div/div/div/div/div/div[1]/div[1]/span[1]')
    select_android.click()
    radio_button = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div[2]/div[2]/div[3]/div[5]/div/div[5]/div/div/div/div/div/div[1]/div[1]/fieldset/div/label[2]/span[1]/span[1]/input')
    radio_button.click()


