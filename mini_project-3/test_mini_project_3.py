import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.title("TC-1: Successful login")
@pytest.mark.positive
def test_mini_project():
    driver=webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    user_name=driver.find_element(By.ID,"username")
    user_name.send_keys("augtest_040823@idrive.com")
    password=driver.find_element(By.ID,"password")
    password.send_keys("123456")
    sign_in=driver.find_element(By.ID,"frm-btn")
    sign_in.click()
    time.sleep(10)
    assert driver.find_element(By.CLASS_NAME,"id-card-title").is_displayed()==True


