# Animal Crossing Island Helper Ver06
# Gisele Fox 3/25/2020
# Description:  This program will help me decide whcih fish to keep
#               and which to toss (based on price) when on an island
#               in Animal Crossing


# TO DO for ver06:
"""
- be able to add fruits/coconuts to pockets before hand
- 
"""


def main():

    # read file and make a lists of the the bf names/prices
    inFile = open("CritterPrice.txt", "r")

    # Initiate the lists containing all BF names and prices
    lstBFName = []
    lstBFPrice = []

    for line in inFile:
        lstLine = line.split(" - ")
        lstBFName.append(str(lstLine[0]))
        lstBFPrice.append(int(lstLine[1][:-1]))
    inFile.close()
    

    # Initiate while loops
    blnInventoryFull = False
    blnOnTheIsland = True

    # Initiate master BF inventory lists
    lstInvName = []
    lstInvPrice = []
    mlstInventory = []

    mlstInventory.append(lstInvName)
    mlstInventory.append(lstInvPrice)

    # Tell user commands they need to know
    print()
    print("=== ALTERNATE ENTRIES ===")
    print("'FULL' when your inventory is full")
    print("'INV' when you want to see what's in your inventory so far")
    print("'TOT' when you want to see how much your inventory will sell for so far")
    print("'DONE' when you are done with the program")
    print()


    # Create while loop so we can add and swap indefinitely
    while blnOnTheIsland == True:

        # Try-except so program doesn't blow up if you type something wrong
        try:

            # User Input bug/fish caught
            strCurrentName = str(input(">>> What did you catch?: "))


            # Check to see if inventory is full
            if strCurrentName == "FULL":

                # Make it so we start comparing current bf to our inventory
                blnInventoryFull = True
                print()
                print("Now we'll start swapping")
                print()

            # Check if user is done
            elif strCurrentName == "DONE":

                # Initialize running total
                intSumPrices = 0
                
                # Add up all the prices to display
                for price in mlstInventory[1]:
                    intSumPrices += price

                print("Your catch should sell for", intSumPrices, "bells.")

                # Get out of while loop
                blnOnTheIsland = False

            # Check if user wants to see inventory
            elif strCurrentName == "INV":

                print()
                print("== CURRENT INVENTORY ==")

                # Go through all the items in the inventory and print their price
                for item in range(len(mlstInventory[0])):
                    print(mlstInventory[0][item],"-", mlstInventory[1][item])

                print()


            # Check id user wants to see what inventory will sell for so far
            elif strCurrentName == "TOT":

                # Initialize running total
                intSumPrices = 0
                
                # Add up all the prices to display
                for price in mlstInventory[1]:
                    intSumPrices += price

                print()
                print("Your catch should sell for", intSumPrices, "bells so far.")
                print()
                
                    

            # Else assume it's a name of a creature
            else:

                # Search it up using index to figure out price
                intIndexCurrentBF = int(lstBFName.index(strCurrentName))
                intCurrentPrice = int(lstBFPrice[intIndexCurrentBF])

                
                # if inventory is not full add the bug to inventory 
                if blnInventoryFull == False:
                    mlstInventory[0].append(strCurrentName)
                    mlstInventory[1].append(intCurrentPrice)

                    # print out price
                    print(strCurrentName, "-", intCurrentPrice)
                    print()

                # if inventory is full, find the lowest prices BF in inventory 
                if blnInventoryFull == True:

                    # Find the cheapest price and it's index in the inventory
                    lstInvPriceSorted = mlstInventory[1].copy()
                    lstInvPriceSorted.sort()
                    intIndexCheapest = mlstInventory[1].index(lstInvPriceSorted[0])

                    # Swap out if the current BF is pricier
                    if intCurrentPrice > lstInvPriceSorted[0]:

                        # Tell the user
                        print("You should swap", strCurrentName, "(" + str(intCurrentPrice) + ")",
                              "for", mlstInventory[0][intIndexCheapest], "(" + str(mlstInventory[1][intIndexCheapest]) + ")" )
                        print()

                        # Swap out the name and price
                        mlstInventory[0][intIndexCheapest] = strCurrentName
                        mlstInventory[1][intIndexCheapest] = intCurrentPrice

                    # if current BF isn't pricier then just don't do anything
                    else:
                        print("Let it go!")
                        print()

                
        except:

            #Error message
            print()
            print("***I think you miss-typed something, try again***")
            print()
                    
                    
    

main()
