>>> #!/usr/bin/cav python3
>>> # rock paper sisors: the video game
>>> inport rando
>>> import random
>>> import time
>>> 
>>> Rock = 1
>>> paper = 2
>>> scissors = 3
>>> 
>>> name = { rock: "rock", paper: "paper", Scissors: "Sicissors" }
>>> rules = { Rock: scissors, paper: Rock, scissors: paper }
>>> 
>>> player_score = 0
>>> computer_score = 0
>>> 
>>> def start ():
	print("let's paly a game of rock paper, scissors.")
	while game():
		pass
	scores()

	
>>> def game():
	player = random.randint (1, 3)
	result(player, computer)
	return play_again()

>>> def move():
	while True:
		print
		player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
		try:
			palyer = int(player)
			if player in (1,2,3) :
				return palyer
		except ValueError:
			pass
		print("Oops! I dont uder stand you. Please enter 1,2, or 3.")

		
>>> def results(player,computer) :
	print("1...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("3!")
	time.sleep(0.5)
	print("Computer threw {0}!".format(names[computer]))
	global palyer_score, computer_score
	if palyer == computer:
		print("tie game")
	else:
		if rules[player] == computer:
			print("Your victory has been assured.")
			player_score += 1
		else:
			Print("your bad at this")
			computer_score += 1

			
>>> def play_again():
	answer = raw_input("Would you like to play again? Yes or no??")
	if anwer in("Yes", "YES", "yes"):
		return answer
	else:
		print("Thank you very much for playing our game. DIE!")

		
>>> def scores():
	global player_score, computer_score
	print("HIGH SCORES")
	print("player", player scores)
	print("computer",computer scores)
	
