#        KEY : Value
cars = {"browser":"ff","url":"https://www.google.com","search":"selenium jobs in bangalore"}

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if cars["browser"] == "chrome":
    driver= webdriver.Chrome(executable_path="/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/chromedriver")
elif cars["browser"] == "ff":
    driver = webdriver.Firefox(executable_path="/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/geckodriver")

driver.get(cars["url"])

driver.find_element_by_name("q").send_keys(cars["search"],Keys.ENTER)


