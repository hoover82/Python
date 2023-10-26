# python C:\dan\learn\python\rockPaperScissors.py

import random

def get_choice():

    while True:    
        player = None
        try:
            player = input ( "Enter (r)ock, (p)aper, or (s)cissors: ").lower()[0]
            if player in choices.keys():
                break
        except:
            None
        print ( '{} is an invalid selection. Please choose r, p, or s.'.format ( player ) ) 

    return player

def determine_winner ( pair ):

    if pair[0] == pair[1]: 
        winner = "Tie"
        message = "We both have {}".format ( choices[pair[0]] )

    elif set(pair) == {'p','r'}:     
            #PAPER and ROCK
            winner = 'p'
            message = "Paper covers Rock"

    elif set(pair) == {'p','s'}:     
            #PAPER and SCISSORS
            winner = 's'
            message = "Scissors cut Paper"

    elif set(pair) == {'r','s'}:     
            #ROCK and SCISSORS'
            winner = 'r'
            message = "Rock smashes Scissors"

    return winner,message

choices = {'r':'rock','p':'paper','s':'scissors'}
options = [ choices[k] for k in choices.keys() ]
scores = {'computer':0, 'player':0}

while scores['computer']<5 and scores['player']<5:
    computer = [ k for k in choices.keys() ] [ random.randint(0,2) ]
    player = get_choice()
    
    print ( 'computer: {}'.format ( computer ) ) 
    print ( 'player: {}'.format ( player ) ) 

    winner,message = determine_winner ( list ( [computer, player] ) )

    if winner == "Tie":
        result = winner
    elif computer == winner:
        result = "Computer wins"
        scores['computer'] += 1
    elif computer == winner:
        result = "Player wins"
        scores['player'] += 1
    else:
        print ('Fatal logic error!')
        break        
    print ( "Computer has {}, player has {}.".format ( choices[computer], choices[player] ) )
    print ( "{}. {}.".format ( result, message ) )
    print ( "Computer score: {} Player score: {}\n".format ( scores['computer'], scores['player'] ) )
