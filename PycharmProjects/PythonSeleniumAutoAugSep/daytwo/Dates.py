from datetime import datetime
import time

print(datetime.now())
dt = str(datetime.now()).replace("-","_").replace(" ","_").replace(":","_").split(".")[0]

print(dt)



fileName =  "Demo"+dt+".txt"
print(fileName)

print(time.time())
print(round(time.time()))



num1 = 20
num2 = 7
print(num1/num2)
print(round(num1//num2))

print(round(1.8))