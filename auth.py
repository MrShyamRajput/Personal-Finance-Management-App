from pymongo import MongoClient
import bcrypt

client=MongoClient("mongodb://localhost:27017")

db=client["finance_db"]
users_collection=db["login_data"]
if db is not None:
    print("connected successully")

def register_user(username, password):
    # Check if the username already exists
    if users_collection.find_one({"username": username}):
        return "🔴 Oops! That username is taken. 🚧 Try another one! 🎭"
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Store user in the database
    users_collection.insert_one({"username": username, "password": hashed_password})
    return "User registered successfully!  Login now."

def login_user(username, password):
    # Find user in database
    user = users_collection.find_one({"username": username})
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    else:
        return False