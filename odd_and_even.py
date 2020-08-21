playing = True
print("Find out if a number is odd or even!")
print("type 'q' to exit.")


while playing:
	number = input("Give me a number: ")
	
	if number == 'q':
		odd_even = False
		break
	
	elif number != 'q':
		number = int(number)
		if number % 2 == 0:
			print("Your number is even.")
		else:
			print("Your number is odd.")
