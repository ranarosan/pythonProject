import datetime
def welcome_message():
    print("\n")
    print("--------------------------------------------------")
    print("|\tWelcome to Costume Rental Application    |")
    print("--------------------------------------------------")
    print("\n")

def option_select_message():
    print("Select a desirable option.")
    print("(1) || Press 1 to rent a costume.")
    print("(2) || Press 2 to return a costume.")
    print("(3) || Press 3 to exit.\n")

def thank_you_message():
    print("\nThank You for using our application.\n")

def invalid_message():
    print("\nIvalid input")
    print("\nPlease select the value as per the provied options\n")

def rent_costume():
    print("\n\t\t\t\t\tRent")

def costume_available():
    print("---------------****--------------")
    print("|\tCostume is available\t|")
    print("---------------------------------")
    print("\n")

def costume_unavailable():
    print("\n-----------------------------------")
    print("Costume is not available")
    print("------------------------------------\n")

def invalid_exception_message():
    print("********************************************")
    print("Invalid option! Please provide valid option")
    print("********************************************")


def display_rent():
    file = open("costumes.txt","r")
    print("----------------------------------------------------------------------------------")
    print("|\tID \tCustomer Name\t\t\tCustome Brand\tPrice   Quantity |")
    print("----------------------------------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print("\t", counterID, "\t" + line.replace(",","\t"))
    print("----------------------------------------------------------------------------------")
    file.close()


def dictionary_rent():
    file = open("costumes.txt", "r")
    counterID = 0
    dictionaryCostume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')

        dictionaryCostume[counterID] =  line

    return dictionaryCostume
    file.close()


def return_costume():
    print("\n\t\t\t\t\tReturn")

def valid_Costume_ID():
    exceptionIs = False
    while exceptionIs == False:
        try:
            validCostumeID = int(input("Enter the ID of costume you want to return: "))
            exceptionIs = True
        except:
            invalid_exception_message()
    
    while validCostumeID <= 0 or validCostumeID > len(dictionary_rent()):
        print("\nPlease provide a valid costume ID !\n")
        display_rent()
        validCostumeID = int(input("\nEnter the ID of costume you want to return: "))
    return validCostumeID


def valid_costume_ID():
    exceptionIs = False
    while exceptionIs == False:
        try:
            validCostumeID = int(input("Enter the ID of costume you want to rent: "))
            exceptionIs = True
        except:
            invalid_exception_message()
    
    while validCostumeID <= 0 or validCostumeID > len(dictionary_rent()):
        print("\nPlease provide a valid costume ID !\n")
        display_rent()
        validCostumeID = int(input("\nEnter the ID of costume you want to rent: "))
    return validCostumeID

def rent_quantity_costume(stockQuantity):
    exceptionIs = False
    while exceptionIs == False:
        try:
            quantityOfCostume = int(input("\nEnter the quantity of costume: "))
            exceptionIs = True
        except:
            invalid_exception_message()

    while quantityOfCostume <=0 or quantityOfCostume > stockQuantity:
        if quantityOfCostume <= 0:
            print("\n-----------------------------------------")
            print("Please provide valid qauntity as input")
            print("-----------------------------------------\n")
        else:
            print("\n-----------------------------------------")
            print("Provied quantity is greater than the quantity in stock")
            print("-----------------------------------------\n")

        exceptionIs = False
        while exceptionIs == False:
            try:
                quantityOfCostume = int(input("\nEnter the quantity of costume: "))
                exceptionIs = True
            except:
                invalid_exception_message()
    return quantityOfCostume

def return_quantity_costume(c):
    exceptionIs = False
    while exceptionIs == False:
        try:
            quantityOfCostume = int(input("\nEnter the quantity of costume: "))
            exceptionIs = True
        except:
            invalid_exception_message()

    while quantityOfCostume <=0:
        if quantityOfCostume <= 0:
            print("\n-----------------------------------------")
            print("Please provide valid qauntity as input")
            print("-----------------------------------------\n")
        exceptionIs = False
        while exceptionIs == False:
            try:
                quantityOfCostume = int(input("\nEnter the quantity of costume: "))
                exceptionIs = True
            except:
                invalid_exception_message()
    return quantityOfCostume

def stock_costume(dictionary):
    file = open("costumes.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()

def calculate_total_price(dictionary, quantityDetails, costumeID):
    price = float(dictionary[costumeID][2].replace("$",""))
    print("The price of the is costume:", price)
    pricePerItem = price * quantityDetails
    return pricePerItem

def rent_bill(name, todaysDate, totalPrice, rentCostumeName, rentCostumeBrand):
    print("\n")
    print("------------------------------------------------------------------------")
    print("\t\t\tRent Bill Details")
    print("------------------------------------------------------------------------\n")
    print("\t\t Costume Rental Application\n")
    print("\t\t Baneshwor, Kathmandu | 9840987891\n")
    print("\t\t Email: costumerentalapp101@gmail.com\n")
    print("\t\t PAN NO: <AAAAA8875AAA>\n")
    print("\t\t VAT NO: 001673\n")
    print("------------------------------------------------------------------------\n")
    print("Costumer Name:", name.upper())
    print("Date/time:", todaysDate)
    print("Total price:", totalPrice)
    print("Costume rented are:")
    for x in range(len(rentCostumeName)):
        print(str(x+1) + ". " + rentCostumeName[x] + ":- " + rentCostumeBrand[x])
    print("------------------------------------------------------------------------\n")

def create_rent_detail(cname, date, total, costumeName, costumeBrand):
    fileName = "Rent_" + cname + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"

    file = open(fileName, "w")
    file.write("------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tRent Bill Details\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t Costume Rental Application\n")
    file.write("\t\t\t\t\t Baneshwor, Kathmandu | 9840987891\n")
    file.write("\t\t\t\t\t Email: costumerentalapp101@gmail.com\n")
    file.write("\t\t\t\t\t PAN NO: <AAAAA8875AAA>\n")
    file.write("\t\t\t\t\t VAT NO: 001673\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Costumer Name: " + cname.upper() + "\n")
    file.write("Date/time: " + str(date) + "\n")
    file.write("Total price: " + str(total) + "\n")
    file.write("Costumes rented are: " + "\n")
    for i in range(len(costumeName)):
        file.write(str(i+1) + ". " + costumeName[i] + ":- " + costumeBrand[i] + "\n")
    file.write("------------------------------------------------------------------------\n")
    file.close()

def return_bill(name, todaysDate, days, fine, costumeName, costumeBrand):
    print("\n")
    print("\n------------------------------------------------------------------------")
    print("\t\t\tReturn Bill Details")
    print("------------------------------------------------------------------------\n")
    print("\t\t Costume Rental Application\n")
    print("\t\t Baneshwor, Kathmandu | 9840987891\n")
    print("\t\t Email: costumerentalapp101@gmail.com\n")
    print("\t\t PAN NO: <AAAAA8875AAA>\n")
    print("\t\t VAT NO: 001673\n")
    print("------------------------------------------------------------------------\n")
    print("Costumer Name:", name.upper())
    print("Date/Time:", todaysDate)
    print("Total NO of days:", days)
    print("Fine Amount:", fine)
    print("Costume rented are:")
    for i in range(len(costumeName)):
        print(str(i+1) + ". " + costumeName[i] + ":- " + costumeBrand[i])
    print("------------------------------------------------------------------------\n")

def create_return_detail(cname, date, days, fine, costumeName, costumeBrand):
    fileName = "Return_" + cname + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"

    file = open(fileName, "w")
    file.write("------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tReturn Bill Details\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t Costume Rental Application\n")
    file.write("\t\t\t\t\t Baneshwor, Kathmandu | 9840987891\n")
    file.write("\t\t\t\t\t Email: costumerentalapp101@gmail.com\n")
    file.write("\t\t\t\t\t PAN NO: <AAAAA8875AAA>\n")
    file.write("\t\t\t\t\t VAT NO: 001673\n")
    file.write("------------------------------------------------------------------------\n")
    file.write("Costumer Name: " + cname.upper() + "\n")
    file.write("Date of returned: " + str(date) + "\n")
    file.write("Total No of days:" + str(days))
    file.write("Fine Amount: " + str(fine) + "\n")
    file.write("Costumes rented are: " + "\n")
    for x in range(len(costumeName)):
        file.write(str(x+1) + ". " + costumeName[x] + ":- " + costumeBrand[x] + "\n")
    file.write("------------------------------------------------------------------------\n")
    file.close()
