# python C:\dan\learn\python\rockPaperScissors.py

import random

choices = {'r':'rock','p':'paper','s':'scissors'}
options = [ choices[k] for k in choices.keys() ]
scores = {'computer':0, 'player':0}

while scores['computer']<5 and scores['player']<5:
    computer = random.randint(0,2)

    while 1==1:    
        player = input ( "Enter (r)ock, (p)aper, or (s)cissors: ").lower()[0]
        if player in choices.keys():
            break
        print ( '{} is an invalid selection. Please choose r, p, or s.'.format ( player ) ) 

    if computer == 0: 
        if player == "s":
            result = "I win"
            message = "Rock beats scissors"
            scores['computer'] += 1
        elif player == "p":
            result = "You win"
            message = "Paper beats rock"
            scores['player'] += 1
        else:
            result = "Tie"
            message = "We both have rock"
       
    elif computer == 1: 
        if player == "r":
            result = "I win"
            message = "Paper beats rock"
            scores['computer'] += 1
        elif player == "s":
            result = "You win"
            message = "Scissors beat paper"
            scores['player'] += 1
        else:
            result = "Tie"
            message = "We both have paper"

    elif computer == 2: 
        if player == "p":
            result = "I win"
            message = "Scissors beat paper"
            scores['computer'] += 1
        elif player == "r":
            result = "You win"
            message = "Rock beats scissors"
            scores['player'] += 1
        else:
            result = "Tie"
            message = "We both have scissors"

    print ( "I have {}, you have {}.".format ( options[computer], choices[player] ) )
    print ( "{}. {}.".format ( result, message ) )
    print ( "My score: {} Your score: {}\n".format ( scores['computer'], scores['player'] ) )
