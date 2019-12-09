from selenium.webdriver import Chrome

# /Users/aravindanathdm/Documents/TeslaEV/PycharmProjects/PythonSeleniumAutoAugSep/driver/chromedriver
# winPath = "..\\driver\\chromedriver.exe"
# For MAC
# Relative path
path = "../driver/chromedriver"

driver = Chrome(executable_path=path)
driver.get("https://www.amazon.in/")