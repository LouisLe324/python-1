rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jester', 'Queen', 'King', 'Ace')
suits = ('hearts', 'diamonds', 'clubs', 'spades')
deck = [(rank, suit) for rank in ranks for suit in suits]
import random
random.shuffle(deck)
p1_deck = deck[:26]
p2_deck = deck[26:]

card_comparison(deck.pop(0), deck.pop(0))
    

def card_comparisons(p1_card, p2_card):

    if ranks.index(p1_deck[0]) > ranks.index(p2_deck[0]):
        return 1
    elif ranks.index(p1_deck[0]) == ranks.index(p2_deck[0]):
        return 0
    else:
        return 2

def play_round(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        
        print(f"Player 1's card is {p1_card}")
        print(f"Player 2's card is {p2_card}")

        result = card_comparisons(p1_card, p2_card)

        if result == 1:
            print("Player 1 wins the round!")
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        elif result == 2:
            print("Player 2 wins the round!")
            p2_deck.append(p1_card)
            p2_deck.append(p2_card)
        else:
            print("Tie!")
            tie(p1_card, p2_card)


def tie(p1_deck, p2_deck):
    print("Both players will put three cards down and whoever's fourth card is the biggest wins it all!")

    p1_tiedeck = []
    p2_tiedeck = []
    
    p1_card = p1_deck.pop(0) 
    p1_tiedeck.append(p1_card)

    p1_card = p1_deck.pop(0) 
    p1_tiedeck.append(p1_card)

    p1_card = p1_deck.pop(0) 
    p1_tiedeck.append(p1_card)
    
    p2_card = p2_deck.pop(0) 
    p2_tiedeck.append(p2_card)
    
    p2_card = p2_deck.pop(0) 
    p2_tiedeck.append(p2_card)
    
    p2_card = p2_deck.pop(0) 
    p2_tiedeck.append(p2_card)
    
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)

    result = card_comparisons(p1_card, p2_card)
    
    if result == 1:
        print("Player 1 wins the tie!")
        
        p1.append(p1_card)
        
        while len p1_tiedeck > 0
            p1_card = p1_tiedeck(0)
            p1_deck.append(p1_card)
        
        p1.append(p2_card)
    
        while len p2_tiedeck > 0
            p2_card = p2_tiedeck.pop(0)
            p1_deck.append(p2_card)


    elif result == 2:

        print("Player 2 wins the tie!")
        
        p2.append(p1_card)

        while len p1_tiedeck > 0
            p1_card = p1_tiedeck(0)
            p2_deck.append(p1_card)

        p1.append(p2_card)

        while len p2_tiedeck > 0
            p2_card = p2_tiedeck.pop(0)
            p1_deck.append(p2_card)


            p2_deck.append(p2_card)
    
    else:
        print("Tie again!")
        tie(









