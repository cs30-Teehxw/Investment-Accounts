#Investment Accounts

Accounts = [1473, 4356, 1273, 2339, 1234, 99, 3, 2389, 4000, 2400, 1768, 4321, 2355, 3500, 2500, 1122, 2343, 1527, 5000, 2112 ]

# Main Program Loop
loop = True
while loop:
  # Main Menu
  print("\nMAIN MENU ")
  print("1. Print Accounts")
  print("2.  Deposit")
  print("3. Withdrawal")
  print("4. Count Under $2000")
  print("5. Generous Donor")
  print("6. Hacker Attack")
  print("7. Exit")

  # Get Menu Selection from User
  option = input("Enter Selection (1-6): \n")

  # Take Action Based on Menu Selection
  # Option 1

  if option == "1":
    # PRINT ACCOUNTS
    print("PRINT ACCOUNTS")
    for i in range(len(Accounts)):
      print(f"Accounts {i}: ${Accounts[i]}")

  # Option 2
  elif option == "2":
    # DEPOSIT
   print("DEPOSIT")
   accountnum = int(input("Enter Account#: "))
   deposit = int(input("Enter amount to deposit: "))
   sum = Accounts[accountnum] + deposit
   print(f"Account {accountnum} Previous Balance: ${Accounts[accountnum]}")
   print(f"Account {accountnum} New Balance: ${sum}")
 

  # Option 3
  elif option == "3":
    # WITHDRAWAL
    print("WITHDRAWAL")
    accountnum = int(input("Enter Account#: "))
    withdraw = int(input("Enter amount to withdraw: "))
    sum = Accounts[accountnum] - withdraw
    if sum < 0:
      print("Sorry, insufficient funds")
    else:
      print(f"Account {accountnum} Previous Balance: ${Accounts[accountnum]}")
      print(f"Account {accountnum} New Balance: ${sum}")
      

  # Option 4
  elif option == "4":
    #COUNT UNDER $2000
    print("COUNT UNDER $2000")
    count = 0
    for i in range(len(Accounts)):
      if Accounts[i] <= 2000:
        print(f"Account {i}: ${Accounts[i]}")
        totalcount = count + 1

    print(f"Account with less than $2000: {totalcount}")


"""
  #Option 5
  elif option == "5":   
    #GENEROUS DONOR


# Option 6
  elif option == "6":
    #HACKER ATTACK

    
  # Option 7
  elif option == "7":
    print("EXIT")
    loop = False
"""
