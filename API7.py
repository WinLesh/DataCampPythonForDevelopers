# Create a dictionary with the playlist info
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data=playlist_data)
print(response.text)