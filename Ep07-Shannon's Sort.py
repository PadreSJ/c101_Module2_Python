print "Who has RSVP'd to my wedding as a yes or a no?"

#open and read the file
text_file = open("C:\Users\Shannon\Desktop\Shannon's Stuff\Python\ExampleEp15Shannon.txt", "r")

WeddingRSVP = text_file.read()

Names = WeddingRSVP.split(",")

for Guest in Names:
    print Guest

raw_input("Press Enter to Continue")

#sort them
Names.sort();

for Guest in Names:
    print Guest

#write sorted list out to file
    text_file = open("C:\Users\Shannon\Desktop\Shannon's Stuff\Python\ExampleEp17ShannonWrite.txt", "a")

    text_file.write(Guest + "\n")
    text_file.close()

print "Guest are now sorted alphabetically in new file"

raw_input("Press Enter to Exit")
