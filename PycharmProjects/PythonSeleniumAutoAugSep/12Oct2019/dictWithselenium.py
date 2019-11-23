from selenium import webdriver
import time


td = {"url":"https://www.google.com/",'browser':"ff"}

if td['browser']=="chrome":

    driver = webdriver.Chrome("/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/chromedriver")
elif td['browser']=="ff":
    driver = webdriver.Firefox(executable_path="/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/geckodriver")


driver.get(td['url'])
time.sleep(2)
# driver.quit()