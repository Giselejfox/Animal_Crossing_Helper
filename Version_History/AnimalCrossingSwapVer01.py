# Animal Crossing Island Helper Ver01
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

    # Initiate the lists
    lstBFName = []
    lstBFPrice = []
    mlstBFNamePrice = []

    for line in inFile:
        lstLine = line.split(" - ")
        lstBFName.append(lstLine[0])
        lstBFPrice.append(lstLine[1][:-1])
    inFile.close()

    mlstBFNamePrice.append(lstBFName)
    mlstBFNamePrice.append(lstBFPrice)

    # Initiate while loop 
    blnInventoryFull = False
    

    #   while 
    # Tell user to input FULL when they want to start swapping things out
    print("remember to enter FULL when your inventory is full")

    # User Input bug/fish caught
    strCurrentBF = str(input(What did you catch?: ))

    # Search it up to figure out price and record index
    lstBFName.index(strCurrentBF)


    # Initiate master bug inventory lists
    lstInvName = []
    lstInvPrice = []
    mlstInventory = []

    mlstInventory.append(lstInvName)
    mlstInventory.append(lstInvPrice)

    # add the bug to a list if inventory not full (include price by looking at big price list)
    if blnInventoryFull == False:
        
        

    # compare bug to inventory if inventory full

    # if the bug caught is more valuable then swap it out for the least valuable bug in the inventory

    # if can't find bug display error mesage

    
    




main()
