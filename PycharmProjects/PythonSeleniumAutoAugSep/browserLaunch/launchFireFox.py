from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Firefox

# /Users/aravindanathdm/Documents/TeslaEV/PycharmProjects/PythonSeleniumAutoAugSep/driver/chromedriver
# winPath = "..\\driver\\chromedriver.exe"
# For MAC
# Relative path

path = "../driver/geckodriver"

driver = Firefox(executable_path=path)
