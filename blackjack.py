#Blackjack game
import random

p1cards = []

class Player(object):
  def __init__(self,name,bankroll):
    self.name = name
    self.bankroll = bankroll

  def cards(self,cardone,cardtwo):
    self.cardone = None
    self.cardtwo = None

class Card(object):

  def __init__(self):
    self.card = random.randint(1,10)

#game start
print "Welcome to Blackjack"
playername = raw_input("Enter your name: ")
playerbankroll = input("Enter your bankroll in $$$: ")

#init instance of player
p1 = Player(playername,playerbankroll)

#gameplay
print "Let's play."

while True:
  p1cards.append(Card().card)
  p1cards.append(Card().card)
  #print p1cards.append(random.randint(1,10))

  print "You've got a %d and a %d" %(p1cards[0],p1cards[1])
  action = raw_input("Hit or Stay? :")

  if action == "Hit":
    p1.cardt



