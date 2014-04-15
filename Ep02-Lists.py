#! usr/bin/env python

companions = ['Sarah Jane Smith','Leela','Rose Tyler']

for companion in companions:

	print 'The Doctor once traveled with', companions.pop(0) + '.'

  

raw_input("Press Enter to Exit")

# Looping through an array
# for companion in companions:
# 
#   print 'The Doctor once traveled with', companion + '.'

#A few ways to manipulate lists

#companions.append('Martha Jones') #add one new item to the list
#companions.extend(['Clara Oswald','Mickey Smith']) #add multiple new items to the list
#del companions[0] #delete items from a list
#companions.pop(0) #delete an item while using it
