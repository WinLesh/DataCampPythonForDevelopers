#Respecting API rate limits
#Let's put what we learned about error handling to the test.
#  In this exercise you'll encounter a rate-limit error, 
# which means you're sending too many requests to the server in a short amount of time.
#  Let's fix it by implementing a workaround to circumvent the rate limit so our script
#  doesn't fail.
# Your music library contains over 3500 music tracks, 
# so let's try to find the longest track by checking the
# Length property of each track.
#But there is an issue, the /tracks API has a maximum page size of 500 items 
# and has a rate-limit of 1 request per second. The script we've written is sending too many requests to the server in a short amount of time. Let's fix it!
#The requests and time packages are already imported, and we've created the following variables for you:

#longestTrackLength = 0
#longestTrackTitle = ""
#headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
#page_number = 1

# Start by running the exercise without making changes to the code, 
# you'll notice that the console outputs a 429 Client Error indicating we are sending 
# too many requests to the server in a short amount of time.
#Fix the script by adding a 3 second pause at the end of the while-loop using
#  the sleep method from the time package.


while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
    
    # Add your fix here
    time.sleep(3)

print('The longest track in my music library is: ' + longestTrackTitle)