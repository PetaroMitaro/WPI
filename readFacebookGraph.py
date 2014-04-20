import json
from pprint import pprint

json_file=open('roomate_data.json','r')
data=json.load(json_file)
content = data['data']
#pprint(content)
for post in content:
    print(post['message'])
    
