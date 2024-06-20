import bcrypt
import csv

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def register(username, password):
    hashed_password = hash_password(password)
    with open("users.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, hashed_password.decode('utf-8')])

def login(username, password):
    with open("users.csv", mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            reg_username = row[0]
            reg_password = row[1].encode('utf-8')
            if username == reg_username:
                if bcrypt.checkpw(password.encode('utf-8'), reg_password):
                    return True
                else:
                    return False
    return False

# Example usage:
username = input("Enter a username: ")
password = input("Enter a password: ")
register(username, password)

username = input("Enter your username: ")
password = input("Enter your password: ")
if login(username, password):
    print("Login successful!")
else:
    print("Invalid credentials.")
