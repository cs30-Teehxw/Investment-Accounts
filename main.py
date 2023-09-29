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

    for num in Accounts:
      print("Account " + ": "+ "$" + str(num))

'''
  # Option 2
  elif option == "2":
    # DEPOSIT

 

  # Option 3
  elif option == "3":
    # WITHDRAWAL
      

  # Option 4
  elif option == "4"
    #COUNT UNDER $2000


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
    '''
