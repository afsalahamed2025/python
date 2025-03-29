import mysql.connector
from tabulate import tabulate


cons = mysql.connector.connect(host='localhost', user="root", password='root', database='connected')



def insert(name, age, gender, city):
    res = cons.cursor()
    sql = "INSERT INTO connect (name, age, gender, city) VALUES (%s, %s, %s, %s)"
    user = (name, age, gender, city)
    res.execute(sql, user)
    cons.commit()
    print("Passenger Details Inserted Successfully! ")



def update(id, name, age, gender, city):
    res = cons.cursor()
    sql = "UPDATE connect SET name=%s, age=%s, gender=%s, city=%s WHERE id=%s"
    user = (name, age, gender, city, id)
    res.execute(sql, user)
    cons.commit()
    print("Passenger Details Updated Successfully! ")



def delete(id):
    res = cons.cursor()
    sql = "DELETE FROM connect WHERE id=%s"
    user = (id,)
    res.execute(sql, user)
    cons.commit()
    print("Passenger Deleted Successfully! ")



def select():
    res = cons.cursor()
    sql = "SELECT * FROM connect"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, ['ID', 'Name', 'Age', 'Gender', 'City'], tablefmt="grid"))



while True:
    print("\n===== Passenger Management System =====")
    print("1 = Insert Data")
    print("2 = Update Data")
    print("3 = Delete Data")
    print("4 = View All Data")
    print("5 = Exit")

    enter = int(input('\nEnter Your Choice: '))

    if enter == 1:
        name = input('Enter Your Name: ')
        age = input("Enter Your Age: ")
        gender = input("Enter Your Gender: ")
        city = input("Enter Your City: ")
        insert(name, age, gender, city)

    elif enter == 2:
        id = input("Enter Passenger ID to Update: ")
        name = input("Enter New Name: ")
        age = input("Enter New Age: ")
        gender = input("Enter New Gender: ")
        city = input("Enter New City: ")
        update(id, name, age, gender, city)

    elif enter == 3:
        id = input("Enter Passenger ID to Delete: ")
        delete(id)

    elif enter == 4:
        select()

    elif enter == 5:
        print("\nExiting... Thank You! ")
        cons.close()
        break

    else:
        print("\n Invalid Choice! Please Try Again.")