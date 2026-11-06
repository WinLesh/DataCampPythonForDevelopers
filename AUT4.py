#Receiving JSON with the requests package
#When requesting JSON data from an API, the requests
#library makes it really easy to decode the JSON string you received from the API back into a Python object. In this exercise you'll first need to request data in the JSON format from the API, then decode the response into a Python object to retrieve and print the album Title property.
#Note: The requests package has been imported for you,
#  and because the albums API is protected by authentication,
#  the correct header has already been added.
#Instructions
#1Add the correct header to request JSON from the API.
#2Decode the JSON response into an album object.
#3Print the album Title property

headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    'Accept': 'application/json'
}
response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# Get the JSON data as a Python object from the response object
album = response.json()

# Print the album title
print(album['Title'])