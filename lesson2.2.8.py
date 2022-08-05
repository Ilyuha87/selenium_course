from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    input1.send_keys("Ilya")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]')
    input2.send_keys("Bobrov")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]')
    input3.send_keys("Bobrov@gmail.com")
    file_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file.txt")
    file_button.send_keys(file_path)
    send_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    send_button.click()

finally:
    time.sleep(5)
    browser.quit()










