import os

money=100
cost=0
milk=0
sugar=0
coffee=0
water=0
employees={}
customers=[]

def latte_ingredients():
    global milk,sugar,coffee,water
    milk-=100
    sugar-=50
    coffee-=300
    water-=200

def espresso_ingredients():
    global milk,sugar,coffee,water
    milk-=200
    sugar-=40
    coffee-=200
    water-=200

def cappaucino_ingredients():
    global milk,sugar,coffee,water
    milk-=300
    sugar-=60
    coffee-=100
    water-=100        


def display():
    global money, cost
    r5 = int(input("How many 5 rs coins :"))
    r10 = int(input("How many 10 rs coins :"))
    r20 = int(input("How many 20 rs coins :"))
    sume = r5*5 + r10*10 + r20*20
    if sume < cost:
        print("Sorry, not enough money. Money refunded.")
        return False   
    change = sume - cost
    money += cost      
    print(f"Here is your change {change}")   
     
def latte():
    latte_ingredients()
    if milk > 0 and water > 0 and coffee > 0 and sugar > 0:
        global cost,money
        cost=150
        display()
        print("Here is your Latte")
        user()
    else :
        print("Contact , support team")
        print("Shortage of ingredients")
        print(f"There is {milk} in coffee machine")
        print(f"There is {water} in coffee machine")
        print(f"There is {sugar} in coffee machine")
        print(f"There is {coffee} in coffee machine")
        
def espresso():
    espresso_ingredients()
    if milk > 0 and water > 0 and coffee > 0 and sugar > 0:
        global cost,money
        cost=200
        display()
        print("Here is your Espresso")
        user()
    else :
        print("Contact , support team")    
        print("Shortage of ingredients")
        print(f"There is {milk} in coffee machine")
        print(f"There is {water} in coffee machine")
        print(f"There is {sugar} in coffee machine")
        print(f"There is {coffee} in coffee machine")

def cappaucino():
    cappaucino_ingredients()
    if milk > 0 and water > 0 and coffee > 0 and sugar > 0:
        global cost,money
        cost=300
        display()  
        print("Here is your Cappaucino") 
        user()
        
    else :
        print("Contact , support team")   
        print("Shortage of ingredients")
        print(f"There is {milk} in coffee machine")
        print(f"There is {water} in coffee machine")
        print(f"There is {sugar} in coffee machine")
        print(f"There is {coffee} in coffee machine")
    
def report():
    global milk,sugar,coffee,water,money
    print(f"There is {milk} in coffee machine")
    print(f"There is {water} in coffee machine")
    print(f"There is {sugar} in coffee machine")
    print(f"There is {coffee} in coffee machine")
    print(f"The revenue from machine is {money}")
    print("Do you want to add ingredints into machine ")
    addin=int(input(("Press '1' to add or '2' to exit ")))
    
    if addin==1: 
        x=int(input("Enter qunatity to add into milk :"))
        y=int(input("Enter qunatity to add into water :"))
        a=int(input("Enter qunatity to add into sugar :"))
        b=int(input("Enter qunatity to add into coffee :"))
        milk+=x
        water+=y
        sugar+=a
        coffee+=b
        
    elif addin==2:
        print("Machine is ready to serve")               
    user()
    
print("Welcome to Coffe - Machine ")

def user():
    identity=int(input("Enter 1 for customer entry or 2 for owner entry :"))
    if identity==1:
        global customers
        print("Here is your menu we are serving espresso/cappaucino/latte ")
        name=str(input("Enter your name :"))
        customers.append(name)
        choice=str(input("Enter your choice :"))
        if choice=='espresso':
            espresso()
        elif choice=='cappaucino':
            cappaucino()
        elif choice=='latte':
            latte() 
            
    elif identity==2:
        global employees
        print("If you are new enter '1' for registration or '2' for login ")
        new=int(input("Enter your response :"))
        if new==1:
            print("You need to enter same name for login to access the machine ")
            employee=str(input("Enter your name :"))
            print("Remember your password ")
            password=str(input("Enter your password :"))
            rpassword=str(input("Enter password again to check :"))
            if password==rpassword:
                print("You have successfully registered")
                employees[employee]=password
                os.system("cls")
                user()
                
            else:
                print("The entered password did not match ") 
                
                   
        elif new==2:        
            employee1=str(input("Enter your name :"))
            password1=str(input("Enter your password:"))
            if employee1 in employees:
                pass1=employees[employee1]
                if pass1==password1:
                    report()
                        
           

user()            



