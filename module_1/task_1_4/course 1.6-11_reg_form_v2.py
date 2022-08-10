from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

try:
    # link = "http://suninjuly.github.io/registration1.html" #первая форма регистрации
    link = "http://suninjuly.github.io/registration2.html" #обновленная форма регистрации
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.first') #обязательное поле для ввода 'First name'
    first_name.send_keys('Полиграф')  #заполнение поля
    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block input.second') #обязательное поле для ввода 'Last name'
    last_name.send_keys('Шариков') #заполнение поля
    email = browser.find_element(By.CSS_SELECTOR, '.first_block input.third') #обязательное поле для ввода 'Email'
    email.send_keys('abyr@valg.ru') #заполнение поля

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()