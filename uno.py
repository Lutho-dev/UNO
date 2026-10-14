import random
#DECK OF CARDS
# - 108 cards 
# - 4 types of colours
# - 25 cards of each colour

#CARDS
# - 19 number cards of each colour
#       - one zero
#       - 2 of each
# - 


#HAND FOR EACH PLAYER
# - 7  cards

#DICARD PILE
# - 1 initial card
# - added with each play

#DRAW PILE
# - 108 initial cards
# - reduced eveytime player draws

#PLAYER
# - 7 cards in the beginning of the round

#TURNS
# - undefined number of turns, turns will continue until a player wins.

#ENDGAME
# - The game ends as soon as theres a winner.

#CARDS
# wild_cards = ("wild_cards","wild_cards","wild_cards","wild_cards","wild_draw_4_card","wild_draw_4_card","wild_draw_4_card","wild_draw_4_card")
# red_cards = (0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,"reverse","reverse","skip","skip","draw","draw")
# yellow_cards = (0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,"reverse","reverse","skip","skip","draw","draw")
# blue_cards = (0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,"reverse","reverse","skip","skip","draw","draw")
# green_cards = (0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,"reverse","reverse","skip","skip","draw","draw")

# deck = {
#     "wild_cards" : wild_cards,
#     "red_cards" : red_cards,
#     "yellow_cards" : yellow_cards,
#     "blue_cards" : blue_cards,
#     "green_cards" : green_cards,
#     }

cards = ["0 red", "1 red", "1 red", "2 red", "2 red", "3 red", "3 red", "4 red", "4 red", "5 red", "5 red", "6 red", "6 red", "7 red", "7 red", "8 red", "8 red", "9 red", "9 red", 
         "0 blue", "1 blue", "1 blue", "2 blue", "2 blue", "3 blue", "3 blue", "4 blue", "4 blue", "5 blue", "5 blue", "6 blue", "6 blue", "7 blue", "7 blue", "8 blue", "8 blue", "9 blue", "9 blue",
         "0 green", "1 green", "1 green", "2 green", "2 green", "3 green", "3 green", "4 green", "4 green", "5 green", "5 green", "6 green", "6 green", "7 green", "7 green", "8 green", "8 green", "9 green", "9 green",         
         "0 yellow", "1 yellow", "1 yellow", "2 yellow", "2 yellow", "3 yellow", "3 yellow", "4 yellow", "4 yellow", "5 yellow", "5 yellow", "6 yellow", "6 yellow", "7 yellow", "7 yellow", "8 yellow", "8 yellow", "9 yellow", "9 yellow",
         ]

def my_hand(cards):
    hand = []
    for card in cards:
        if len(hand) <= 7:
            hand.append(cards)
            return hand
    return hand
print(my_hand(cards))