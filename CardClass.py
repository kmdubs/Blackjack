class Card():
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	
	def __str__(self):
		if self.value == 11:
			printCard = "Jack of " + self.suit
		elif self.value == 12:
			printCard = "Queen of " + self.suit
		elif self.value == 13:
			printCard = "King of " + self.suit
		elif  self.value == 14:
			printCard = "Ace of " + self.suit
		else:
			printCard = str(self.value) + " of " + self.suit
		return printCard

	def __repr__(self):
		if self.value == 11:
			printCard = "Jack of " + self.suit
		elif self.value == 12:
			printCard = "Queen of " + self.suit
		elif self.value == 13:
			printCard = "King of " + self.suit
		elif  self.value == 14:
			printCard = "Ace of " + self.suit
		else:
			printCard = str(self.value) + " of " + self.suit
		return printCard

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit


if __name__ == '__main__':
	card1 = Card(14, "clubs")

	a = card1.getValue()
	print a

	print card1

	suit = card1.getSuit()

