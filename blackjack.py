import config
import random

def card():
    deck_index = random.randint(0,12)
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return deck[deck_index]


def first_deal():
    for i in range(0,2):
        config.player.append(card())
        config.computer.append(card())


def deal_again(hand):
    hand.append(card())


def player_total(hand):
    hand_size = len(hand)
    player_points = 0
    for i in range(0,hand_size):
        player_points += hand[i]
    return player_points


def game_rules():
    if config.points["player"] > 21 and config.points["computer"] > 21:
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nGame over. Both players bust.\n")
    elif config.points["player"] == 21 and config.points["computer"] == 21:
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nDraw. Boths players win!\n")
    elif config.points["player"] == 21:
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nYou win!\n")
    elif config.points["computer"] == 21: 
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nThe computer wins!\n")
    elif config.points["player"] > 21:
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nThe computer wins!\n")
    elif config.points["computer"] > 21: 
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nYou win!\n")
    else:
        print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's first card: {config.computer[0]}\n")
        draw_again = input("Type 'y' to get another card, type 'n' to pass.\n")
        
        if draw_again == "y":
            deal_again(config.player)
            player_total(config.player)
            config.points["player"] = player_total(config.player)
            game_rules()
            
        else:
            
            while player_total(config.computer) < 17:
                deal_again(config.computer)
                player_total(config.computer)
                config.points["computer"] = player_total(config.computer)
                
            if config.points["player"] > config.points["computer"]:
                print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nYou win!\n")
                
            elif config.points["player"] == config.points["computer"]:
                print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nDraw!\n")
                
            else:
                print(f"Your cards: {config.player}, current score: {config.points['player']}\nComputer's cards: {config.computer}, Computer's score: {config.points['computer']}\nComputer wins!\n")
