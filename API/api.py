import requests
import json

# Define the base URL
base_url = "https://api.nationalize.io"

# Replace 'YOUR_NAME' with your actual name or the name you want to test
name = "Jay"

# GET Request
get_response = requests.get(f"{base_url}?name={name}")
print("GET Response Status Code:", get_response.status_code)
print("GET Response Body:", get_response.text)

# Specify the path to your JSON file here
json_file_path = "test.json"

# POST Request with a JSON file
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

post_response = requests.post(base_url, json=json_data)
print("POST Response Status Code:", post_response.status_code)
print("POST Response Body:", post_response.text)

# PUT Request with JSON data
put_response = requests.put(base_url, json=json_data)
print("PUT Response Status Code:", put_response.status_code)
print("PUT Response Body:", put_response.text)

# DELETE Request
delete_response = requests.delete(f"{base_url}?name={name}")
print("DELETE Response Status Code:", delete_response.status_code)
print("DELETE Response Body:", delete_response.text)

# PATCH Request with a JSON body
patch_data = {
    "new_name": "Dhruv",
    "new_age": 21,
    "new_country": "India"
}
patch_response = requests.patch(base_url, json=patch_data)
print("PATCH Response Status Code:", patch_response.status_code)
print("PATCH Response Body:", patch_response.text)
