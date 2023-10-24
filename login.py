# User database (username: password)
users = {}

# Secured page content
secured_page_content = "Welcome to the secured page! You have successfully logged in."

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    
    if username in users:
        print("Username already exists. Please choose another one.")
    else:
        users[username] = password
        print("Registration successful!")

# Function to log in a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in users and users[username] == password:
        print("Login successful!")
        access_secured_page()
    else:
        print("Invalid username or password. Please try again.")

# Function to access the secured page
def access_secured_page():
    print(secured_page_content)

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Please select an option: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")
