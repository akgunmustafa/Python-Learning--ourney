import getpass

database = {"b": "654321", "c": "123", "a": "123"}  #In-memory database

username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
x = len(database)

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("! Enter Your Password Again : ")
        break

for x, y in database.items():
    if username == x and password == y:
        print("verified")