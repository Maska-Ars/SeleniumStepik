from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
    email.send_keys("test@example.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()