from DbOperations import DbOperations
import csv

db = DbOperations()
db.create_DB()


def userInput():
    print(
        """
    What do you want to do?
    0. exit
    1. Add purchase
    2. Add Sale
    3. View all owned
    4. Import
    5. Export
    """
    )

    inputNumber = int(input("Number 0-5: "))
    if inputNumber == 0:
        print("Good Buy.")
        return
    elif inputNumber == 1:
        addPurchase()
    elif inputNumber == 2:
        addSale()
    elif inputNumber == 3:
        printAll()
    elif inputNumber == 4:
        importData()
    else:
        print("Chose a valid number")

    userInput()


def addPurchase():
    print("Add Purchase")

    # date = input("date 'yy mm dd': ")
    date = "21/02/01"
    name = input("name: ")
    averagePrice = input("Average price: ")
    amount = input("Amount: ")
    currentPrice = input("CurrentPrice: ")
    db.write_to_db(date, name, averagePrice, amount, currentPrice)


def addSale():
    print("Add Sale")


def importData():
    print("import Data")
    with open("import.csv") as myData:
        for line in csv.DictReader(myData):
            date = "21/02/01"
            name = line["name"]
            averagePrice = line["avgPrice"]
            currentPrice = line["currentPrice"]
            amount = line["amount"]
            db.write_to_db(date, name, averagePrice, amount, currentPrice)


def printAll():
    print("View all owned")
    data = db.read_from_db()

    for line in data:
        print(line)


userInput()
