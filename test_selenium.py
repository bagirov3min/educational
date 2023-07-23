from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.ozon.ru/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "input[class*=u8v]"))
)
search_string.send_keys("Мебель")
button = browser.find_element(By.CSS_SELECTOR, "span[class*=a2-f0]").click()
check = (
    WebDriverWait(browser, 10)
    .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*=t5z]")))
    .text
)
the_search = "По запросу мебель найден 1 товар"
assert check == the_search, f"Test not successful: {check}"

browser.quit()
