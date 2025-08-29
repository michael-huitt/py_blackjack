import random #for shuffle
import os

term_size = os.get_terminal_size()

SEPERATOR_LEN = term_size.columns   #length of the seperators that appear on screen

balance = 1000
wager = 15                          #default, can be changed in main game loop
winnings = 0

def add_balance():
    global balance
    balance += wager

def subtract_balance():
    global balance
    balance -= wager

def calculate_score(hand):
    score = 0 
    num_aces = 0 
    
    for card in hand:
        rank = card.split(" ")[0] 
        
        if rank in ("Jack", "Queen", "King"):
            score += 10
        
        elif rank == "Ace":
            score += 11 
            num_aces += 1
        
        else:
            score += int(rank)

    for ace in range(num_aces):
        if score > 21:
            score -= 10

    return score

def compare_scores(p1_score, p2_score):
        scores = [p1_score, p2_score]
        scores.sort(reverse = True)
        
        for score in scores:
            if int(score) > 21:
                scores.remove(score)
        
        if len(scores) == 1:
            return scores[0]

        elif len(scores) == 0:
            return 1

        elif len(scores) == 2:
            if scores[0] != scores[1]:
                return scores[0]
            
            else:
                return 0

##functions with the prefix 'display' handles
##the display of global variables such as winnings

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

def display_footer():
    print('-' * SEPERATOR_LEN)
    print(f"WINNINGS: {winnings}")
    print('=' * SEPERATOR_LEN)

def main():
    player_hand = []
    dealer_hand = []
    deck = [] 
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "King", "Queen", "Ace"] 
        
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")
        
    random.shuffle(deck)
       
    os.system("clear || cls") 
    display_header()
    display_footer() 
    
    print("DEAL? (y/n)")
    yn_prompt = input()

    if yn_prompt.lower() == "y":
        player_score = dealer_score = 0 

        for draw in range(2):
            dealer_hand.append(deck.pop())
            player_hand.append(deck.pop())
            
        while player_score < 21:    #player's turn
            player_score = calculate_score(player_hand) 
            os.system("clear || cls")
            display_header()
            print(f"HOUSE'S HAND: {dealer_hand[0]}\n\nPLAYER HAND: ", end = '')
            display_hand(player_hand)
            print(f"SCORE: {player_score}") 
            
            if player_score > 21:
                break

            display_footer()
            print("HIT OR STAND (y for hit):")
            
            yn_prompt = input()
            
            if yn_prompt.lower() == "y":
                player_hand.append(deck.pop())
            elif yn_prompt.lower() == "n":
                break

        while dealer_score < 16:    #dealer's turn
            dealer_score = calculate_score(dealer_hand)
            os.system("clear || cls")
            display_header()
            print("HOUSE'S HAND: ", end = '') 
            display_hand(dealer_hand) 
            print(f"HOUSE'S SCORE: {dealer_score}\n")
            print("PLAYER HAND: ", end = '')
            display_hand(player_hand)
            print(f"SCORE: {player_score}")
            dealer_hand.append(deck.pop())
            display_footer()

        winning_score = compare_scores(player_score, dealer_score) 
        
        if player_score == winning_score:
            print("-= YOU WIN =-")
            add_balance()

        elif dealer_score == winning_score:
            print("-= DEALER WINS =-")
            subtract_balance()

        elif winning_score == 0 or winning_score == 1:
            print("-= TIE =-")

    elif yn_prompt.lower() == "n":
        return

main()
