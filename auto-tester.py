from selenium import webdriver
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = browser.find_element_by_id("price")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element_by_id("book")
button.click()
x = int(browser.find_element_by_id("input_value").text)
input = browser.find_element_by_tag_name("input")
input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
submit2 = browser.find_element_by_css_selector("[type='submit']")
submit2.click()