#! /usr/bin/env python

player1_hand1 = '5H 5C 6S 7S KD'
player2_hand1 = '2C 3S 8S 8D TD'

def highestCard(hand):
    
    i = [0, 3, 6, 9, 12]
    highest_card = None
    k = False
    q = False
    j = False
    
    for key in i:
        if hand[key] == 'A':
            return 'A'
        if hand[key] == 'K':
            k = True
        if hand[key] == 'Q':
            q = True
        if hand[key] == 'J':
            j = True
        
        if hand[key] > highest_card:
            highest_card = hand[key]
    
    if k:
        return 'K'
    if q:
        return 'Q'
    if j:
        return 'J'
    else:
        return highest_card

print highestCard(player1_hand1)