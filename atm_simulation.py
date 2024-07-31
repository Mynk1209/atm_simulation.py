# name = input("plz enter your name :")
# print("hello" , name )
# message ='''
# HOW may i help you sir

# plez selest any of the option ,
# type1 >>> check balnce
# type2 >>> deposit
# type3 >>>m withdrow
# '''
# print(message)
# task= int(input("plz select any options :"))
# avilable_amount= 5000
# if task >=1 and task<=3:
#     print("welcome sir")
    
#     if task==1 :
#         #check balance program
#        print("your avilable amount is :", avilable_amount, "INR")
#     elif task ==2 :
#         #deposit amount
#          deposit_amount = int(input("plz enter deposit amount  : "))
#          if deposit_amount > 0:
#            # avilable_amount =avilable_amount+ deposit_amount
#            avilable_amount+= deposit_amount
#            print("you have sucessfully deposit your amount : ",deposit_amount)
#            print("your avilabe amount is :",avilable_amount,"INR")
# else: 
#     print("plz enter valid amount!")


# elif:
#         # withdrawl amount
#         withdrawl_amount = int(input("plz enter withdrawl amount : "))
#         if withdrawl_amount <= avilable_amount:
#              avilable_amount -= withdrawl_amount
#              print('You have succussfully withdrawl your amount : ',withdrawl_amount)
#              print('Your available amount is : ',avilable_amount,' INR') 
#         else:
#             print("you dont have sufficient amount in your account!")
#             print('Your available amount is : ',avilable_amount,' INR') 
# else:
#     print("plz choose valid option in between 1 to 3 !")

    



#       name = input("plz enter your name : ")
# print("hello", name)
# message =''' HOW may i help you sir plez selest any of the option ,
# type1 >>> check balance
# type2 >>> deposit
# type3 >>> withdraw '''
# print(message)
# task = int(input("plz select any options : "))
# available_amount = 5000
# if task >= 1 and task
# print("welcome sir")
# if task == 1:
# # check balance program
# print("your available amount is :", available_amount, "INR")
# elif task == 2:
# # deposit amount
# deposit_amount = int(input("plz enter deposit amount : "))
# if deposit_amount > 0:
# available_amount += deposit_amount
# print("you have successfully deposited your amount : ", deposit_amount)
# print("your available amount is :", available_amount, "INR")
# else:
# print("plz enter valid amount!")
# elif task == 3:
# # withdraw amount
# withdraw_amount = int(input("plz enter withdraw amount : "))
# if withdraw_amount
# available_amount -= withdraw_amount
# print('You have successfully withdrawn your amount : ', withdraw_amount)
# print('Your available amount is : ', available_amount, ' INR')
# else:
# print("you don't have sufficient amount in your account!")
# print('Your available amount is : ', available_amount, ' INR')
# else:
# print("plz choose valid option in between 1 to 3 !")


# name = input("plz enter your name :")
# print("hello" , name )
# message ='''
# HOW may i help you sir

# plez selest any of the option ,
# type1 >>> check balnce
# type2 >>> deposit
# type3 >>>m withdrow
# '''
# print(message)
# task= int(input("plz select any options :"))
# avilable_amount= 5000
# if task >=1 and task<=3:
#     print("welcome sir")
    
#     if task==1 :
#         #check balance program
#        print("your avilable amount is :", avilable_amount, "INR")
#     elif task ==2 :
#         #deposit amount
#          deposit_amount = int(input("plz enter deposit amount  : "))
#          if deposit_amount > 0:
#            # avilable_amount =avilable_amount+ deposit_amount
#            avilable_amount+= deposit_amount
#            print("you have sucessfully deposit your amount : ",deposit_amount)
#            print("your avilabe amount is :",avilable_amount,"INR")
#          else: 
#            print("plz enter valid amount!")
#     elif task ==3:
#         # withdrawl amount
#         withdrawl_amount = int(input("plz enter withdrawl amount : "))
#         if withdrawl_amount <= avilable_amount:
#              avilable_amount -= withdrawl_amount
#              print('You have succussfully withdrawl your amount : ',withdrawl_amount)
#              print('Your available amount is : ',avilable_amount,' INR') 
#         else:
#             print("you dont have sufficient amount in your account!")
#             print('Your available amount is : ',avilable_amount,' INR') 
# else:
#     print("plz choose valid option in between 1 to 3 !")


name = input("plz enter your name : ")
print("hello", name)
message =''' HOW may i help you sir plez selest any of the option ,
type1 >>> check balance
type2 >>> deposit
type3 >>> withdraw '''
print(message)
task = int(input("plz select any options : "))
available_amount = 5000
if task >= 1 and task <= 3:
    print("welcome sir")
    if task == 1:
        # check balance program
        print("your available amount is :", available_amount, "INR")
    elif task == 2:
        # deposit amount
        deposit_amount = int(input("plz enter deposit amount : "))
        if deposit_amount > 0:
            available_amount += deposit_amount
            print("you have successfully deposited your amount : ", deposit_amount)
            print("your available amount is :", available_amount, "INR")
        else:
            print("plz enter valid amount!")
    elif task == 3:
        # withdraw amount
        withdraw_amount = int(input("plz enter withdraw amount : "))
        if withdraw_amount <= available_amount:
            available_amount -= withdraw_amount
            print('You have successfully withdrawn your amount : ', withdraw_amount)
            print('Your available amount is : ', available_amount, ' INR')
        else:
            print("you don't have sufficient amount in your account!")
            print('Your available amount is : ', available_amount, ' INR')
else:
    print("plz choose valid option in between 1 to 3 !")

