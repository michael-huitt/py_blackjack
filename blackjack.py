import random ##for shuffle
from os import system ##for screen clearing

SEPERATOR_LEN = 30

balance = 1000
wager = 15 ##default, can be changed in main game loop

def calculate_score(hand):
    score = 0 
    num_aces = 0 
    for card in hand:
        if card[0] == 'J' or 'K' or 'Q': score += 10
        elif card[0] == 'A': num_aces += 1
        else: score += card[0]

def display_hand(hand):
    for card in hand:
        if card == hand[-1]:
            print(card)
        else:
            print(card, end = ", ")

def display_header():
    print('=' * SEPERATOR_LEN)
    print(f"BALANCE: {balance}\nWAGER: {wager}")
    print('-' * SEPERATOR_LEN)

def main():
    player_hand = []
    dealer_hand = []
    deck = [] 
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"] 
        
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
        
    random.shuffle(deck)
       
    system("clear || cls") 
    display_header()

    print("PLAY? (y/n)")
    yn_prompt = input()
        
    if yn_prompt.lower() == "y":
        player_score = dealer_score = 0 

        for draw in range(2):
            dealer_hand.append(deck.pop())
            player_hand.append(deck.pop())
            
        system("clear || cls")
        display_header()
        print(f"DEALER HAND: {dealer_hand[0]}\n\nPLAYER HAND:")
        display_hand(player_hand)
        print(calculate_score(player_hand))

        input()
        
    elif yn_prompt.lower() == "n":
        return

main()
