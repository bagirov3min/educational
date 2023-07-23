from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://www.citilink.ru/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

name_try = [
    "Ноутбуки",
    "Смартфоны",
    "Телевизоры",
    "Мониторы",
    "Процессоры",
    "Садовая техника",
    "Стиральные машины",
    "Климатическая техника",
    "Холодильники",
    "Компьютеры",
]
name_elements = []
for index in range(10):
    elements_by_citilink = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "div[class*=app-catalog-1ljlt6q]>a")
        )
    )
    elements_by_citilink[index].click()
    check = (
        WebDriverWait(browser, 15)
        .until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1[class*=e1gjr6xo0]"))
        )
        .text
    )
    name_elements.append(check)
    time.sleep(1)
    browser.back()
assert name_elements == name_try, f"Test not successful: {name_elements}"
browser.quit()
