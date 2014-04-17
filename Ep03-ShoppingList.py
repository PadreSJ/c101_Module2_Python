# Simple Shopping List program to demonstrate use of Python lists
# Written on 04/10/2014 by Darryl Medley for Coding 101 on the TWiT network

# This program features a simple list edit feature. When an item name is entered that
# is already in the list, the program will ask if the item should be added to the list
# or if the existing entry should be changed or deleted.

# shopList is the main list but each entry in it is a 2-item sub-list containing the
# item name and the item quantity. If you were to manually create the list it would
# look like this: shopList = [["Eggs","1 doz."], ["Milk", "1 gal."]]. To access the 
# members of the main list and sub-list, you use 2 indexes: shopList[idx1][idx2]. The
# first index, idx1, points to the member of shopList to access. The second, idx2,
# points to the member of the sub-list. For example: print shopList[1][0] would print
# Milk (remember, list indexes ar 0-based).

shopList = []   # create an empty list that we can append to
lcaseList = []   # create a second list to use for case-insensitive comparisons
itemCount = 0

print "Shopping List"
print "For fun try entering the same item name more than once"
print 

# Main input loop: Get item names and quantities and add to main list
while True:
    itemCount+=1   # increment Shopping List line nbr
    itemName = raw_input("Enter name of item " + str(itemCount) + " (just press Enter when finished): ")
    if itemName == "":
        break   # exit the input loop if nothing entered for the item name
    
    itemQty = raw_input("Enter quantity of " + itemName + " to buy: ")

    # test to see if item has been previously entered using our case-insensitive list
    if (itemName.lower() in lcaseList):
        print itemName, "is already in your list"
        print "Add item to list (default), Change the item qty, Delete the item"
        optn = "x"   # int so the while loop is not skipped

        # get a valid Add / Change / Delete response
        while (optn != "") and (optn not in "ACD"):
            optn = raw_input("Enter A, C, or D: ")
            
            if optn == "":
                optn = "A"   # default to Add
            else:   # convert entry to upper-case so both lower-case and upper-case entries will work
                optn = optn[0].upper()   # [0] grabs just the first character in case a complete word is entered

        # Handle Change and Delete options
        if optn != "A":   # Change or Delete selected 
            itemIndex = lcaseList.index(itemName.lower())   # index of dupe item in the main list
            
            if optn == "C":   # Change -> update the quantity value
                # Tricky part: update the quantity value in the sub-list
                # This is how you change a list inside of another list
                shopList[itemIndex][1] = itemQty
                itemCount-=1   # decrement counter because an item is not being added
                print itemName, "updated"
            elif optn == "D":   # Delete -> remove item from the list
                shopList.pop(itemIndex)   # remove item from the Shopping List
                lcaseList.pop(itemIndex)  # remove item from the case-insensitive test list            
                itemCount-=2   # decrement counter because an item is not being added
                print itemName, "deleted"
    else:   # itemName was not found to be in the list already
        optn = "A"   # Item has not been previously entered. Set Add mode

    if optn == "A":   # Add mode - list item was not Changed or Deleted above
        # Tricky part: Store the Name / Qty pair as a little sub-list inside of the main list
        itemPair = [itemName, itemQty]   # Create the sub-list
        shopList.append(itemPair)   # add the sub-list to the main list
        lcaseList.append(itemName.lower())   # add lower-case item name to the test list
# end of item entry while loop  <- Pro Tip: end of block comments make code easier to follow

# Print the iist
print
print "Your Shopping List:"

# Loop through the main list
# - remember each entry in the main list is a 2 value sub-list: [item name, qty]
# Use a "for" loop that returns both the index and the value of each member of the main list
for itemIndex, itemPair in enumerate(shopList):
    # output the line # and the 2 values (item name, item qty) in the itemPair sub-list
    print str(itemIndex+1) + ":", itemPair[0] + ", Qty:", itemPair[1]

print 
raw_input("(press Enter to close)")
