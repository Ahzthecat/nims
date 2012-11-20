# -*- coding: utf-8 -*-
# Name: Gordon
# Section: MOOC
# nims.py


##Exercise 2.6 – The game of Nims/Stones 
##In this game, two players sit in front of a pile of 100 stones.
##They take turns, each removing between 1 and 5 stones (assuming
##there are at least 5 stones left in the pile). The person who
##removes the last stone(s) wins. Download nims.py from the website
##and open it up. Check out the lines of text in between the sets
##of ’’’, underneath the deﬁnition of play nims. This is called a
##docstring, and is handy to use to tell users of your program what
##parameters to pass in, and what your program does. 
##In this problem, you’ll write a function to play this game;
##we’ve outlined it for you. It may seem tricky, so break it down
##into parts. Like many programs, we have to use nested loops
##(one loop inside another). In the outermost loop, we want to
##keep playing until we are out of stones. Inside that, we want
##to keep alternating players. You have the option of either
##writing two blocks of code, or keeping a variable that tracks
##the current player. The second way could be slightly trickier,
##but it’s deﬁnitely do-able! 
##Finally, we might want to have an innermost loop that checks if
##the user’s input is valid. Is it a number? Is it a valid number
##(e.g. between 1 and 5)? Are there enough stones in the pile to
##take off this many? If any of these answers are no, we should
##tell the user and re-ask them the question. 
##As always, feel free to ask the LAs for help on any part of this problem. 
##If you choose to write two blocks of code, the basic outline
##of the program should be something like this: 
##while [pile is not empty]:
##while [player 1’s answer is not valid]:
##[ask player 1]
##[execute player 1’s move]
##
##[same as above for player 2] 
##Be careful with the validity checks. Speciﬁcally, we want to
##keep asking player 1 for their choice as long as their answer
##is not valid, BUT we want to make sure we ask them at least ONCE.
##So, for example, we will want to keep a variable that tracks
##whether their answer is valid, and set it to False initially. 
##When you’re ﬁnished, test each other’s programs by playing them! 



def play_nims(pile, max_stones):
##    '''
##    An interactive two-person game; also known as Stones.
##    @param pile: the number of stones in the pile to start
##    @param max_stones: the maximum number of stones you can take on one turn
##    '''


    print"""

                    Let's Play Nim's stones!
            It is a simple game of numbers for two players.


                              Not really a lot of fun, tho...
                              """
    pile=100
    max_stones=5

    while pile>=1:
        p1a=raw_input("\nPlayer one, how many stones do you take? ")
        while p1a!="1" and p1a!="2" and p1a!="3" and p1a!="4" and p1a!="5":
            print"You can't have that."
            p1a=raw_input("How many stones? ")
        p1a=int(p1a)
        while p1a>=max_stones or p1a<=0:
            if p1a>=max_stones:
                print"That's too many.  Try again."
                p1a=int(raw_input("How many stones do you take? "))
            elif p1a>=pile:
                print"That's too many.  Try again."
                p1a=int(raw_input("How many stones do you take? "))
            elif p1a<=0:
                print"You can't do that.  Try again."
                p1a=int(raw_input("How many stones do you take? "))
            else:
                print "Player 1 takes",p1a,"stones."
            pile = pile - p1a

        p2a=raw_input("\nPlayer 2, how many stones? ")
        while p2a!="1" and p2a!="2" and p2a!="3" and p2a!="4" and p2a!="5":
            print"You can't have that."
            p2a=raw_input("How many stones? ")
        p2a=int(p2a)
                        
        while p2a>=max_stones or p2a<=0:
            
            if p2a>=max_stones:
                print"That's too many.  Try again."
                p2a=int(raw_input("How many stones do you take? "))
            elif p1a>=pile:
                print"That's too many.  Try again."
                p2a=int(raw_input("How many stones do you take? "))
            elif p2a<=0:
                print"You can't do that.  Try again."
                p2a=int(raw_input("How many stones do you take? "))
            else:
                print "Player 2 takes",p1a,"stones."
        pile = pile - p2a
                


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
