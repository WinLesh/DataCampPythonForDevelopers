# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')