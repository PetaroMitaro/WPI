import json
from pprint import pprint

#read file in
#I made this file by copying and pasting from the output
#of the facbeook graph API explorer
json_file=open('roomate_data.json','r')
#json parse
data=json.load(json_file)
#the file is structured with the overall 'data' object
#so we pull that out here
content = data['data']
#content itself is a list of JSON objects
#each object is a post, which is an ID, message, and other stupid stuff
messageList=[]
for post in content:
    #take each post and pull out the 'message' which is the actual post
    messageList.append(post['message'])
#messageList now contains a list of all the messages of the post

#Now we need to start using this data
#I'm thinking make a "user" object
#each user has a name, and a list of their responses
#that would be a pretty easy structure to use
#as for comparing answers, not sure yet, but I'm looking.
#try and add to this what you can with the 'user' objects and stuff
#I'm a good at object oriented programming but i'm shit at python :P
