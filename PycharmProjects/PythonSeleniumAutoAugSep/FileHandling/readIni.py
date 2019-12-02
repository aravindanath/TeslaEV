from configparser import ConfigParser as config

parser = config()
parser.read("./TestData.ini")

url = parser.get("TC001","url")

print(url)