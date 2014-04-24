text_file = open("/Users/dchase/Desktop/text_file.txt", "r") #Creates a reference to our file, for "r" reading

textFromFile = text_file.read() #Reads our entire file into a variable as a string

foes = textFromFile.split(',') #split() uses the , in our string to create an array
		
for foe in foes:
	
	if foe == 'Joker':
		print 'Why so serious?'
	else:
		print foe
		
		
# for i in range(0,len(foes)):	#iterate over a range of numeric values
# 		
# 	if foes[i] == 'Deathstroke': 
# 	
# 		print 'Slade. The one-eyed wonder.'
# 		
# 	elif foes[i] == 'Clayface':
# 		
# 		print "Clayface. Easily bent out of shape."
# 
# 	else: 
# 	
# 		print foes[i]

# for index, value in enumerate(foes): # iterate over the array while having access to the current index and current value
# 
#   if value == 'Bane':
#     print 'Bane. The man who broke the bat.'
#   else:
#     print foes[index]
# 		
