## Cup and Ball Game

from random import randint

gameon = True
display = ["[x]","[x]","[x]"]
guess = 0
cupandball = 0
score = 0

print("Welcome to the cup guessing game.")
print("Simply guess which cup the ball is in! [x],[x],[x]")

def reset_cups():

	display = ["[x]","[x]","[x]"]
	
	return display

def ball_location(display, cupandball):
	
	cupandball = randint(0,2)
	display[cupandball] = '[O]'
	
	return display

def player_guess(guess):
	
	guessing = True
	
	while guessing:
		guess = input("\nWhich cup do you think the ball is in? (0,1 or 2): ")
		
		if guess.isdigit() == True and guess in ['0','1','2']:
			print(f"\nYou have guessed {guess}!")
			guessing = False
			break
		else:
			print(f"{guess} is not a valid guess!")
	
	guess = int(guess)
	return guess
	
def check_guess(display, guess, cupandball, score):
	
	guess = guess
	score = int(score)
	cup = cupandball
	
	if display[guess] == '[O]':
		score +=1
		print("That was correct!")
		print(display)
	else:
		print("That was the wrong cup!\n")
		print(display)
	
	return score

def play_again(gameon, score):
	
	again = True
	print(f"\nYour current score is {score}.")
	while again:
		restart = input("\nWould you like to play again? (Y/N): ")
		
		if restart == 'Y':
			gameon = True
			print("Good Luck!")
			again = False
			break
		elif restart == 'N':
			gameon = False
			print("Thanks for playing.")
			again = False
			break
		else:
			print("Please choose Y or N")
			again = True
			
	return gameon


while gameon:
	display = reset_cups()
	display = ball_location(display, cupandball)
	guess = player_guess(guess)
	score = check_guess(display,guess,cupandball,score)
	gameon = play_again(gameon,score)