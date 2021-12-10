import random
class DeckOfCardsGame :

  def deck_Of_Cards():

    suit=["Clubs","Diamonds", "Hearts", "Spades"]
    rank =["2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King", "Ace"]
    
    deckOfCards=[]
    player1=[]
    player2=[]
    player3=[]
    player4=[]
    
    
    for i in suit:
      for j in rank:
       cards=(i+j)
       deckOfCards.append(cards)
       
    random.shuffle(deckOfCards)  
    #print(deckOfCards)
    #print(len(deckOfCards))


    for i in range(len(deckOfCards)):
      if(i<=8):
        player1.append(deckOfCards[i])
      elif (9<=i<=17):
        player2.append(deckOfCards[i])
      elif(18<=i<=26):
        player3.append(deckOfCards[i])
      elif(27<=i<=35):
        player4.append(deckOfCards[i])
      else:
        pending=deckOfCards[i]
    
    print("player1 : ",player1)
    print("player2 : ",player2)
    print("player3 : ",player3)
    print("player4 : ",player4)

  deck_Of_Cards()   
      
