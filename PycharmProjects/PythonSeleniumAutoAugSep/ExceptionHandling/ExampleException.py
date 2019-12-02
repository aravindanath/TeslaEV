

print("Good morning")

try:
    i = 10
    j = 0
    print(i / j)

except ZeroDivisionError:
    print("Num cant div by zero")

finally:

    print("Closing file")


print("Bye")