from PycharmProjects.PythonSeleniumAutoAugSep.browserLaunch import launchChrome as op
import time

op.driver.get("https://www.icicibank.com/")

time.sleep(3)
try:
    op.driver.find_element_by_xpath("(//*[@id='modal-close'])[2]").click()
except:
    print("Fast Tag popup is not displayed")
time.sleep(2)
op.driver.find_element_by_class_name("pl-login-ornage-box").click()

print(op.driver.title)