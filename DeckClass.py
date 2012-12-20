from CardClass import Card
import random

class Deck():
	def __init__(self):
		self._cards = []
		values = range(2,15)
		suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

		for suit in suits:
			for value in values:
				self._cards.append(Card(value, suit))

	def __getitem__(self, key):
		return self._cards[key]

	def shuffle(self):
		l = range(1,len(self._cards))
		l.reverse()
		for i in l:
			j = random.randint(0,i)
			self._cards[j], self._cards[i] = self._cards[i], self._cards[j]

	def __repr__(self):
		return str(self._cards)


if __name__ == '__main__':
	d = Deck()

	print d[51]

	d.shuffle()
	print d			
