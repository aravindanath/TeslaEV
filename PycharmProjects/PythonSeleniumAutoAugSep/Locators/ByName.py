from PycharmProjects.PythonSeleniumAutoAugSep.browserLaunch import launchChrome as op
from selenium.webdriver.common.keys import Keys
import time
op.driver.get("https://www.google.com")
op.driver.find_element_by_name("q").send_keys("Selenium jobs",Keys.ENTER)

time.sleep(2)
op.driver.quit()




