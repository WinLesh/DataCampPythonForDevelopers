#add a query parameter to only get lyrics by
#  a specific artist.
#Create a dictionary variable with one entry: 
# the key artist with a value of Deep Purple.
#Pass this dictionary to the requests.get()
#  method as the params argument.

# Create a dictionary variable with query params
query_params = {'artist':'Deep Purple'}

# Pass the dictionary to the get() function
response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

print(response.text)