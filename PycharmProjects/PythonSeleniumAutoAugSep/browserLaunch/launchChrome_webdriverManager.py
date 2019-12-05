from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
# d = webdriver.Firefox(GeckoDriverManager.install())

# https://github.com/SergeyPirogov/webdriver_manager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in")


