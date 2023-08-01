import time
import webbrowser
from conftest import driver, web_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import email, password,phone, temp_email

base_url = 'https://b2c.passport.rt.ru'

def test_new_user_by_email(driver):      # Регистрация нового пользователя по E-mail
    driver.get(base_url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'kc-register')))        # Ожидание загрузки страницы
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"     # Проверяем, что оказались на главной
    driver.find_element(By.ID, 'kc-register').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    driver.find_element(By.NAME, 'firstName').send_keys('Иван')
    driver.find_element(By.NAME, 'lastName').send_keys('Иванов')
    driver.find_element(By.ID, 'address').send_keys(temp_email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password)
    time.sleep(4)
    driver.find_element(By.NAME, 'register').click()
    time.sleep(4)
    assert driver.find_element(By.LINK_TEXT, 'Пароли не совпадают')

def test_new_user_by_phone(driver):      # Регистрация нового пользователя по номеру телефона
    driver.get(base_url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'kc-register')))
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Авторизация"
    driver.find_element(By.ID, 'kc-register').click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1')))
    driver.find_element(By.NAME, 'firstName').send_keys('Иван')
    driver.find_element(By.NAME, 'lastName').send_keys('Иванов')
    driver.find_element(By.ID, 'address').send_keys(phone)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'password-confirm').send_keys(password)
    time.sleep(4)
    driver.find_element(By.NAME, 'register').submit()
    time.sleep(4)
    assert driver.find_element(By.LINK_TEXT, 'Пароли не совпадают')

def test_auth_user(driver):     # Авторизация уже созданного пользователя
    driver.get(base_url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element(By.ID, 'username').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    assert driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"

def test_register_name_last_name(driver):      # Проверка полей "Имя" и "Фамилия" при регистрации
    driver.get(base_url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "Регистрация"
    time.sleep(3)

    # Тест-кейс TC-RosTel-002
    driver.find_element(By.NAME, 'register').click()      # Проверка обязательности полей
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

    driver.find_element(By.NAME, 'firstName').send_keys('А')       # Принимает ли одно значение
    driver.find_element(By.NAME, 'lastName').send_keys('А')
    driver.find_element(By.NAME, 'register').click()
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
