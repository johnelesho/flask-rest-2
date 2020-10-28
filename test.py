import requests

BASE = "http://127.0.0.1:5000/"

import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 200, "name": "How to make Rest API", "views": 10000},
    {"likes": 100, "name": "How to program python", "views": 2000},
    {"likes": 100, "name": "Daniel", "views": 90000},

    
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i+10), data[i])
    print(response.json())
    input()

response = requests.delete(BASE + 'video/0')
print(response)
input()

response = requests.get(BASE + "video/2")
print(response.json())

# response = requests.get(BASE + "hello/John")

# response = requests.put(BASE + "video/204", {"likes": 10, "name": "John", "views": 200})
