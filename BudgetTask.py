gap = "=" *20
class Budget:
    """
    This is a Budget class
    """
    Fund = [0,0,0]
    Budgets = ["Food", "Clothing", "Entertainment"]
    

    def __init__(self, category):
        self.category = category - 1


    def what_to_do(self):
        print(gap)
        print("What would you like to do?:")
        print(f"1. Deposit to {self.Budgets[self.category]} Budget")
        print(f"2. Withdraw from {self.Budgets[self.category]} Budget")
        print(f"3. Check balance of {self.Budgets[self.category]} Budget")
        print("4. Transfer to another Budget")

        action = input(": ")

        if (action == "1"):
            self.deposit()

        elif(action == "2"):
            self.withdraw()

        elif(action == "3"):
            self.balance()

        elif(action == "4"):
            self.transfer()
        else:
            print(gap)
            print("Invalid input")
            pass

   
    def deposit(self):
        try:
            print(gap)
            amount = int(input("Enter amount to deposit: \n"))
            self.Fund[self.category] += amount
            print(gap)
            print("Transaction Completed!")

        except ValueError as verr:
            print(gap)
            print(f"Error: {verr}")
            print("Transaction failed")
        


    def withdraw(self):
        try:
            print(gap)
            amount = int(input("Enter amount to withdraw: \n"))
            if(self.Fund[self.category] != 0 or amount < self.Fund[self.category]):
                self.Fund[self.category] -= amount
                print(gap)
                print("Transaction Completed!")

            else:
                print(gap)
                print("Insufficient Funds!")

        except ValueError as verr:
            print(gap)
            print(f"Error: {verr}")
            print("Transaction failed")


    def balance(self):
        print(gap)
        print(f"You have {self.Fund[self.category]} in your {self.Budgets[self.category]} Budget")
        print(gap)
        print("Transaction Completed!")
        pass


    def transfer(self):
        try:
            print(gap)
            print("1. Food")
            print("2. Clothing")
            print("3. Entertainment")
            selection = int(input("Choose budget to transfer to:\n"))
            
            if(selection <= 3):
                selection -= 1
                
                print(gap)
                amount = int(input("Enter amount to transfer: \n"))
                        
                if(selection == self.category):
                    print(gap)
                    print("Same account selected")
                    print("Transaction failed!")

                elif(self.Fund[selection] != 0 or amount < self.Fund[selection]):
                    print(gap)
                    self.Fund[selection] -= amount
                    self.Fund[(self.category - 1)] += amount

                    print(gap)                        
                    print("Transaction Completed!")
                    
                else:
                    print(gap)
                    print("Insufficient Funds!")

            else:
                print(gap)
                print("Invalid input")
                

        except ValueError as verr:
            print(gap)
            print(f"Error: {verr}")
            print("Transaction failed")
        except IndexError as ierr:
            print(gap)
            print(f"Error: {ierr}")
            print("Transaction failed")
        except:
            print(gap)
            print("Error occured!")

    
    


def init():
    print("*******Budget*******")
    print("1. Food")
    print("2. Clothing")
    print("3. Entertainment")

    selection = input("Select from the budgets below:\n")

    if (selection == "1"):
        budget = Budget(1)
        budget.what_to_do()
    elif(selection == "2"):
        budget = Budget(2)
        budget.what_to_do()
    elif(selection == "3"):
        budget = Budget(3)
        budget.what_to_do()
    else:
        print("Invalid input")

    print(gap)  
    retry = input("Would you like to try again? Y/N: ")

    if (retry == "Y" or retry == "Yes" or retry == "y" or retry == "yes"):
        init()
    else:
        print(gap)
        print("Thank you")


init()