from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# /Users/aravindanathdm/Documents/TeslaEV/PycharmProjects/PythonSeleniumAutoAugSep/driver/chromedriver
# winPath = "..\\driver\\chromedriver.exe"
# For MAC
# Relative path

path = "../driver/chromedriver"
ops = ChromeOptions()
# ops.add_argument("--headless")
ops.add_argument("--disable-notifications")
driver = Chrome(executable_path=path,chrome_options=ops)
# driver.get("https://www.amazon.in/")