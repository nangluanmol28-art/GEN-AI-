# W3D3
# from requests import delete 
# from requests import put 
import requests
import json
# 1. How to convert python data to JSON format and viceverca 
def json_lesson():
    print("---- 1. JSON Example -----\n")
    # JSON is a lightweight data interchange format.
    # In Python, JSON data structures map to dictionaries and lists.

    data = {
        "name": "Anmol SIngh",
        "age":  28,
        "is_student" : True,
        "courses": ["Math","computer science"]
    }

    # Convert Python dictionary to a JSON string (Serialization)
    # json.dumps() takes a Python object and returns a JSON formatted string.
    json_string = json.dumps(data,indent=4)# indent value means after how many spaces data apperes
    print("Serialized JSON String:")
    print(json_string)
    # Convert JSON string back to a Python dictionary (Deserialization)
    # json.loads() takes a JSON string and parses it into a Python dictionary.
    parsed_data = json.loads(json_string)
    print(f"Deserialized Data Type: {type(parsed_data)}")
    print(f"Accessing data: Name = {parsed_data['name']}")
    print("-" * 30 + "\n")


def requests_get_lesson():
    print(f"--- 2. REST API GET REQUESTS(fetching data )\n")
    # REST APIs allow programs to talk to each other over the internet using HTTP.
    # We will use JSONPlaceholder, a free fake API for testing.
    
    # The URL we want to send a GET request to
    url = f"https://jsonplaceholder.typicode.com/todos/1"
    print(f"Sending GET request to {url}...")
    response = requests.get(url)
    print(response.json())
    print(f"Status Code:{response.status_code}")
    if response.status_code == 200:
        print("Get Requets Successfully\n")
        # .
        # .
        # .
        # .
    else :
        print("GET Request Failed.")
    # Check the status code to see if the request was successful
    # 200 OK means the request was successful

def requests_post_lesson():
    print("--- 3. Rest API Post lesson ---\n")
    # POST requests are used to send data to a server to create or update a resource.
    url = f"https://jsonplaceholder.typicode.com/todos/1"
    # Data we want to send to the server
    new_post_data = {
        "title": "Learning REST APIs",
        "body": "This is a great lesson on requests and JSON in Python.",
        "userId": 1
    }
    print(f"sending POST request to {url}...")
    # The `json` parameter automatically serializes our dictionary into a JSON string
    # and sets the correct HTTP headers (Content-Type: application/json)
    response = requests.post(url, json=new_post_data)
    
    # 201 Created usually means a resource was successfully created on the server
    print(f"status code: {response.status_code}")
    if response.status_code == 201:
        print("PoST request successfully! Resource created. \n")
        # The server usually responds with the created resource and its new ID
        created_post = response.json()
        print("Response From server :")
        print(json.dumps(created_post,indent=4))
    else:
        print("request failed .")

json_lesson()
requests_get_lesson()
requests_post_lesson()



