import json
from pathlib import Path
import string
import random

class Bank:
    database = 'data.json'
    data = []
    
    def __init__(self):
        try:
            if Path(Bank.database).exists():
                with open(Bank.database, 'r') as fs:
                    Bank.data = json.load(fs)
            else:
                print("No such file exists. Starting fresh.")
        except Exception as err:
            print(f"An exception occurred as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    # Helper method to avoid code redundancy for login/authentication
    def __authenticate(self):
        accnumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin as well: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("Please Input Correct credentials.")
            return None
        return userdata[0] # Returns the specific client dictionary directly

    def Createaccount(self):
        info = {
            "name": input("Enter your name: "), 
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter 4 digit pin number: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0,
        }
        if info['age'] < 18:  
            print(f"Sorry, you cannot create your account your age {info['age']} < 18")
        elif len(str(info['pin'])) != 4:
            print("Please enter 4 digit pin")
        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")
            
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        client = self.__authenticate()
        if client:
            amount = int(input("Please enter the amount you want to deposit: "))
            if amount <= 0:
                print(f"Amount money can't be zero or negative {amount}")
            else:
                client['balance'] += amount
                Bank.__update()
                print(f"Successfully deposited {amount}. New balance is {client['balance']}.")

    def withdrawmoney(self):
        client = self.__authenticate()
        if client:
            amount = int(input("Please enter the amount you want to withdraw: "))
            if amount <= 0:
                print(f"Amount money can't be zero or negative {amount}")
            elif amount > client['balance']:
                print("Insufficient balance!")
            else:
                client['balance'] -= amount
                Bank.__update()
                print(f"Successfully withdrew {amount}. New balance is {client['balance']}.")

    def details(self):
        client = self.__authenticate()
        if client:
            print("Please check your details carefully:")
            for key, value in client.items():
                print(f"{key} : {value}")

    def updatedetails(self):
        client = self.__authenticate()
        if client:
            print("Important Information - You can only change your Name, E-mail and Pin of your Bank Account.")
            print("Leave blank and press Enter if you don't want to change a field.")
            
            new_name = input(f"Enter new name (current: {client['name']}): ")
            new_email = input(f"Enter new email (current: {client['email']}): ")
            new_pin = input("Enter new 4-digit pin: ")

            # Update directly if input is provided
            if new_name.strip() != "":
                client['name'] = new_name
            if new_email.strip() != "":
                client['email'] = new_email
            if new_pin.strip() != "":
                if len(new_pin) == 4 and new_pin.isdigit():
                    client['pin'] = int(new_pin)
                else:
                    print("Invalid PIN format. PIN was not updated.")

            Bank.__update()
            print("Details updated successfully!")

    def delete(self):
        client =  self.__authenticate()
        check = input("press y if you actually want to delete the account or press n")
        if check == 'n' or check == "N":
                print("bypassed")
        else:
            index = Bank.data.index(client)
            Bank.data.pop(index)
            print("account deleted successfully ")
            Bank.__update()

# Main Execution
user = Bank()
print("Press 1 for Creating an account")
print("Press 2 for Depositing the money in the bank")
print("Press 3 for Withdrawing the money")
print("Press 4 for Details")
print("Press 5 for Updating the details")
print("Press 6 for Deleting your account")

check = int(input("Enter the input to proceed: "))

if check == 1:
    user.Createaccount()
elif check == 2:
    user.depositmoney()
elif check == 3:
    user.withdrawmoney()
elif check == 4:
    user.details()
elif check == 5:
    user.updatedetails()
elif check == 6:
    user.delete()