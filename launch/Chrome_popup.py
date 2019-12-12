from selenium.webdriver import Chrome

# /Users/aravindanathdm/Documents/TeslaEV/PycharmProjects/PythonSeleniumAutoAugSep/driver/chromedriver
# winPath = "..\\driver\\chromedriver.exe"
# For MAC
# Relative path
path = "../mydriver/chromedriver.exe"

driver = Chrome(executable_path=path)
