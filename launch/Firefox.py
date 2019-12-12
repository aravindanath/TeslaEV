from selenium.webdriver import Firefox

# /Users/aravindanathdm/Documents/TeslaEV/PycharmProjects/PythonSeleniumAutoAugSep/driver/chromedriver
# winPath = "..\\driver\\chromedriver.exe"
# For MAC
# Relative path
path = "../mydriver/geckodriver.exe"

driver = Firefox(executable_path=path)
driver.get("https://www.amazon.in/")