import urllib #importing to use its urlencode function
import urllib2 #for making http requests
import json #for decoding a JSON response

API_KEY = open("/Users/dchase/Desktop/APIKey.txt", "r") #Creates a reference to our file, for "r" reading
API_KEY = API_KEY.read() #Reads our entire file into a variable as a string

searchTerm = raw_input('Search for a video: ')

searchTerm = urllib.quote_plus(searchTerm) #turns non word characters into url-safe characters

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q='+searchTerm+'&key='+API_KEY 

response = urllib2.urlopen(url) #makes the call to YouTube

videos = json.load(response) #decodes the response so we can work with it

videoMetadata = [] #declaring our list

for video in videos['items']:
	
  if video['id']['kind'] == 'youtube#video':
    videoMetadata.append(video['snippet']['title']+
    "\nhttp://youtube.com/watch?v="+video['id']['videoId']) #Appends each video title and link to our list

videoMetadata.sort(); # sorts our list alphabetcally

print "\nSearch Results:\n"

for metadata in videoMetadata:
  print metadata+"\n"


raw_input('Press Enter to Exit')
