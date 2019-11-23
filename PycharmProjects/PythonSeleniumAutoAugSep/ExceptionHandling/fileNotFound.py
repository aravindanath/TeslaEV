
print("Starting..")

print("Open DB connection..")
try:
    f = open("/user/demo.txt",'r')
    f.readline()
except FileNotFoundError:
    print("Enjoy file not found exception!")
    # raise Exception
except ZeroDivisionError:
    print("Enjoy zero div exception!")

except :
    print("Enjoy exception!")

finally:
    print("Close DB connection..")


print("Ending..")
