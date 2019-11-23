#        KEY : Value
cars = {"browser":"chrome","url":"https://www.google.com","search":"selenium jobs in bangalore"}


bike= {}
print(cars.keys())
print(cars.values())

cars.pop("search")
print(cars)

bike = cars.copy()
bike["Wheel"]='2'
print(bike)
#
#
# for c in cars.items():
#     print(c)