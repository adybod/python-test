initbalance = int(input("how much do you have on your account?: "))

print("Select option: Account balance (1), Withdraw (2), Deposit (3)")
choice = int(input())

if choice == 1:
    print(initbalance)
elif choice == 2:
    withdraw = int(input("withdraw: "))
    initbalance = initbalance - withdraw
    print("new balance:", initbalance)
elif choice == 3:
    deposit = int(input("deposit: "))
    initbalance = initbalance + deposit
    print("new balance:", initbalance)






# elif attempts==0:
#     print("account terminated. please contact a member from the bank")
#     exit
# else:
#     attempts - 1
#     print("wrong pin", "attempts remaining: "+attempts)
