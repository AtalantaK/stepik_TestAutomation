from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищем кнопку и нажимаем на неё
    my_button = browser.find_element_by_css_selector("[type='submit']")
    my_button.click()

    # нажимаем на ОК в всплывающем окне
    confirm = browser.switch_to.alert
    confirm.accept()

    # считываем значение x и высчитываем значение по формуле
    x_1 = browser.find_element_by_css_selector("[id='input_value']")
    x = x_1.text
    y = calc(x)

    # записываем полученное значение в форму
    my_answer = browser.find_element_by_css_selector("[id='answer']")
    my_answer.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
