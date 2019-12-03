#  pip3 install logging-py

# importing logging pkg
import logging

# #Create and configure logger
logging.basicConfig(filename="./demo.log",filemode='w',format='%(asctime)s %(message)s')

#Creating an object
log=logging.getLogger()

log.setLevel(logging.DEBUG)
log.info("User is learning logger!")

try:
    i = 10
    j = 0
    s =i/j
except ZeroDivisionError:
    log.exception("Number cant div by zero")

log.info("User learnt the logger")





