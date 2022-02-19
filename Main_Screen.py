def Main_Screen(user):
    print("HOME PAGE")
    print(f"{user.name} your Account Balance is: {user.account_balance}")
    user_input = input("To Make A Withdraw PRESS 'A'\nTo Make A Deposit PRESS 'B'").upper()

    if user_input == "A":
        Withdraw_amount = int(input("How Much would You Like to Withdraw?: "))
        if Withdraw_amount > user.account_balance:
            print("the amount you wish to withdraw exceds the amount in your account")
        else:
            user.Withdraw(Withdraw_amount)
    elif user_input == "B":
        Deposit_amount = int(input("How Much would You Like to deposit?: "))
        user.Deposit(Deposit_amount)
        print(f"Your New Account Balance is: {user.account_balance}")