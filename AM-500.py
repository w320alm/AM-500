
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:44:27 2018

@author: austinmcdonnell
"""
#import matplotlib.pyplot as plt (need to updat matplotlib.pyplot)
from numpy import sin, cos, arange,pi
import smtplib


# This function adds two numbers 
def add(x, y, z, a):
   return x + y + z + a

# This function subtracts two numbers 
def subtract(x, y, z, a):
   return x - y -z -a


# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

#This function raises first number to the power of second number
def exp(x,y):
   return x**y

#This function takes the square root of number
def sqrt(x):
   return x**.5

#This function will give you the reciprical
def reciprocal(x):
    return 1/x

#This function will convert from radians to degrees
def degree(x):
    return (180/pi)*x

#This function will convert from degrees to radians
def radian(x):
    return (pi/180)*x

#This will solve the hypotenus for right triangle
def hyp(a,b):
    return sqrt((a**2)+(b**2))

print("You have entered the AM-500, my way of learning Python")
print("Please choose one of the following")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponential")
print("6.Square Root")
print("7.Reciprocal")
print("8.Plot Sine Wave")
print("9.Plot Cosine Wave")
print("10.Plot Sine(Red) and Cosine(Green)")
print("11.Radians to Degrees")
print("12.Degree to Radians")
print("13.Age Calculator")
print("14.Tip Calculator")
print("15.Send an Email")
print("16. Hyp of Triangle")
print("17. Black Jack")

# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17):")

if choice == '1':
    print("How many numbers will you be adding")
    ch=input("Enter how many numbers to be added: 2/3/4:")
    if ch=='2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = 0
        num4 = 0
        print(num1,"+",num2,"=", add(num1,num2,num3,num4))
    elif ch=='3':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         num3 = float(input("Enter third number: "))
         num4 = 0
         print(num1,"+", num2,"+",num3,"=", add(num1,num2,num3,num4))
    elif ch=='4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        print(num1,"+", num2,"+",num3,"+",num4,"=", add(num1,num2,num3,num4))
        
elif choice == '2':
    print("How many numbers will you be subtracting")
    ch=input("Enter how many numbers to be added: 2/3/4:")
    if ch=='2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = 0
        num4 = 0
        print(num1,"+",num2,"=", add(num1,num2,num3,num4))
        
    elif ch=='3':
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))
         num3 = float(input("Enter third number: "))
         num4 = 0
         print(num1,"+", num2,"+",num3,"=", add(num1,num2,num3,num4))
         
    elif ch=='4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        print(num1,"+", num2,"+",num3,"=", add(num1,num2,num3,num4))
        
elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1,"*",num2,"=", multiply(num1,num2))
    
elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1,"/",num2,"=", divide(num1,num2))
    
elif choice =='5':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1,"^",num2,"=", exp(num1,num2))
    
elif choice == '6':
    num1 = float(input("Enter number: "))
    print(num1,"sqrt", "=", sqrt(num1))
    
elif choice == '7':
    num1 = float(input("Enter number: "))
    print(num1,"reciprocal","=", reciprocal(num1))
    
elif choice =='8':
    num1 = float(input("Enter x starting number: "))
    num2 = float(input("Enter x ending number: "))
    x=arange(num1,num2,.01)
    y=sin(x)
    plt.plot(x,y)
    plt.show()
    
elif choice == '9':
    num1 = float(input("Enter x starting number: "))
    num2 = float(input("Enter x ending number: "))
    x=arange(num1,num2,.01)
    y=cos(x)
    plt.plot(x,y)
    plt.show()
    
elif choice =='10':
    num1 = float(input("Enter x starting number: "))
    num2 = float(input("Enter x ending number: "))
    x=arange(num1,num2,.01)
    y=sin(x)
    z=cos(x)
    plt.plot(x,y,'r')
    plt.plot(x,z,'g')
    plt.show()
    
elif choice =='11':
    num1 = float(input("Enter number: "))
    print(num1,"radian","=", degree(num1),"degrees")
    
elif choice =='12':
    num1 = float(input("Enter number: "))
    print(num1,"degrees","=", radian(num1),"radians")
    
elif choice =='13':
    mon = int(input("Enter The Current Month MM "))
    day = int(input("Enter The Current Day DD "))
    yr = int(input("Enter The Current Year YYYY "))
    mon1 = int(input("Enter The Birthday Month MM "))
    day1 = int(input("Enter The Birthday Day DD "))
    yr1 = int(input("Enter The Birthday Year YYYY "))
    a = mon-mon1
    b = yr-yr1
    if a<0:
        c = b-1
        e = 11-abs(a)
        print("Today you are this old ", c,"years",e,"months") 
    elif a>0:
        h = b
        i = a
        print("Today you are this old ", h,"years",i,"months") 
    elif a==0:
        j = b
        print("Today you are this old ", j,"years",a,"months") 
        
elif choice =='14':
    num1=float(input("Enter the Total for the meal "))
    num2=float(input("Enter the Percent Tip you want to give "))
    num3=num2/100
    num4=num1*num3
    print("The Tip that you want to give is ",num4)
    
elif choice =='15':
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your email address", "Password") 
    recp=str(input("write out the email address this is being sent to"))
    msg = str(input("Write out your email"))
    server.sendmail("email of person recieving", recp, msg)
    server.quit()

elif choice == '16':
    num1 = float(input("Enter the first leg of the triangle "))
    num2 = float(input("Enter the second leg of the triangle "))
    print("The hyp is:", hyp(num1,num2))
    
elif choice =='17':
    import deck, interface

    card_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
            'J':10, 'Q':10, 'K':10, 'A':(1,11)}

    WIN = 0
    LOSE = 1
    TIE = 2

    WIN_VALUE = 21
    DEALER_CONDITION = 16   #If equal or lower to condition, dealer draws
    
    class Player():
        """ Player object containing name and hand (list of cards)
            Draw function adds another card to the hand
        """
        def __init__(self, name:str, initial_hand:list):
            self.name = name
            self.hand = initial_hand
    
        def draw(self, deck:list):
            self.hand.append(deck.pop())
    
    def hand_value(hand:list, ace_value:int = 0) -> int:
        """ Returns int value of a player's hand """
        total = 0
        for cards in hand:
            card = cards[1:]     #Not looking at the suit, only card value
            if card == 'A':
                total += card_dict[card][ace_value]
            else:
                total += card_dict[card]
        return total
    
    def hand_isBust(hand:list) -> bool:
        """ Returns true if hand value is over 21, else false """
        return hand_value(hand) > WIN_VALUE
    
    def best_hand(hand:list) -> int:
        """ Returns the better hand value if player contains an Ace card
            If there is no ace card, basically hand value is returned
        """
        ACE_VALUE_1 = 0
        ACE_VALUE_11 = 1
        hand1 =  hand_value(hand, ACE_VALUE_1)
        hand2 = hand_value(hand, ACE_VALUE_11)
        if hand1 == WIN_VALUE:
            return hand1
        elif hand2 <= WIN_VALUE:
            return hand2
        else:
            return hand1
    
    def user_actions(user, deck:list):
        """ Asks what kind of action the user wants. If the user wants to hit, a card is drawn
            from the deck. If the user BUSTS, turn ends automatically and user loses game.
            Function repeats or recursively calls itself until user stays and returns nothing
        """
        action = interface.userInput_move()
        if action.upper() == 'H':
            user.draw(deck)
            print("Updating hand...")
            interface.print_player_hand(user.name, user.hand)
            if hand_isBust(user.hand):
                interface.print_bust_message(user.name)
                return None
            user_actions(user, deck)
    
    def should_draw(dealer) -> bool:
        """ Checks if dealer should draw a card. True to draw, else false
            Checks if either hand has 21, returning False
            Simply base the AI off of the smallest hand value (Ace value of 1)
        """
        hand = best_hand(dealer.hand)
        if hand == WIN_VALUE:
            return False
        return hand <= DEALER_CONDITION
    
    def dealer_actions(dealer, deck:list):
        """ This function will have the dealer AI keep drawing until above
            the DEALER CONDITION
        """
        while should_draw(dealer):
            print("{} is drawing...".format(dealer.name))
            dealer.draw(deck)
            interface.print_dealer_hand(dealer.name, dealer.hand)
        print("{} is ending turn.".format(dealer.name))
    
    def determine_winner(user, dealer) -> int:
        """ If User wins, return WIN value. If User loses, return Lose value.
            If a tie, return TIE value
        """
        user_best_hand = best_hand(user.hand)
        dealer_best_hand = best_hand(dealer.hand)
        if user_best_hand > dealer_best_hand and user_best_hand <= WIN_VALUE:
            return WIN
        if user_best_hand < dealer_best_hand and dealer_best_hand > WIN_VALUE:
            return WIN
        if user_best_hand > dealer_best_hand and dealer_best_hand <= WIN_VALUE:
            return LOSE
        if user_best_hand < dealer_best_hand and dealer_best_hand <= WIN_VALUE:
            return LOSE
        else:
            return TIE
    
    def print_game_result(result:int):
        """ Prints and end game message depending on the game result """
        if result == WIN:
            print("WINNER, WINNER CHICKEN DINNER!")
        elif result == LOSE:
            print("YOU LOSE HA!")
        else:
            print("TIE")
    
    def determine_continue_game() -> bool:
        return interface.userInput_new_game() == 'Y'
    
    def new_game():
        card_deck = deck.create_randomDeck()
        dealer = Player("Dealer", [card_deck.pop(), card_deck.pop()])
        user = Player("You", [card_deck.pop(), card_deck.pop()])
        interface.print_beginning_hands(user.name, user.hand, dealer.name, dealer.hand)
        user_actions(user, card_deck)
        if hand_isBust(user.hand) == False:
            dealer_actions(dealer, card_deck)
        interface.print_reveal_dealer_hand(dealer.name, dealer.hand)
        if hand_isBust(dealer.hand):
            interface.print_bust_message(dealer.name)
        print_game_result(determine_winner(user, dealer))

    def main():
        interface.print_welcome_message()
        CONTINUE_PLAYING = True
        while CONTINUE_PLAYING:
            print("Starting new game!")
            new_game()
            CONTINUE_PLAYING = determine_continue_game()
        interface.print_end_message()
    
    if __name__ == "__main__":
        main()
    
else:
   print("Invalid input")
