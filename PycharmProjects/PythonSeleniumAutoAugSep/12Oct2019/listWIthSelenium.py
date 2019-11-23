from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/chromedriver")

driver.get("https://www.wikipedia.org/")
lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")

print("Total no of Lang:", len(lang))
emptyLang =[]
for l in lang:
    emptyLang.append(l.text)


print("unsorted list",emptyLang)
emptyLang.sort()

print("sorted list",emptyLang)

emptyLang.sort(reverse=True)

print("reverse sorted list",emptyLang)
driver.close()