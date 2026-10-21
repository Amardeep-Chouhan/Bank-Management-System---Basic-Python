import json
from pathlib import Path
import string
import random

class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")


    def Createaccount(self):
        info={
            "name":input("enter your name: "),
            "age":int(input("enter your age: ")),
            "email":input("enter your email: "),
            "pin":input("enter 4 digit pin number: "),
            "account_number":1234,
            "balance":0,

        }
        if info['age'] < 18 :  
        
            print(f"sorry you cannot create your account {info["age"]} < 18")
        elif len(str(info['pin'])) != 4:
            print(f"plese enter 4 digit pin")
        else:
            print(f"account has been created successfully {info["pin"]} less then 4 digits ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")



print("press 1 for Creating an account")
print("press 2 for Depositing the money in the bank ")
print("press 3 for Withdrawing the money ")
print("press 4 for Details ")
print("press 5 for Updating the details")
print("press 6 for Deleting your account")

check = int(input(" Enter the input to procced : "))

if check==1:
    Bank.Createaccount