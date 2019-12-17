from launch import chrome as op

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

op.driver.get(("//https:www.amazon.in/"))
op.driver.fullscreen_window()
search=op.driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys("headphones",Keys.ENTER)

time.sleep(2)
search=op.driver.find_element(By.ID,"twotabsearchtextbox")
search.clear()
search.send_keys("Leather jaket",Keys.ENTER)
time.sleep(2)

op.driver.close()