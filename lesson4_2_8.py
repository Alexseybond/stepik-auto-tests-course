from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x: int):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

message1 = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
button1 = browser.find_element(By.ID, "book")
button1.click()

text1 = browser.find_element(By.ID, "input_value")
text2 = text1.text
y = calc(text2)

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)

button3 = browser.find_element(By.ID, 'solve')
button3.click()


#assert "successful" in message.text