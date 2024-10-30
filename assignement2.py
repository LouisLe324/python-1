ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jester', 'Queen', 'King', 'Ace')
suits = ('hearts', 'diamonds', 'clubs', 'spades')
deck = [(rank, suit) for rank in ranks for suit in suits]
import random
random.shuffle(deck)
import time

def card_comparisons(p1_card, p2_card):

    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) == ranks.index(p2_card[0]):
        return 0
    else:
        return 2

def play_round(p1_deck, p2_deck):
    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        
        p1score = len(p1_deck)
        p2score = len(p2_deck)

        print(f"Player 1's card is {p1_card}")
        print(f"Player 2's card is {p2_card}")

        result = card_comparisons(p1_card, p2_card)
        
        time.sleep(1)

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
            tie(p1_deck, p2_deck, p1_card, p2_card)
        
        time.sleep(1)
        print(f"Player 1 is at {p1score} cards and Player 2 is at {p2score} cards")
        time.sleep(1)

        if len(p1_deck) == 0:
            print("Player 1 wins the game!")
            break
        elif len(p2_deck) == 0:
            print("Player 2 wins the game!")
            break

def tie(p1_deck, p2_deck, p1_card, p2_card):
    print("Both players will put three cards down and whoever's fourth card is the biggest wins it all!")

    p1_tiedeck = [p1_card]
    p2_tiedeck = [p2_card]
    

    
    for x in range(3):
        p1_tiedeck.append(p1_deck.pop(0))
        p2_tiedeck.append(p2_deck.pop(0))

    result = card_comparisons(p1_tiedeck[1], p2_tiedeck[-1])
    
    time.sleep(1)


    if len(p1_deck) < 4 or len(p2_deck) < 4:
        if len(p1_deck) < 4:
            print("Player 1 doesn't have enough cards for a tie and loses!")
            p1_deck.clear()
        else:
            print("Player 2 doesn't have enough cards for a tie and loses!")
            p2_deck.clear()
        return
    
    print(f"Player 1's card is {p1_tiedeck[-1]}")
    print(f"Player 2's card is {p2_tiedeck[-1]}")
    
    time.sleep(1)

    if result == 1:
        print("Player 1 wins the tie!")
        
        p1_deck.extend(p1_tiedeck + p2_tiedeck)

    elif result == 2:

        print("Player 2 wins the tie!")
        
        p2_deck.extend(p1_tiedeck + p2_tiedeck)
    
    else:
        print("Tie again!")
        tie(p1_deck, p2_deck, p1_tiedeck[-1], p2_tiedeck[-1])





def start_game(deck):
    
    p1_deck = deck[:26]
    p2_deck = deck[26:]
    
    play_round(p1_deck, p2_deck)


