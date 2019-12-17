from PycharmProjects.PythonSeleniumAutoAugSep.browserLaunch import launchChrome as op
import time
from selenium.webdriver.common.keys import Keys
op.driver.get("https://www.google.com/")

op.driver.find_element_by_link_text("मराठी").click()
op.driver.find_element_by_name("q").send_keys("news",Keys.ENTER)

time.sleep(2)
op.driver.quit()