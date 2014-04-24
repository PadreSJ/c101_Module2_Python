#project2014-P002.py
#Lets determine some factors of a number

#First do some housekeeping

fac=int(1) #The factor test number
Factors = [] # Create an empty list for the factors to be stored in
findex = int(0) # Prime the list index variable

# Begin the adventure
# Ask for a number to factor and make it an interger
num = int(raw_input("Please give me a number: ")) 

print "The number you entered is: ", num

# Start the loop to find the factors
for x in range(1,num) : # Test for factors through the number itself

    if num%fac == 0: # Check for an even division
        print "A factor is: ", fac  # If the remainder is zero print the factor
        
        Factors[findex:] = [fac] # Place the factor into the list.
                            # This was tuff, you have to use [x:] to load the list
                            # Specifing a range x to the end
                            
        findex = findex + 1 # Add one to the index
        
        fac = fac + 1 # Add one to the factor test
        
    else:
       fac = fac + 1 # Add one to the factor test and restart
    
else:
    print " The list of factors is ", Factors
    print "all done" # We are all done 
raw_input() # To keep the window open on gui systems, as suggested by +Nevrin O
