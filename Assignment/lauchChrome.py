from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(executable_path= ChromeDriverManager().install(),chrome_options=option)
driver.get('https://www.icicibank.com/')
