import json
from pathlib import Path
import string
import random

class Bank:
    database = 'data.json'
    data = []
    
    def __init__(self):
        # Load data safely when an object is created
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
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        
        info={
            "name":input("enter your name: "), 
            "age":int(input("enter your age: ")),
            "email":input("enter your email: "),
            "pin":int(input("enter 4 digit pin number: ")),
            "accountNo.":Bank.__accountgenerate(),
            "balance":0,

        }
        if info['age'] < 18 :  
        
            print(f"sorry you cannot create your account your age {info['age']} < 18")
        elif len(str(info['pin'])) != 4:
            print(f"plese enter 4 digit pin ")
        else:
            print(f"account has been created successfully ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            
            Bank.data.append(info)

            Bank.__update()


    def depositmoney(self):
        accnumber = input("please tell your account number:")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Please Input Correct credentials.")

        else:
            amount =int(input("plese enter the amount you want to deposit: "))
            if amount<=0:
                print(f"amount money can't be zero or negative{amount}")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print(f"Successfully deposited {amount}. New balance is {userdata[0]['balance']}.")

    def withdrawmoney(self):
        accnumber = input("please tell your account number:")
        pin = int(input("please tell your pin as well "))
    
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
    
        if not userdata:
            print("Please Input Correct credentials.")
    
        else:
            amount =int(input("plese enter the amount you want to withdraw: "))
            if amount<=0:
                print(f"amount money can't be zero or negative{amount}")
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print(f"Successfully withdrawal {amount}. New balance is {userdata[0]['balance']}.")

    def details(self):
        accnumber = input("please tell your account number:")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Please Input Correct credentials.")

        else:
            print("plese check your details carefully: ")
            client_dict = userdata[0]
            for key, value in client_dict.items():
                 print(f"{key} : {value}")

    def updatedetails(self):
        accnumber = input("please tell your account number:")
        pin = int(input("please tell your pin as well "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
    
        if not userdata:
            print("Please Input Correct credentials.")


        else:
            print("Important Information - You can only change your Name, E-mail and Pin of your Bank Account.")
            print("Lets Start:- ")
            newdata={
                "name":input("please enter your name or skip by pressing Enter button:"),
                "email":input("plese input you new email or skip by pressing Enter button:"),
                "pin":input("please enter your new pin skip by pressing Enter button:")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")
                

            

        
user = Bank()
print("press 1 for Creating an account")
print("press 2 for Depositing the money in the bank ")
print("press 3 for Withdrawing the money ")
print("press 4 for Details ")
print("press 5 for Updating the details")
print("press 6 for Deleting your account")

check = int(input(" Enter the input to procced : "))

if check==1:
    user.Createaccount()

if check==2:
    user.depositmoney()

if check==3:
    user.withdrawmoney()

if check ==4:
    user.details()

if check ==5:
    user.updatedetails()
    
 

