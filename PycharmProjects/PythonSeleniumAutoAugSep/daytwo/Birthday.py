from datetime import datetime


birthday  = input("Enter the date (dd/mm/yyyy)")

birth_date =  datetime.strptime(birthday,'%d/%m/%Y')
print("Birthday " + str(birth_date))