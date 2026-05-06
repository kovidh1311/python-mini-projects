
import json
class person:   

    def __init__(self,name,age,password,money):
        if age<18:
            raise ValueError("you are not allowed to make a account")
        else:
            self.money = money
            self.name = name
            self.age = age
            self.password = password

    def clrify(self,amount):
        if amount <= 0:
            print("what are u trying to do?")
            return False
        else:
            return True

    def deposit(self,deposit):
        if self.clrify(deposit):
            self.money = self.money + deposit

    def withdraw(self,withdraaw):
        if self.clrify(withdraaw):
            if self.money<withdraaw:
                print(f"you have only been give {self.money} as that is how much is in your account")
                self.money = 0
            else:      
                self.money -= withdraaw

    def cheeck(self):
        print(f"you have {self.money} in your account")

people = {}
ccc = None

with open("accounts.json", "r") as file:
    data = json.load(file)
    for i in data:
        people[i]=person(i,data[i]["age"],data[i]["password"],data[i]["money"])


def createe():
    global ccc
    x = input("enter name")
    while x  in people.keys():
        print("name already exsists")
        x = input("enter name")   
    a = input("enter password")
    y = int(input("enter age"))
    people[x] = person(x,y,a,0)
    ccc = people[x]


def login():
    global ccc
    aa = input("enter your name")
    if aa in people:
        u = 0
        while u != 3:
            aaa = input("enter your password")
            if aaa == people[aa].password:
                print(f"you have logged in into {aa} account")
                ccc = people[aa]
                break
            else:
                print("password is wrong")
                u = u+1


while True:

    c = input("what would u like to do?(create,deposit,withdraw,check,log in,log out,imdone)")
    if c == "log in":
        if ccc:
            print("log out first")
        else:
            login()
    elif c == "create":
        if ccc:
            print("log out first")
        else:
            createe()
    elif c == "deposit":
        d = int(input("enter deposit amount"))
        ccc.deposit(d)
    elif c == "withdraw":
        d = int(input("enter withdraw amount"))
        ccc.withdraw(d)
    elif c == "check":
        ccc.cheeck()
    elif c == "log out":
        if ccc == None:
            print("no account to log out from")
        else:
            print(f"logged out of {ccc.name} account")
            ccc = None
    elif c == "imdone":
        break

data = {}

for name, person in people.items():
    data[name] = {
        "age": person.age,
        "password": person.password,
        "money": person.money
    }

with open("accounts.json", "w") as f:
    json.dump(data, f)


