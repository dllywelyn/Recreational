import time
import random
import platform

import os

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

clear()
print("Welcome to the Last Chance Saloon. Let's play some Blackjack!")
time.sleep(2)
total = 0

##  NEED TO WORK OUT HOW TO SHOW PICTURE CARD, i.e. 'J' BUT HOLD TRUE VALUE (11)
dic = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}
deck = ["2","2","2","2","3","3","3","3","4","4","4","4","5","5","5","5","6","6","6","6","7","7","7","7",
"8","8","8","8","9","9","9","9","10","10","10","10","J","J","J","J","Q","Q","Q","Q","K","K","K","K",
"A","A","A","A"]
    
    



#cards = [card1, card2, card3, card4, card5]
#total = (dic[card1] + dic[card2])
#print(total)
def A():
    if total > 21:
        dic["A"] = 1
def Ad():
    if dtotal > 21:
        dic["A"] = 1
#A()
#print(dic["A"])
        
        
##### if you want Ace to be able to change value, can't say total = total + <nextcard>
## i.e. pick card 3, total = total + card 3. This will have saved the previous value of Ace 
# and build it into the total. Need to keep cards seperate so Ace can retroactively change

#### put whole thing in while = true statement,   if lose (or win)
bjscore = None
while True:
    clear()
    card1 = random.choice(deck)
    deck.remove(card1)
    card2 = random.choice(deck)
    deck.remove(card2)
    card3 = random.choice(deck)
    deck.remove(card3)
    card4 = random.choice(deck)
    deck.remove(card4)
    card5 = random.choice(deck)
    deck.remove(card5)
    print ("Here's your first two cards\n", card1, card2)
    total = (dic[card1] + dic[card2])
    A()
    total = (dic[card1] + dic[card2])
    print("You have", total)
    if total == 21:
        print("21!")
        bjscore = 1         
    elif total < 21:
        hs = input("Hit or stick? [h/s]  ")
        if hs == "s":
            print("Suit yourself")
            bjscore = 1
        elif hs == "h":
            print ("Here's your next card...", card3)
            total = dic[card1] + dic[card2] + dic[card3]
            A()
            total = dic[card1] + dic[card2] + dic[card3]
            print("You have", total)
            if total > 21:
                print("Bust!")
                bjscore = 0                 
            elif total == 21:
                print("21!")
            elif total < 21:
                hs = input("Hit or stick? [h/s]  ")
                if hs == "s":
                    print("Suit yourself")
                    bjscore = 1
                elif hs == "h":
                    print ("Here's your next card...", card4)
                    total = dic[card1] + dic[card2] + dic[card3] + dic[card4]
                    A()
                    total = dic[card1] + dic[card2] + dic[card3] + dic[card4]
                    print("You have", total)
                    if total > 21:
                        print("Bust!")
                        bjscore = 0                         
                    elif total == 21:
                        print("21!")
                    elif total < 21:
                        hs = input("Hit or stick? [h/s]  ")
                        if hs == "s":
                            print("Suit yourself")
                            bjscore = 1
                        elif hs == "h":
                            print ("Here's your next card...", card5)
                            total = dic[card1] + dic[card2] + dic[card3] + dic[card4] + dic[card5]
                            A()
                            total = dic[card1] + dic[card2] + dic[card3] + dic[card4] + dic[card5]
                            print("You have", total)
                            if total > 21:
                                print("Bust!")
                                bjscore = 0                                 
                            elif total == 21:
                                print("21!")
                            elif total < 21:
                                print ("5 Card Charlie! Automatic win!")                                 
    
    
    ### Dealer ###
    #dealer cards
    dcard1 = random.choice(deck)
    deck.remove(dcard1)
    dcard2 = random.choice(deck)
    deck.remove(dcard2)
    dcard3 = random.choice(deck)
    deck.remove(dcard3)
    dcard4 = random.choice(deck)
    deck.remove(dcard4)
    dcard5 = random.choice(deck)
    deck.remove(dcard5)
    if bjscore != 0:
        print ("\nDealer's first two cards are ...\n", dcard1, dcard2)
        dtotal = (dic[dcard1] + dic[dcard2])
        print("Dealer has", dtotal)
        if dtotal == 21:
            print("21! Dealer wins!")
            bjscore = 0         
        elif dtotal == total:
            print("Draw! Dealer wins!")
            bjscore = 0         
        elif dtotal > total and dtotal < 21:
            print("Stick, dealer wins!")
            bjscore = 0         
        elif dtotal < 21 and dtotal < total:
            print ("Dealer's next card ... ", flush=True, end = "")
            time.sleep(2) 
            print(dcard3)
            dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3]
            Ad()
            dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3]
            print("Dealer has", dtotal)
            if dtotal > 21:
                print("Dealer's bust!")
                bjscore = 1             
            elif dtotal == total:
                print("Draw! Dealer wins!")
                bjscore = 0
            elif dtotal == 21:
                print("21! Dealer wins!")
                bjscore = 0             
            elif dtotal > total and dtotal < 21:
                print("Stick, dealer wins!")
                bjscore = 0             
            elif dtotal < 21 and dtotal < total:
                print ("Dealer's next card ... ", flush=True, end = "")
                time.sleep(2) 
                print(dcard4)
                dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3] + dic[dcard4]
                Ad()
                dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3] + dic[dcard4]
                print("Dealer has", dtotal)
                if dtotal > 21:
                    print("Dealer's bust!")
                    bjscore = 1                 
                elif dtotal == total:
                    print("Draw! Dealer wins!")
                    bjscore = 0                 
                elif dtotal == 21:
                    print("21! Dealer wins!")
                    bjscore = 0                 
                elif dtotal > total and dtotal < 21:
                    print("Stick, dealer wins!")
                    bjscore = 0                 
                elif dtotal < 21 and dtotal < total:
                    print ("Dealer's next card ... ", flush=True, end = "")
                    time.sleep(2) 
                    print(dcard5)
                    dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3] + dic[dcard4] + dic[card5]
                    Ad()
                    dtotal = dic[dcard1] + dic[dcard2] + dic[dcard3] + dic[dcard4] + dic[card5]
                    print("Dealer has", dtotal)
                    if dtotal > 21:
                        print("Dealer's bust!")
                        bjscore = 1                    
                    elif dtotal == total:
                        print("Draw! Dealer wins!")
                        bjscore = 0                   
                    elif dtotal == 21:
                        print("21! Dealer wins!")
                        bjscore = 0                    
                    elif dtotal > total and dtotal < 21:
                        print("Dealer wins!")
                        bjscore = 0
                    elif dtotal < 21:
                        print ("5 Card Charlie! Automatic win!")
                        bjscore = 0 
                        

        
    if bjscore == 0:
        print("Loser!")
    else:
        print("Winner!")
    retry = input("Would you like to play again? ")
    if retry == "y":
        pass
    else:
        quit()






