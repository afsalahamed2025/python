import mysql.connector
from  tabulate import tabulate


con = mysql.connector.connect(host='localhost',
                              user='root',
                              password='root',
                              database='conneted')

def insert(name,age,place):
  res=con.cursor()
  sql="insert into connt(name,age,place)values(%s,%s,%s)"
  user=(name,age,place)
  res.execute(sql,user)
  con.commit()
  print("insert successfully:)")



while True:
    print("1. add data")
    choice=int(input("enter"))

    if choice ==1:
        name=input("enter the name :")
        age = input("enter age")
        place=input("enter place")
        insert(name,age,place)

    else:
        print("no")
