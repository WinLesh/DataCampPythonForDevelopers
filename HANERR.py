#When the requests library is unable to connect to an 
# API server, it will raise an exception. 
# This exception allows you to detect if the API is
#  available and act accordingly. But even when the 
# request is successfully sent, we can still encounter
#  errors. If we send an invalid request, a 4xx Client
#  Error is returned from the API, if the server encounters an error, 
# a 5xx Server Error is returned.
#The requests package provides a set of included exceptions that can be
#  used to handle these errors using try/except statements.
#The requests package has already been imported for your convenience.
#Import the exception class used to detect connection errors from the requests package, then use the imported class to intercept the error raised by the API request.
#Import the exception class used to detect errors returned via the response status code, then enable the setting on the response object which will automatically raise an error when an unsuccessful status code value is received. Finally, intercept the imported exception to print an error.

# Import the correct exception class
from requests.exceptions import ConnectionError

url ="http://wronghost:3000/albums"
try: 
    r = requests.get(url) 
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')



