from configparser import ConfigParser as config

con = config()
title = "TC001"
con[title]={'name':'Arvind '}


with open("./TestData.ini",'a') as t:
    con.write(t)


