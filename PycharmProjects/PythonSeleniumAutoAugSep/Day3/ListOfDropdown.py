

from selenium import webdriver

driver =webdriver.Chrome("/Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/driver/chromedriver")

driver.get("https://www.wikipedia.org/")

lang = driver.find_elements_by_xpath("//select[@id='searchLanguage']/option")

print("Total no of Lang is", len(lang))


emptyList =[]



print("Empty List",emptyList)

for lan in lang:
    emptyList.append(lan.text)



print("Empty List unSorted",emptyList)

emptyList.sort()

print("Empty List Sorted",emptyList)

emptyList.sort(reverse=True)
print("Empty List reverse Sorted",emptyList)
driver.quit()
