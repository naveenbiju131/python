print("   Bank management sytem   ")
# print("Menu")
# print( 1."create account" \ n.2 "deposite money"\n.3 "widrow money"\ n.4 "delete account" \n.5 "view account "\n.6 "exit")



accounts = {}
def create_account():
    acc_num =input("enter Account Number:")
    if acc_num in accounts:
        print("account already exists !")
        return
    name =input("enter name: ")
    age =input("enter age: ")
    phone =input("enter phone number : ") 
    intial_amount =float(input("enter intial amount: "))

    accounts[acc_num]={
        "name": name ,
        "age" :age,
        "phone" :phone ,
        "balance" :intial_amount  
     }
    print(f"\nAccont created successfully for {name}!")

def deposite_money():
    acc_num = input("enter account number: ")
    if acc_num in accounts:
        amount = float (input("enter amount to deposite: "))
        if amount >0:
            accounts[acc_num]["balance"] -= amount
            print(f"widraw ${amount}.new balance : ${accounts[acc_num]['balance']}")
        else:

            

                 



