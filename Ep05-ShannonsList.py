print "Who has RSVP'd to my wedding as a yes or a no?"

text_file = open("C:\Users\Shannon\Desktop\Shannon's Stuff\Python\ExampleEp15Shannon.txt", "r")

WeddingRSVP = text_file.read()

Names = WeddingRSVP.split(",")

for Guest in Names:
    if Guest.find("Yes") != -1: 
        print Guest.split("-")[0],'has replied YES'
    elif Guest.find("Not replied") != -1:
        print Guest.split("-")[0],'has NOT REPLIED'
    else:
        print Guest.split("-")[0],'has replied No'

raw_input("Press Enter to Exit")
