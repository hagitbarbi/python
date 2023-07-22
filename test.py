import requests

def login_function(login_url, username, password):
    # Create a dictionary with the user's credentials
    payload = {
        'username': username,
        'password': password
    }

    # Send a POST request to the login URL with the user's credentials
    response = requests.post(login_url, data=payload)

    # Check if the login was successful
    if response.status_code == 200:
        print("התחברת בהצלחה!")
        # You can add additional code here to perform actions after successful login
    else:
        print("התחברות נכשלה. נסה שוב.")

# Example usage
login_url = "https://example.com/login"  # The login form URL
username = "my_username"  # Your username
password = "my_password"  # Your password
login_function(login_url, username, password)
