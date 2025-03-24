from auth import register_user,login_user
from transactions import *
def main():
    print("\n💰 Personal Finance Management Application 💰")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username=input("Enter Username:\t")
            password=input('Enter Your Password:\t')
            user=register_user(username,password)
            print(user)
        elif choice == "2":
            username=input("Enter Username:\t")
            password=input('Enter Your Password:\t')
            user = login_user(username,password)
            if user is True:
                print("Login Successful ")
                user_menu(username)
            else:
                print("Wrong username or password!.. Try again")
        elif choice == "3":
            print("Exiting application. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")
            main() 

def user_menu(username):
    while True:
        print("\n🔹 Main Menu 🔹")
        
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Set Budget")
        print("5. Check Budget Status")
        print("6. Generate Monthly Report")
        print("7. Generate Yearly Report")
        print("8. Backup Data")
        print("9. Restore Data")
        print("10. Logout")
        choice =input("\tChoose an option: ")

        
        if choice == "1":
            print(add_transaction(username))
        elif choice == "2":
            view_transactions(username)
        elif choice=="3":
            update_transaction(username)
        elif choice == "4":
            set_budget(username)
        elif choice == "5":
            check_budget(username)
        elif choice == "6":
            generate_report_monthly(username)
        elif choice == "7":
            generate_report_yearly(username)
        elif choice == "8":
            backup_data(username)
        elif choice=="9":
            restore_all_transactions(username)
        elif choice=="10":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Please try again.")

        
if __name__=="__main__":
    main()