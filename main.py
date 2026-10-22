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
            print(f"plese enter 4 digit pin")
        else:
            print(f"account has been created successfully {info['pin']} less then 4 digits ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            
            Bank.data.append(info)

            Bank.__update()


    def depositmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin as well "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Please Input Correct credentials.")

        else:
            amount =int(input("plese enter the amount: "))
            if amount<=0:
                print(f"amount money can't be zero or negative{amount}")
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print(f"Successfully deposited {amount}. New balance is {userdata[0]['balance']}.")


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
    
 

