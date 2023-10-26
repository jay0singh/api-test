import requests
import json

# Replace with your name
your_name = "Jay"

# Base URL for the Nationalize.io API
base_url = f"https://api.nationalize.io?name={your_name}"

# Helper function to print response details
def print_response(response):
    print(f"Response Code: {response.status_code}")
    print("Response Body:")
    try:
        response_json = response.json()
        print(json.dumps(response_json, indent=4))
    except ValueError:
        print(response.text)

# GET request
print("GET Request:")
get_response = requests.get(base_url)
print_response(get_response)

# PUT request
print("PUT Request:")
put_data = {
    "name": your_name,
}
put_response = requests.put(base_url, json=put_data)
print_response(put_response)

# POST request with a hardcoded JSON body
print("POST Request with Hardcoded JSON Body:")
post_data = {
    "name": your_name,
}
post_response_with_json = requests.post(base_url, json=post_data)
print_response(post_response_with_json)

# POST request with a JSON file
print("POST Request with JSON File:")
with open("test.json", "r") as json_file:
    json_data = json.load(json_file)
post_response_with_json_file = requests.post(base_url, json=json_data)
print_response(post_response_with_json_file)

# PATCH request
print("PATCH Request:")
patch_data = {
    "name": "Jay",
}
patch_response = requests.patch(base_url, json=patch_data)
print_response(patch_response)

# DELETE request
print("DELETE Request:")
delete_response = requests.delete(base_url)
print_response(delete_response)
