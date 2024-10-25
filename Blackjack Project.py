# First draft
    
"""
def play_blackjack():
    available_cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    user_cards = []
    computer_cards = []
    start_game = str(input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")).lower()
    
    if start_game == 'yes':
        print("\n"*20)
        
        for i in range (2):
            user_cards.append(random.choice(available_cards))
        total_amount = int(sum(user_cards))
        print(f"Your cards : {user_cards} , current score :  {total_amount}")
                
        for i in range(1):
            computer_cards.append(random.choice(available_cards))
        total_amount_computer = int(sum(computer_cards) )  
        print(f"Computer's first card: {computer_cards}")
        
        if total_amount == 21 and total_amount_computer == 21:
            print ("It's a tie!")
            play_blackjack()
            
        elif total_amount == 21:
           print ("It's a tie!")
           play_blackjack()     
            
        elif total_amount_computer == 21:
            print ("The computer did a black jack and won!")
            play_blackjack()
            
        
        keep_playing = str(input("Type 'yes' to get another card, type 'no' to pass: ")).lower()
        get_another_card = True
        
        
        while get_another_card:
            if keep_playing == "yes":
                
                user_cards.append(random.choice(available_cards))
                total_amount = int(sum(user_cards))
                print(f"Your cards : {user_cards} , current score :  {total_amount}")
                
                while total_amount_computer < 17: 
                    computer_cards.append(random.choice(available_cards))
                    total_amount_computer = int(sum(computer_cards))
                print(f"Computer's cards: {computer_cards}, current score : {total_amount_computer}")
                
                if total_amount_computer > 21:
                    get_another_card = False
                elif total_amount < 21:
                    keep_playing = str(input("Type 'yes' to get another card, type 'no' to pass: ")).lower()
                else:
                    get_another_card = False
                
            else:
                get_another_card = False
                
                
        else:
            print (f"Your final hand: {user_cards} , final score :  {total_amount}")
            
            while total_amount_computer < 17: 
                computer_cards.append(random.choice(available_cards))
                total_amount_computer = int(sum(computer_cards))
                
            print(f"Computer's final hand: {computer_cards}, final score {total_amount_computer}")
                
            if total_amount > 21:
                print ("You went over. You lost. :( ")
            
            elif total_amount_computer > 21:
                print ("Computer went over. You won!")
                
            elif total_amount == 21:
                print ("You did a black jack and won!")
                
            elif total_amount_computer == 21:
                print ("The computer did a black jack, you lost! :( ")
                
            elif total_amount < total_amount_computer:
                print ("Computer got closer to 21! You  lost.")
                
            elif total_amount > total_amount_computer:
                print ("You got closer to 21! You  won.")
                
            elif total_amount == total_amount_computer:
                print ("That's a Tie!")
            
            play_blackjack()
            
    else:
        print("Game over!")


play_blackjack()"""
 
# Second draft

import random

# Deal and select a random card
def deal_card():
    available_cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    card = random.choice(available_cards)
    return card
    
# Calculate the score of each player
def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        # Return 0 means we have BlackJack
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
       
    # This return statement is out of the loop to do the um in any other case    
    return sum(cards)


# Function to compare the results

def compare(user_input, computer_input):
    
    if user_input == computer_input:
        print("It's a draw")
        black_jack()
        
    elif user_input == 0:
        print ("You won with a BlackJack!")
        black_jack()
        
    elif computer_input == 0:
        print ("The house won!")
        black_jack()
        
    elif user_input > 21:
        print ("You lost!")
        black_jack()
        
    elif computer_input > 21:
        print ("Computer lost.")
        black_jack()
        
    elif user_input > computer_input:
        print ("You won!")
        black_jack()
        
    else:
        print("You lost")
        black_jack()
        
    
# Start of the game
def black_jack():
    play_game = input("Do you want to play a game of Black Jack? Type 'yes' or no 'no' : ")
    
    if play_game == "yes":
        print("\n"*20)
    
        # Deal the user and computer two cards each 
        user_cards = []
        computer_cards = []
        # To monitor the game results
        game_over = False
        
        for i in range (2):
            # += is used to joins the objects (like the .extend() function) while .append() is adding an element to the list in place. 
            user_cards.append(deal_card())
            computer_cards.append(deal_card())       
            
        
        while not game_over:
            # Call the score function to calculate each user's score 
            user_score = calculate_score(user_cards) 
            computer_score = calculate_score(computer_cards)
            
            print(f"Your cards : {user_cards} , current score :  {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
                
            # First, check if the game is over already
            if user_score == 21 or computer_score == 21 or user_score > 21:
                game_over = True      
            else:
                keep_playing = str(input("Type 'yes' to get another card, type 'no' to pass: ")).lower()
                    
                if keep_playing == "yes":
                    # User plays one more card
                    user_cards.append(deal_card())
                else:
                    game_over = True
                        
        #The computer should be playing more cards until it reaches a score higher than 17
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            
        print("\n"*20)   
        print(f" Your final hand : {user_cards} , score :  {user_score}")
        print(f" Computer's final hand : {computer_cards} ,  score :  {computer_score}")      
        print(compare(user_score,computer_score))

    else:
        print("We hope to see you back soon!")

# To launch the program
black_jack()
        
        
    

    
    
    

