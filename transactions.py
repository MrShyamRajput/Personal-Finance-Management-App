from auth import users_collection,db
from datetime import datetime
from bson.objectid import ObjectId
import json
import os


def add_transaction(username):
    users_collection=db[f"{username}_transactions"]
    transaction = {
        "username": username,
        "amount": float(input(" Enter the amount: ")),
        "category":input(" Category: "),
        "type": input(" Transaction_type ( income or expense): "),    
        "date": datetime.today(),
    }
    try:
        users_collection.insert_one(transaction)
        print("Transaction added successfully!")
    except:
        print("Error... Try again")


def view_transactions(username):
    collection=db[f"{username}_transactions"]
    data=collection.find()
    if data:
        print("""+-----+---------------------------+--------+------------+---------------------+
|  No  |     Transaction ID       |   Amount   | Category   | Type of Transaction |
+-----+---------------------------+--------+------------+---------------------+""")
        
        i=1
        for transaction in data:
            print(f"  {i}  -->,{transaction["_id"]},--->{transaction["amount"]} Rs,--->, {transaction["category"]},--->, {transaction["type"]}")
            print("+------------------------------------------------------------------------------")
            i+=1
            

def update_transaction(username):
    users_collection=db[f"{username}_transactions"]
    try:
        transaction_id=ObjectId(input("Enter the transaction id: "))
        transaction = {
        "amount": float(input(" Enter the amount: ")),
        "category":input(" Category: "),
        "type": input(" Transaction_type ( income or expense): "),    
        "date": datetime.today(),
        }
        if users_collection.update_one({"_id":transaction_id}, {"$set": transaction}):
            print("Transaction Updated Successfully.")
    except:
        print("Error!... Try again")



def set_budget(username):
    budget=float(input("Enter your new budget:\t"))
    try:
        users_collection.update_one({"username":username}, {"$set": {"budget": budget}})
        print("New Budget Updated")
    except:
        print("Error occured!..  Try again.")
    

def check_budget(username):
    budget=users_collection.find_one({ "username":username}, { "budget": 1 })
    print(f"Your budget is {budget["budget"]}")
    

def generate_report_monthly(username):
    month_no=int(input("Enter the month number: "))
    if month_no<=0 or month_no>12:
        print("Enter a valid month no")
        return
    months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
    users_collection = db[f"{username}_transactions"]
    data=users_collection.find({"username":username})
    total_income=0
    total_expenses=0
    trans=[]
    if data:
        for i in data:
            date_obj = i['date']
            month = date_obj.month  # Extract month
            if month==month_no:
                trans.append(i)
                if  "inc" in i["type"]:
                    total_income+=i["amount"]
                elif "exp" in i["type"]:
                    total_expenses+=i["amount"]
    i=1
    print(f"Transaction in the month: {months[month_no-1]}")
    print("""+-----+---------------------------+--------+------------+---------------------+
|  No  |     Transaction ID       |   Amount   | Category   | Type of Transaction |
+-----+---------------------------+--------+------------+---------------------+""")
    for transaction in trans:
        print(f"  {i}  -->,{transaction["_id"]},--->{transaction["amount"]} Rs,--->, {transaction["category"]},--->, {transaction["type"]}")
        print("+------------------------------------------------------------------------------")
        i+=1
    print()
    print("**************************")
    print(f"Reports of the month: {months[month_no-1]}")
    print("**************************")
    print(f"Total Earning: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Saving: {total_income-total_expenses}")
    

def generate_report_yearly(username):
    yr=int(input("Enter the year: "))
    if yr<=0 or yr>12:
        print("Enter a valid month no")
    
    users_collection = db[f"{username}_transactions"]
    data=users_collection.find({"username":username})
    total_income=0
    total_expenses=0
    trans=[]
    if data:
        for i in data:
            date_obj = i['date']
            year = date_obj.year  # Extract month
            if year==yr:
                trans.append(i)
                if  "inc" in i["type"]:
                    total_income+=i["amount"]
                elif "exp" in i["type"]:
                    total_expenses+=i["amount"]

    i=1
    print(f"Transaction of the year: {yr}")
    print("""+-----+---------------------------+--------+------------+---------------------+
|  No  |     Transaction ID       |   Amount   | Category   | Type of Transaction |
+-----+---------------------------+--------+------------+---------------------+""")
    for transaction in trans:
        print(f"  {i}  -->,{transaction["_id"]},--->{transaction["amount"]} Rs,--->, {transaction["category"]},--->, {transaction["type"]}")
        print("+------------------------------------------------------------------------------")
        i+=1
    print()
    print("**************************")
    print(f"Reports of the year: {yr}")
    print("**************************")
    print(f"Reports of the year:{year}")
    print(f"Total Earning: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Total Saving: {total_income-total_expenses}")



def backup_data(username):
    users_collection = db[f"{username}_transactions"]
    try:
        transactions = list(users_collection.find())

        # Convert ObjectId and datetime to strings for JSON
        for txn in transactions:
            txn["_id"] = str(txn["_id"])  # Convert ObjectId to string
            if "date" in txn and isinstance(txn["date"], datetime):
                txn["date"] = txn["date"].strftime("%Y-%m-%d %H:%M:%S")

        if not os.path.exists("Backup"):
            os.makedirs("Backup")
        file_path = os.path.join("Backup", f"{username}_transactions.json")
        
        with open(file_path, "w") as file:
            json.dump(transactions, file, indent=4)
        
        print(f"✅ Transactions saved to {file_path}")
    except Exception as e:
        print(f"❌ Failed to save transactions: {e}")

def restore_all_transactions(username):
    backup_folder = "backup"
    file_path = os.path.join("Backup", f"{username}_transactions.json")
    
    if not os.path.exists(file_path):
        print("Backup file not found!")
        return
    
    try:
        with open(file_path, "r") as file:
            transactions = json.load(file)
        users_collection = db[f"{username}_transactions"]
        
        if transactions:
            users_collection.insert_many(transactions)
            print(f" Successfully restored {len(transactions)} transactions!")
        else:
            print(" No transactions found to restore.")
            
    except Exception as e:
        print(f"❌ Error during restore: {e}")