import function
import datetime
function.welcome_message()
continueLoop = True
while continueLoop == True:

    function.option_select_message()

    loop = False
    while loop == False:
        try:
            user_input = int(input("Enter a option: "))
            loop = True
        except:
            function.invalid_exception_message()
            function.option_select_message()

    if user_input == 1:
        function.rent_costume()
        function.display_rent()
        function.dictionary_rent()

        dictionaryCostume = function.dictionary_rent()

        rentCostumeID = function.valid_costume_ID()

        rentCostumeN = []
        rentCostumeB = []

        if int(dictionaryCostume[rentCostumeID][3]) > 0:
            function.costume_available()

            quantityOfCostume = function.rent_quantity_costume(int(dictionaryCostume[rentCostumeID][3]))
            dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - quantityOfCostume

            name = input("Enter the name of customer: ")
            todaysDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            rentCostumeN.append(dictionaryCostume[rentCostumeID][0])
            rentCostumeB.append(dictionaryCostume[rentCostumeID][1])

            function.stock_costume(dictionaryCostume)

            totalPrice = function.calculate_total_price(dictionaryCostume,quantityOfCostume,rentCostumeID)
            
            print("------------------------------------------------------------------------------------")
            print("Have the costumer rented another costume as well??")
            continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()

            loop = True
            while loop == True:
                if continueRent == "y":
                    function.rent_costume()
                    function.display_rent()
                    dictionaryCostume = function.dictionary_rent()
                    rentCostumeID = function.valid_costume_ID()

                    if int(dictionaryCostume[rentCostumeID][3]) > 0:
                        function.costume_available()

                        if dictionaryCostume[rentCostumeID][0] in rentCostumeN:
                            quantityOfCostume = function.rent_quantity_costume(int(dictionaryCostume[rentCostumeID][3])) + quantityOfCostume
                        
                        else:
                            rentCostumeN.append(dictionaryCostume[rentCostumeID][0])
                            rentCostumeB.append(dictionaryCostume[rentCostumeID][1])
                            quantityOfCostume = function.rent_quantity_costume(int(dictionaryCostume[rentCostumeID][3])) + quantityOfCostume

                        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) - quantityOfCostume
                        function.stock_costume(dictionaryCostume)

                        totalPrice = function.calculate_total_price(dictionaryCostume,quantityOfCostume,rentCostumeID) + totalPrice
                        print("==================================================")
                        print("Have the costumer rented another costume as well??")
                        continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()

                else:
                    function.rent_bill(name, todaysDate, totalPrice, rentCostumeN, rentCostumeB)
                    function.create_rent_detail(name, todaysDate, totalPrice, rentCostumeN, rentCostumeB)
                    loop = False
                    
        else:
            function.costume_unavailable()
        
    elif user_input == 2:
        function.return_costume()
        function.display_rent()
        dictionaryCostume = function.dictionary_rent()
        rentCostumeID = function.valid_Costume_ID()

        rentCostumeN = []
        rentCostumeB = []

        quantityOfCostume = function.return_quantity_costume(int(dictionaryCostume[rentCostumeID][3]))
        dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) + quantityOfCostume

        name = input("Enter the name of customer: ")
        todaysDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        rentCostumeN.append(dictionaryCostume[rentCostumeID][0])
        rentCostumeB.append(dictionaryCostume[rentCostumeID][1])

        function.stock_costume(dictionaryCostume)

        days = int(input("Enter the Number of Days the costume was rented: "))

        fine = 0
        lateDay = 0
        fineNo = 10
        if days > 5:
            lateDay = days - 5
            fine = lateDay * fineNo * quantityOfCostume
            print("The total amount of fine is:", fine)
        
        print("==================================================")
        print("Have the costumer rented another costume as well??")
        continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()

        loop = True
        while loop == True:
            if continueRent == "y":
                function.return_costume()
                function.display_rent()
                dictionaryCostume = function.dictionary_rent()
                rentCostumeID = function.valid_costume_ID()
                
                function.costume_available()

                if dictionaryCostume[rentCostumeID][0] in rentCostumeN:
                    quantityOfCostume = function.return_quantity_costume(int(dictionaryCostume[rentCostumeID][3])) + quantityOfCostume
                    dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) + quantityOfCostume
                        
                else:
                    rentCostumeN.append(dictionaryCostume[rentCostumeID][0])
                    rentCostumeB.append(dictionaryCostume[rentCostumeID][1])
                    quantityOfCostume = function.return_quantity_costume(int(dictionaryCostume[rentCostumeID][3])) + quantityOfCostume
                    dictionaryCostume[rentCostumeID][3] = int(dictionaryCostume[rentCostumeID][3]) + quantityOfCostume

                function.stock_costume(dictionaryCostume)

                fine = (lateDay * fineNo * quantityOfCostume) + fine
                print("The total amount of fine is:", fine)

                print("==================================================")
                print("Have the costumer rented another costume as well??")
                continueRent = input("Please enter 'y' if another costume has been rented else provide any other value: ").lower()

            else:
                function.return_bill(name, todaysDate, days, fine, rentCostumeN, rentCostumeB)
                function.create_return_detail(name, todaysDate, days, fine, rentCostumeN, rentCostumeB)
                loop = False

    elif user_input == 3:
        function.thank_you_message()
        continueLoop = False

    else:
        function.invalid_message()
