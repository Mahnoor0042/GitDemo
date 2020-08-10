import requests as reqs
url = 'https://jsonplaceholder.typicode.com/todos/1'
response = reqs.get(url)        # To execute get request
print(response.status_code)     # To print http response code
print(response.text)