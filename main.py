dataBase = []

from lib import User

def getData():
    i_name = input("Name:")
    i_surname = input("Surname:")
    i_username = input("Username:")
    i_password = input("Password:")
    return (i_name, i_surname, i_username, i_password)


def addUserToDataBase():
    dataBase.append(User(*getData()))


def userRegister():
    userCount = int(input("Type your user count:"))
    for count in range(userCount):
        count+=1
        print(f"Add {count} user data:")
        addUserToDataBase()


def showAllUsers():
    for user in dataBase:
        user.showUserData()


def filterUser():
    pass


order = int(input("To start register type 1 :"))
if order == 1:
    userRegister()
