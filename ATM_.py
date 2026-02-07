i=input("Enter a pin Num: ")
l=len(str(i))
if l==4:
		print("Login succesful!\n ")
		balance=5000
		while True:
			print("Enter-1: check balance")
			print("Enter-2: Deposit Money ")
			print("Enter-3:Withdraw Money")
			print("Enter-4: Exit\n ")
			n=int(input("Enter choose options:"))
			if n==1:
				print("Your current balance: ",balance)
			elif n==2:
				deposite=int(input("Enter amount to deposite: "))
				balance=balance+deposite
				print("New balance",balance)
			elif n==3:
				withdraw=int(input("Enter withdrwal money: "))
				if withdraw<=balance:
					print("New balance",balance-withdraw)
				else:
					print("Insufficent Funds!")
			else:
				print("Thank u for using ATM")
				break
else:
	print("Incorrect Pin")
