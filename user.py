class Player:
	def __init__(self, name, balance, win_count=0, draw_count=0, loss_count=0):
		self.name = name
		self.balance = balance
		self.win_count = win_count
		self.draw_count = draw_count
		self.loss_count = loss_count

	def deposit_winnings(self, balance):
		self.balance = self.balance + balance
		print("Your new balance is now ${}".format(self.balance))
		return self.balance

	def make_bet(self, balance):
		# Ensure that bet does not exceed available balance
		if (balance > self.balance):
			print("You don't have enough in your account to make this large of a wager! Place another bet. Your balance is: ${}".format(self.balance))
			return
		else:
			self.balance = self.balance - balance
			print("You've bet ${}, your remaining balance is now: ${}".format(balance, self.balance))
			return self.balance

	def win_loss_count(self, outcome):
		if outcome == 'W':
			self.win_count += 1
		elif outcome == 'D':
			self.draw_count += 1
		elif outcome == 'L':
			self.loss_count += 1

		print('''
___________________________________

|           Your name: {}         |
|           Balance: ${}         |
|            # played: {}           |
|          W:{} | D:{} | L:{}         |
___________________________________
						'''.format(self.name, self.balance, self.win_count + self.loss_count, self.win_count, self.draw_count, self.loss_count))


		return self.win_count, self.draw_count, self.loss_count

	def __str__(self):
		return ('''
___________________________________

|           Your name: {}         |
|           Balance: ${}         |
|            # played: {}           |
|          W:{} | D:{} | L:{}         |
___________________________________
						'''.format(self.name, self.balance, self.win_count + self.loss_count, self.win_count, self.draw_count, self.loss_count))