import random

# Create and shuffle deck of cards
def shuffle_deck(deck):
	print("Shuffling the deck...")
	shuffled_cards = list(deck.keys())

	for times in range(0, random.randint(2,6)):
		random.shuffle(shuffled_cards)
		
	return shuffled_cards

# Game in session


# Expecting a list of cards
def calculate_hand(deck, hand):
	# For each card in the hand
	value = 0
	number_of_aces = 0

	# Loops through all the cards available in the given hand
	for card in hand:
		# Match the corresponding key in the card_deck dictionary
		# Find the corresponding value attached to that key
		# Add it as a sum to calculate
		value = value + deck[card]

		# Detect if card is an ace
		if card.startswith("Ace"):
			# Value = value + 10 (1 -> 11)
			value += 10
			# 'number_of_aces' counter should be incremented by 1
			number_of_aces += 1

		# Detect if the hand is about to go bust
		if value > 21:
			# Check if there are aces in the hand
			if number_of_aces != 0:
				value -= 10
				number_of_aces -= 1
			else:
				pass

	return value

# Calculate Winner
def calculate_winner(betAmount, handOne, valueOne, handTwo, valueTwo):
	# Scenario: Player busted.
	if (valueOne > 21):
		# Payout: Player loses the money.
		print("Outcome: Player busted.")
		return 0

	# Scenario: Player and dealer both have a blackjack
	elif ((valueOne == 21) and (valueTwo == 21)) and ((len(handOne) == 2) and (len(handTwo == 2))):
		# Payout: No winnings. Refund bet value to player
		print("Outcome: Player and dealer both have a blackjack.")
		return betAmount

	# Scenario: Player wins with a blackjack and
	#	dealer doesn't have a blackjack.
	elif (valueOne == 21 and (len(handOne)) == 2):
		print("Outcome: Player wins with a blackjack and dealer doesn't have a blackjack.")
		# Payout 3:2
		return betAmount * 2.5
		
	# Scenario: Dealer busts and player did not.
	elif (valueTwo > 21) and (valueOne <= 21):
		print("Outcome: Dealer busted and player remained in the game.")
		return betAmount * 2

	# Scenario: Player and dealer both have the same value
	elif (valueOne == valueTwo):
		print("Outcome: Player and dealer both have the same value.")
		# Payout: No winnings. Refund bet value to player
		return betAmount

	# Scenario: Player wins with higher value than dealers hand.
	elif (valueOne > valueTwo):
		print("Outcome: Player wins with higher value than dealers hand.")
		# Payout: 1:1
		return betAmount * 2

	# Scenario: Player loses because dealer has a higher hand higher
	elif (valueTwo > valueOne):
		print("Outcome: Player loses because dealer had a higher hand.")
		return 0

	return betAmount