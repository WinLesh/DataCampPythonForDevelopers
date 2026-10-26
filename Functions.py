# You are a junior developer working in a small start-up. 
# Your managers have asked you to develop a new account registration system for a mobile app.
#  The system must validate user input on the sign-up form before creating an account. 
#The previous junior developer wrote some helper functions that validate the name, email, and password. Use these functions to register users, store their data, and implement some error handling! These have been imported into the workspace for you. They will be a great help to you when registering the user, but first you have to understand what the function does! Inspect the docstrings of each of the helper functions: `validate_name`, `validate_email` and `validate_password`.

# Re-run this cell and examine the docstring of each function
#from python_functions import validate_name, validate_email, validate_password, top_level_domains




def validate_name(name):
    return isinstance(name, str) and len(name) >= 3

def validate_email(email):
    # Simple email validation for demonstration
    return isinstance(email, str) and "@" in email and "." in email

def validate_password(password):
    if not isinstance(password, str) or len(password) < 9:
        return False
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_digit

def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("Name must be a string with at least 3 characters.")

    if not validate_email(email):
        raise ValueError("Email format or domain is invalid.")

    if not validate_password(password):
        raise ValueError(
            "Password must have at least 9 characters, an uppercase letter, and a digit."
        )

    return True

def register_user(name, email, password):
    try:
        validate_user(name, email, password)
    except ValueError:
        return False

    return {
        "name": name,
        "email": email,
        "password": password
    }
