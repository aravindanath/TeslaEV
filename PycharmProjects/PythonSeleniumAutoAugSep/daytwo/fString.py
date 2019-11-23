
city = "ercod"
event =  "mountin climbing"

string = "In %s on sunday %s will commence at 6am"%(city,event)

#  python 3 onwards

fString =  f"In {city} on sunday {event} will commence @ 6am ".format()
# fString  =  f"{city.upper()},{event.lower()}".format()

val = "This {} is written in {}".format("article","Golang")
print(val)
print("*"*10)
print(string)
print("*"*10)
print(fString)