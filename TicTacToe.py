from random import randint

welcome_board = ['#','T','O','E','T','A','C','T','I','C']
theboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = 'WRONG'

def clear_screen():
	
	print("\n"*100)

def display_board(board):
    
    print('   |   | ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
 

def player_input():
	marker = ''
	
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player 1: Do you want to be X or O? ').upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')
	

def choose_first():
	if randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

def place_marker(board, marker, position):
	
	theboard[position] = marker
	return theboard

def win_check(board, mark):
	
	return((board[7] == mark and board[8] == mark and board[9] == mark) or ## Win along the top
	(board[4] == mark and board[5] == mark and board[6] == mark) or ## Win along the middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or ## Win along the bottom
	(board[1] == mark and board[4] == mark and board[7] == mark) or ## Win up the left
	(board[2] == mark and board[5] == mark and board[8] == mark) or ## Win up the middle
	(board[3] == mark and board[6] == mark and board[9] == mark) or ## Win up the right
	(board[1] == mark and board[5] == mark and board[9] == mark) or ## Win Diag
	(board[3] == mark and board[5] == mark and board[7] == mark)) ## Win Diag

def space_check(board, position):
	
	return board[position] == ' '

def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
			
	return True
	
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("\nChoose your next position: (1-9) "))
        
    return position

def replay():
	replay = input("Would you like to play again? (Y/N): ")
		
	if replay.lower()[0] == 'y':
		clear_screen()
		return True
	else:
		return False
		


print("Welcome to Tic Tac Toe!\n")
display_board(welcome_board)
print("\n")

while True:
	theboard = [' '] * 10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print("\nRandomly picking who goes first...")
	print(turn + ". You will go first!")
	
	play_game = input("\nAre you ready to start? Enter Yes or No: ")
	
	if play_game.lower()[0] == 'y':
		game_on = True
	else:
		game_on = False
	
	while game_on:
		if turn == 'Player 1':
			## Player 1 Turn.
			
			print("\n" * 10)
			display_board(theboard)
			position = player_choice(theboard)
			place_marker(theboard, player1_marker, position)
			
			if win_check(theboard, player1_marker):
				display_board(theboard)
				print("Congratulations! Player 1 won the game!")
				game_on = False
			else:
				if full_board_check(theboard):
					display_board(theboard)
					print("The game is a draw!")
					break
				else:
					turn = 'Player 2'

		else:
			## Player 2 Turn.
			
			print("\n" * 10)
			display_board(theboard)
			position = player_choice(theboard)
			place_marker(theboard, player2_marker, position)
			
			if win_check(theboard, player2_marker):
				display_board(theboard)
				print("Congratulations! Player 2 won the game!")
				game_on = False
			else:
				if full_board_check(theboard):
					display_board(theboard)
					print("The game is a draw!")
					break
				else:
					turn = 'Player 1'

	if not replay():
		break
