import requests

# 1. import the requests library
url = "https://jsonplaceholder.typicode.com/posts"
# 2. define the url to be used 
params = {"userId": 1}
# 3. define the parameters to be used
response = requests.get(url, params=params)
# 4. make the request
print(response.json()[0].get("body"))