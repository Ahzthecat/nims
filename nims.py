# Name: Gordon
# Section: MOOC
# nims.py

import random

def play_nims(pile, max_stones):
##    '''
##    An interactive two-person game; also known as Stones.
##    @param pile: the number of stones in the pile to start
##    @param max_stones: the maximum number of stones you can take on one turn
##    '''
##    pile = random.randint(1,50)
##    max_stones = 3

    print"""

                    Let's Play Nim's stones!
            It is a simple game of numbers for two players.


                              Not really a lot of fun, tho...
                              """
    pile=int(raw_input("How many stones shall we start with? (Less than 50 is best) "))
    max_stones=int(raw_input("\nLimit draw to how many stones per turn? "))

    while pile>=0:
        p1a=x
        p2a=y
        while p1a>=max_stones or p1a<=0:
            p1a=raw_input("\nPlayer one, how many stones do you take? ")
            p1a=int(p1a)
            if p1a>=max_stones:
                print"That's too many.  Try again."
                break
            else:
                print "Player 1 takes",p1a,"stones."
            pile = pile - p1a
            p1sts = 0 + p1a
            print "Player 1 has",p1sts,"stones"

        while p2a>=max_stones or p2a<=0:
            p2a=raw_input("\nPlayer 2, how many stones? ")
            p2a=int(p2a)
            if p2a>=max_stones:
                print"That's too many.  Try again."
                break
            else:
                print "Player 2 takes",p2a,"stones."
            pile = pile - p2a
            p2sts = 0 + p2a
            print "Player 2 has",p2sts,"stones"
            print pile,"stones remain."

    if p2sts>=p1sts:
        print"Player 1 is the winner!"
    elif p1sts>=p2sts:
        print"Player 2 is the winner!"
    else:
        print "It's a tie!"

    print"Game Over"


        

    ## Basic structure of program (feel free to alter as you please):

#    while [pile is not empty]:
#        while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
#       
#        while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]
#
#    print "Game over"
play_nims(20,5)
