
# List of accepted top-level domains for email validation.
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]


def validate_name(name):
    """
    Validates a user's name.

    Args:
        name: The name entered by the user.

    Returns:
        bool: True if the name is a string and contains
              more than two characters, otherwise False.
    """

    # Check that the name is a string and its length
    # is greater than two characters.
    if isinstance(name, str) and len(name) > 2:
        return True

    # Return False if either condition is not satisfied.
    return False


def validate_email(email):
    """
    Validates a user's email address.

    Args:
        email: The email address entered by the user.

    Returns:
        bool: True if the email is a string, contains '@',
              and ends with an accepted top-level domain.
              Otherwise, False.
    """

    # Check whether the email is a string.
    # This prevents errors when other data types are entered.
    if not isinstance(email, str):
        return False

    # Check whether the email contains the '@' symbol.
    if "@" not in email:
        return False

    # Loop through the list of accepted top-level domains.
    for domain in top_level_domains:

        # Check whether the email ends with the current domain.
        if email.endswith(domain):
            return True

    # Return False if no accepted domain is found.
    return False


# Test the name validation function.
print(validate_name("Lesego"))  # True
print(validate_name("LW"))      # False
print(validate_name(12345))     # False

# Test the email validation function.
print(validate_email("lesego@gmail.com"))  # True
print(validate_email("lesego@gmail"))      # False
print(validate_email("lesegogmail.com"))   # False
