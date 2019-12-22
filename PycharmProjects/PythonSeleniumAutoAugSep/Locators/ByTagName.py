from PycharmProjects.PythonSeleniumAutoAugSep.browserLaunch import launchChrome as op
import time
from selenium.webdriver.common.keys import Keys


op.driver.get("https://www.google.com/")
links = op.driver.find_elements_by_tag_name("a")

print("Total no of links present on ",op.driver.current_url,len(links))

for li in links:
    print(li.text , li.get_attribute("href"))



time.sleep(2)
op.driver.quit()