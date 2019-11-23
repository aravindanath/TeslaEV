#     Key : value
car = {"Model":"2019","colour":"red"}
print(type(car))
print(car)
car.pop("Model")
print(car)

car["cc"]="2000";
print(car)
print(car.keys())
print(car.values())

for i in car.items():
    print(i)

    break