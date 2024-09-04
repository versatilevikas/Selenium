from selenium import webdriver
import pytest
import allure
import time

from selenium.webdriver.common.by import By
@pytest.mark.positive
@allure.title(" Tests case 1 ")
@allure.description(" this is the description!!")
def test_sle():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment= driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()

@pytest.mark.negative
@allure.title(" Invalid login page ")
@allure.description(" this is the description!!")
def test_sle():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url=='https://app.vwo.com/#/login'
    email_webelement= driver.find_element(By.ID,"login-username")
    email_webelement.send_keys("admin@admin.com")
    password_webelement = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_webelement.send_keys("admin@admin.com")
    time.sleep(3)

@allure.title("Test Case 3: this is the third page")
@allure.description("this is the description ")
@pytest.mark.smoke

def test_open_vmologin():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    assert driver.current_url=='https://katalon-demo-cura.herokuapp.com/profile.php#login'

