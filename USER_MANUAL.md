Personal Finance Management CLI project, follow this structure:

📘 User Manual for Personal Finance Management Application
1. Introduction
The Personal Finance Management Application is a CLI-based tool designed to help users manage their finances efficiently. It allows users to track transactions, set budgets, monitor expenses, and generate financial reports.

🛠️ 2. System Requirements
Operating System: Windows/Linux/MacOS
Python Version: 3.9 or higher
MongoDB: Installed and running locally or remotely

Required Libraries:
pymongo
datetime
os
json

⚙️ 3. Installation Instructions

Step 2: Create a Virtual Environment (Optional but Recommended)
python -m venv env
source env/bin/activate    # For Linux/Mac
env\Scripts\activate       # For Windows

4. Setup Instructions
Step 1: Configure MongoDB
Ensure MongoDB is running.

Create a database named finance_db.

Update the connection string in your code if needed.

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["finance_db"]

5. Usage Instructions
Run the Application
python main.py

Main Menu Options:

Add Transaction:
Enter income or expense details.
View Transactions:
List all stored transactions
Update Transaction:
Modify existing records.
Set Budget:
Define a monthly budget.
Check Budget Status:
Verify if expenses exceed the budget.
Generate Monthly Report:
View monthly financial summary.
Generate Yearly Report:
Analyze yearly income and expenses.
Backup Data:
    Export transaction data to JSON.
Logout:


🔍 6. Backup and Restore Instructions
Backup Data:


Use the Restore Data option to load previous transactions.

🛡️ 7. Error Handling
Database Connection Failure:

Check MongoDB service status.

Invalid Input:

The application validates numeric inputs for amount and date formats.

File Backup Error:

Ensure the backup folder has the correct path.

🏁 8. Conclusion
This user manual provides step-by-step guidance on installation, usage, and handling errors. For any additional support or queries, contact the developer.