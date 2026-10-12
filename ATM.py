# ATM

# Write a program that simulates an ATM withdrawal.

# Ask the user to enter their PIN.
# Allow a maximum of 3 PIN attempts.

# The program should accept the withdrawal amount.
# A withdrawal should only be allowed if:
# - The withdrawal amount is greater than 0.
# - The withdrawal amount does not exceed the account balance.
# - At least ₹500 must remain in the account after the withdrawal.

# The program should display whether the withdrawal was successful
# and the remaining balance.



accountBalance = 15000
pin = "1234"  # Changed to string to match the input() type
correctPin = False

# range(3) allows exactly 3 attempts (0, 1, 2)
for i in range(3):
    userPin = input("Enter PIN: ")

    if userPin == pin:
        correctPin = True
        break
    else:
        # Only print 'try again' if it's not their last attempt
        if i < 2:
            print("Incorrect PIN, try again")

if correctPin:
    amount = int(input("Enter The Withdrawal Amount: "))

    # Consolidating the withdrawal rules into a clean if/elif chain
    if amount <= 0:
        print("Please enter a value greater than 0")
        
    elif amount > accountBalance:
        print("Amount is greater than Account Balance")
        
    elif (accountBalance - amount) < 500:
        print("Account Balance can't be less than 500")
        
    else:
        # Subtract the amount and print success
        accountBalance = accountBalance - amount
        print(f"Amount Withdrawn: {amount}")
        print(f"Balance: {accountBalance}")

else:
    print("3 Attempts Failed")