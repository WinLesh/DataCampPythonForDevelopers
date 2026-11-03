# Make a request to the movies endpoint of the API
response = requests.get('http://localhost:3000/movies')

if (response.status_code == 200):
  print('The server responded succesfully!')
  
# Check the response status code
elif (response.status_code == 404):
  print('Oops, that API could not be found!')