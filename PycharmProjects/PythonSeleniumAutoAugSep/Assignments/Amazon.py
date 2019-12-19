from PycharmProjects.PythonSeleniumAutoAugSep.browserLaunch import launchFireFox as op
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

op.driver.get(("https:www.amazon.in/"))

# op.driver.fullscreen_window()

# search = op.driver.find_element(By.ID, "twotabsearchtextbox")

search =  op.driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("headphones", Keys.ENTER)

time.sleep(2)
search=op.driver.find_element(By.ID,"twotabsearchtextbox")
search.clear()

search.send_keys("Leather jacket", Keys.ENTER)

time.sleep(2)

op.driver.close()

