'''
Instructions:
	1. Create a deck of 52 cards

	2. Shuffle the deck

	3. Ask the Player for their bet

	4. Make sure that the Player's bet does not exceed their available chips

	5. Deal two cards to the Dealer and two cards to the Player

	6. Show only one of the Dealer's cards, the other remains hidden

	7. Show both of the Player's cards

	8. Ask the Player if they wish to Hit, and take another card

	9. If the Player's hand doesn't Bust (go over 21),
	ask if they'd like to Hit again.

	10. If a Player Stands, play the Dealer's hand.
			The dealer will always Hit until the Dealer's value meets or exceeds 17

	11. Determine the winner and adjust the Player's chips accordingly

	12. Ask the Player if they'd like to play again

	Playing Cards
	A standard deck of playing cards has four suits
	(Hearts, Diamonds, Spades and Clubs) and
	thirteen ranks (2 through 10,
	then the face cards Jack, Queen, King and Ace)
	for a total of 52 cards per deck.

	Jacks, Queens and Kings all have a rank of 10.
	Aces have a rank of either 11 or 1 as needed to reach 21 without busting.

	As a starting point in your program,
	you may want to assign variables to
	store a list of suits, ranks,
	and then use a dictionary to map ranks to values.
'''
import time
from user import Player 
from functions import (calculate_hand, shuffle_deck, calculate_winner)

card_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
card_numbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
card_deck = {}

# 0. Get the player's name
print(
'''
                                     .------.
                                     |A_  _ |
                                     |( \/ ).-----.
                                     | \  /|K /\  |
                                     |  \/ | /  \ |
                                     `-----| \  / |
                                           |  \/ K|
                                           `------'

$$$$$$$\  $$\        $$$$$$\   $$$$$$\  $$\   $$\          $$$$$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |      $$  __$$\ $$  __$$\ $$ | $$  |         \__$$ |$$  __$$\ $$  __$$\ $$ | $$  |
$$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|$$ |$$  /             $$ |$$ /  $$ |$$ /  \__|$$ |$$  / 
$$$$$$$\ |$$ |      $$$$$$$$ |$$ |      $$$$$  /              $$ |$$$$$$$$ |$$ |      $$$$$  /  
$$  __$$\ $$ |      $$  __$$ |$$ |      $$  $$<         $$\   $$ |$$  __$$ |$$ |      $$  $$<   
$$ |  $$ |$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\        $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  
$$$$$$$  |$$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ | \$$\       \$$$$$$  |$$ |  $$ |\$$$$$$  |$$ | \$$\ 
\_______/ \________|\__|  \__| \______/ \__|  \__|       \______/ \__|  \__| \______/ \__|  \__|
                                                                                                
                                                                                                
                                                                                                
''')
print("Hello! Welcome to black jack! Let's start by giving you a player name.")
player_name = input("What is your username for the game? ")

print("Hi {}! To start you off, we're going to be giving you $1000. Good luck!".format(player_name))
player = Player(player_name,1000)
time.sleep(2)

# Instantiate the new player

# 1. Create the deck
for idx, types in enumerate(card_numbers):
	for suits in card_suits:
		# print(suits)
		# print(types)
		if idx+1 > 10:
			card_deck.update({"{} of {}".format(types, suits):10})
		else:
			card_deck.update({"{} of {}".format(types, suits):idx+1})


									### LOOP BEGIN ###
## Any game will always start around here until the player goes bankrupt
## or if the player decides to leave the table ##

while True:
	# Check if player even has enough $ to play a round
	if player.balance == 0:
		print("You went bankrupt! Game over!")
		time.sleep(1)
		play_game = 'N'
	else:
		play_game = input("Ready to play a round? (Y/N) ")

	if play_game.upper() == 'Y':
		game_on = True
		print(player)

	elif play_game.upper() == 'N':
		game_on = False
		print("Thanks for playing! Here are your final stats:")
		print(player)

		print('''


			''')

		print(
'''
                                     .------.
                                     |A_  _ |
                                     |( \/ ).-----.
                                     | \  /|K /\  |
                                     |  \/ | /  \ |
                                     `-----| \  / |
                                           |  \/ K|
                                           `------'

$$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ $$\   $$\       $$\     $$\  $$$$$$\  $$\   $$\ $$\ 
\__$$  __|$$ |  $$ |$$  __$$\ $$$\  $$ |$$ | $$  |      \$$\   $$  |$$  __$$\ $$ |  $$ |$$ |
   $$ |   $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |$$  /        \$$\ $$  / $$ /  $$ |$$ |  $$ |$$ |
   $$ |   $$$$$$$$ |$$$$$$$$ |$$ $$\$$ |$$$$$  /          \$$$$  /  $$ |  $$ |$$ |  $$ |$$ |
   $$ |   $$  __$$ |$$  __$$ |$$ \$$$$ |$$  $$<            \$$  /   $$ |  $$ |$$ |  $$ |\__|
   $$ |   $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |\$$\            $$ |    $$ |  $$ |$$ |  $$ |    
   $$ |   $$ |  $$ |$$ |  $$ |$$ | \$$ |$$ | \$$\           $$ |     $$$$$$  |\$$$$$$  |$$\ 
   \__|   \__|  \__|\__|  \__|\__|  \__|\__|  \__|          \__|     \______/  \______/ \__|
    
''')
		break

	else:
		print("Please enter a valid answer.")
		continue

	while game_on == True:
		# 2. Shuffle the deck
		shuffled_cards = shuffle_deck(card_deck)

		# 3. Place your bet
		# 4. Make sure that bet does not exceed available chips
		while True:

			# Detect if a number was put in
			try:
				bet_value = int(input("How much would you like to bet? $"))
			except ValueError:
				print("Please enter a valid number")
				continue
			else:
				if player.make_bet(bet_value) is not None:
					break
				else:
					bet_value = int(input("How much would you like to bet? $"))
					player.make_bet(bet_value)

		print(
		'''

		''')
		print("Drawing cards...")

		print(
		'''


		''')
		time.sleep(0.75)
		# 5. Deal two cards to the Dealer and two cards to the Player
		cards_in_play = []

		for card in range(0,4):
			cards_in_play.append(shuffled_cards.pop())

		# print(cards_in_play)

		players_hand = [cards_in_play[0], cards_in_play[1]]
		dealers_hand = [cards_in_play[2], cards_in_play[3]]

		# 6. Show only one of the Dealer's cards, the other remains hidden
		print("[D] Dealer's hand is: {}, ???".format(dealers_hand[0]))
		# 7. Show both of the Player's cards
		players_hand_value = calculate_hand(card_deck, players_hand)
		print("[P] Your hand is: {}, {}.".format(players_hand[0], players_hand[1]))
		
		# TEST
		# players_hand_value = calculate_hand(card_deck, ['Ace of Spades', 'Ace of Hearts'])
		# print("Your hand is: {}, {}.".format('Ace of Spades', 'Ace of Hearts'))
		# END TEST

		print("with a value of: {}".format(players_hand_value))

		print(
		'''


		''')
		time.sleep(1)
		#8. Ask the Player if they wish to Hit, and take another card

		#9. If the Player's hand doesn't Bust (go over 21), ask if they'd
		# 	like to Hit again.
		print(
'''
 --------------------

|     Your turn     |

 --------------------
''')
		players_turn_in_session = True

		while players_turn_in_session == True:
			if (len(players_hand) == 2) and players_hand_value == 21:
				print('''
,---.                                                                                     ,---. 
|   |    ,-----.  ,--.     ,---.   ,-----.,--. ,--.     ,--.  ,---.   ,-----.,--. ,--.    |   | 
|  .'    |  |) /_ |  |    /  O  \ '  .--./|  .'   /     |  | /  O  \ '  .--./|  .'   /    |  .' 
|  |     |  .-.  \|  |   |  .-.  ||  |    |  .   ' ,--. |  ||  .-.  ||  |    |  .   '     |  |  
`--'     |  '--' /|  '--.|  | |  |'  '--'\|  |\   \|  '-'  /|  | |  |'  '--'\|  |\   \    `--'  
.--.     `------' `-----'`--' `--' `-----'`--' '--' `-----' `--' `--' `-----'`--' '--'    .--.  
'--'                                                                                      '--' 
					''')
				print("[P] You got a blackjack!")
				break

			status = input("Would you like to Hit? (Y/N):  ")
			if (status.upper() == "Y"):
				print("[P] You: HIT ME!")
				print("Drawing a card...")
				drawn_card = shuffled_cards.pop()
				print(
				'''


				''')

				print("[P] You drew a:", drawn_card)

				players_hand.append(drawn_card)
				print("[P] Your hand is now:")
				print(players_hand)

				print("Calculating your hand:")
				players_hand_value = calculate_hand(card_deck, players_hand)

				if (players_hand_value > 21):
					print("Hand value at: ", players_hand_value)
					print('''
 ______            _______ _________ _______  ______   _  _ 
(  ___ \ |\     /|(  ____ \\__   __/(  ____ \(  __  \ ( )( )
| (   ) )| )   ( || (    \/   ) (   | (    \/| (  \  )| || |
| (__/ / | |   | || (_____    | |   | (__    | |   ) || || |
|  __ (  | |   | |(_____  )   | |   |  __)   | |   | || || |
| (  \ \ | |   | |      ) |   | |   | (      | |   ) |(_)(_)
| )___) )| (___) |/\____) |   | |   | (____/\| (__/  ) _  _ 
|/ \___/ (_______)\_______)   )_(   (_______/(______/ (_)(_)
 
						''')
					break
				else:
					print("[P] Your hand is: {}".format(players_hand_value))

			elif (status.upper() == "N"):
				print("[P] You: Stand.")
				print("Hand value at: ", players_hand_value)
				players_turn_in_session = False

			else:
				print("Error. Please enter a valid command.")
		time.sleep(0.75)
		print("[P] You ended your turn with a hand of {} ({})".format(players_hand, players_hand_value))
		time.sleep(1.25)
		print(
'''
 --------------------

|  Dealer's turn now  |

 --------------------
''')
		# 10. If a Player Stands, play the Dealer's hand.
		# First check if player busted. If player busted, then no game.
		# Dealer wins.

		if players_hand_value > 21:
			dealers_turn_in_session = False
		else:
			dealers_turn_in_session = True
			print("[D] Dealer reveals his/her hand. It's: {}, {}.".format(dealers_hand[0], dealers_hand[1]))

		dealers_hand_value = calculate_hand(card_deck, dealers_hand)
		time.sleep(0.85)
		while dealers_turn_in_session == True:
			
			if (len(dealers_hand) == 2) and dealers_hand_value == 21:
				print('''
,---.                                                                                     ,---. 
|   |    ,-----.  ,--.     ,---.   ,-----.,--. ,--.     ,--.  ,---.   ,-----.,--. ,--.    |   | 
|  .'    |  |) /_ |  |    /  O  \ '  .--./|  .'   /     |  | /  O  \ '  .--./|  .'   /    |  .' 
|  |     |  .-.  \|  |   |  .-.  ||  |    |  .   ' ,--. |  ||  .-.  ||  |    |  .   '     |  |  
`--'     |  '--' /|  '--.|  | |  |'  '--'\|  |\   \|  '-'  /|  | |  |'  '--'\|  |\   \    `--'  
.--.     `------' `-----'`--' `--' `-----'`--' '--' `-----' `--' `--' `-----'`--' '--'    .--.  
'--'                                                                                      '--' 
					''')
				print("[D] Dealer has a blackjack!")
				time.sleep(0.75)
				break

				
			# The dealer will always Hit until the Dealer's
			#	value meets or exceeds 17
			if (dealers_hand_value < 17):
				print("[D] Dealer: HIT ME!")
				print("Drawing a card...")
				time.sleep(0.75)
				drawn_card = shuffled_cards.pop()
				print(
				'''


				''')
				time.sleep(0.75)
				print("[D] Dealer drew a:", drawn_card)

				dealers_hand.append(drawn_card)
				print("[D] Dealer's hand is now:")
				print(dealers_hand)
				time.sleep(0.75)
				print("Calculating dealer's hand:")
				dealers_hand_value = calculate_hand(card_deck, dealers_hand)
				time.sleep(0.75)
				if (dealers_hand_value > 21):
					print('''
 ______            _______ _________ _______  ______   _  _ 
(  ___ \ |\     /|(  ____ \\__   __/(  ____ \(  __  \ ( )( )
| (   ) )| )   ( || (    \/   ) (   | (    \/| (  \  )| || |
| (__/ / | |   | || (_____    | |   | (__    | |   ) || || |
|  __ (  | |   | |(_____  )   | |   |  __)   | |   | || || |
| (  \ \ | |   | |      ) |   | |   | (      | |   ) |(_)(_)
| )___) )| (___) |/\____) |   | |   | (____/\| (__/  ) _  _ 
|/ \___/ (_______)\_______)   )_(   (_______/(______/ (_)(_)
						''')
					print("Dealer's went bust with a value of: ", dealers_hand_value)
					break
				else:
					print("[D] Dealer's hand is: {}".format(dealers_hand_value))

			elif (17 <= dealers_hand_value <= 21):
				print("[D] Dealer: Stand.")
				time.sleep(0.75)
				print("Dealer's hand value at: ", dealers_hand_value)
				dealers_turn_in_session = False

		print("[D] Dealer ended their turn with a hand of {} ({})".format(dealers_hand, dealers_hand_value))		
		time.sleep(1.25)
		# 11. Determine the winner and adjust the Player's chips accordingly
		print(
'''
 ----------------------

|  Calculating Winner  |

 ----------------------
''')
		time.sleep(1)
		winnings = calculate_winner(bet_value, players_hand, players_hand_value, dealers_hand, dealers_hand_value)
		print("You won: ${}".format(winnings))
		player.deposit_winnings(winnings)

		# Determine win or loss
		if (winnings > bet_value):
			player.win_loss_count('W')
		elif (winnings == bet_value):
			player.win_loss_count('D')
		else:
			player.win_loss_count('L')

		break