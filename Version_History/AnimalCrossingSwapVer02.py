# Animal Crossing Island Helper Ver02
# Gisele Fox 3/25/2020
# Description:  This program will help me decide whcih fish to keep
#               and which to toss (based on price) when on an island
#               in Animal Crossing



## HOW WOULD I DO IT NORMALLY

# open the browser to se big and fish sites
# catch a bf
# just put it away if inventory isn't full
# It it's full i need to swap it out
# check the bf webistes for current bf price
# check my bfs in inventory and all their prices
# If the bf in hand is worth more than one in my inventory, find the least valuable one and swap it out




def main():



    # read file and make a master list of the the bf/prices
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
    print("=== ALTERNATE ENTRIES ===")
    print("'FULL' when your inventory is full")
    print("'DONE' when you are done with the program")


    # Create while loop so we can add and swap indefinitely
    while blnOnTheIsland == True:

        # User Input bug/fish caught
        strCurrentName = str(input("What did you catch?: "))


        # Check to see if inventory is full
        if strCurrentName == "FULL":
            blnInventoryFull = True
            print("We will commence swapping")
            print()

        # Check to see if user is done
        elif strCurrentName == "DONE":
            blnOnTheIsland = False
            

        # Else assume it's a name of a creature
        else:

            # Search it up using index to figure out price
            intIndexCurrentBF = int(lstBFName.index(strCurrentName))
            intCurrentPrice = int(lstBFPrice[intIndexCurrentBF])
            

            # add the bug to inventory if inventory not full
            if blnInventoryFull == False:
                mlstInventory[0].append(strCurrentName)
                mlstInventory[1].append(intCurrentPrice)
                print(mlstInventory)
                


            # Initiate smallest price if we end up swappin stuff
            intCheapestPrice = mlstInventory[1][0]

            # if inventory is full, find the lowest prices BF in inventory 
            if blnInventoryFull == True:

                # Go through each price in inventory
                for price in mlstInventory[1]:

                    # Find the cheapest price
                    if price < intCheapestPrice:
                        intCheapestPrice = price
                        intCheapestIndex = mlstInventory.index(price)

                # Swap out if the current BF is pricier
                if intCurrentPrice > intCheapestPrice:
                    print("You should swap", strCurrentName, "for", mlstInventory[0][intCheapestIndex])

                    # Swap out the name and price
                    mlstInventory[0][intCheapestIndex] = strCurrentName
                    mlstInventory[1][intCheapestIndex] = intCurrentPrice

                # if current BF isn't pricier then just don't do anything
                else:
                    print("Throw it away, you don't have anything worse")
                    
                    
    

main()



### TEST DATA

