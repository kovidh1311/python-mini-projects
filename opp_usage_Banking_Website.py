

class person:   

    def __init__(self,name,age,password):
        if age<18:
            raise ValueError("you are not allowed to make a account")
        else:
            self.money = 0
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
while True:
    c = input("what would u like to do?(create,deposit,withdraw,check,log in)")
    if c == "log in":
        aa = input("enter your name")
        for i in people:
            if aa == i:
                aaa = input("enter your password")
                if aaa == people[i].password:
                    print(f"you have logged in into {aa} account")
                    ccc = people[i]
    elif c == "create":
        x = input("enter name")
        a = input("enter password")
        y = int(input("enter age"))
        people[x] = person(x,y,a)
        ccc = people[x]
    elif c == "deposit":
        d = int(input("enter deposit amount"))
        ccc.deposit(d)
    elif c == "withdraw":
        d = int(input("enter withdraw amount"))
        ccc.withdraw(d)
    elif c == "check":
        ccc.cheeck()



