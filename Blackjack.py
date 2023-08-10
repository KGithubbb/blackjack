import random
from random import randint, randrange


text = 'blackJack'
print(text)
backpack = 50
while(backpack > 0):
    print("you have ",backpack,"$ in youre pocket.")
    Bet = input("how much would you bet? :")
#Bet処理
    while(int(Bet) > backpack):
        print("Enter a number that is under",backpack)
        Bet = input("how much would you bet? :")

    print("You betted",Bet,"$.")
    Player1 = randint(1, 12)  # 0～5の範囲の整数値をランダムに取得
    print("Youre  Card:     " + str(Player1))
    player2 = randint(1, 13)
    print("Player2 card:    " + str(player2));
#until 21 or over
    while(player2 < 21): #1/3でストップ welcome
        half = randint(1, 3)                                                                                                                          
        if(half == 1):
            player2 = (int(player2) + randint(1,13))
        elif(half == 2):
            player2 = (int(player2) + randint(1,13))
        if(half == 3):
            break

    while(Player1 <= 21):
        if(Player1 == 21):
            print('it is BlackJack. You won',Player1)
            exit()
        hit = input("hit or else (hit/n)")
        if(hit == 'n'):
            break
        elif((hit == "hit")):
            Player1 = (int(Player1) + randint(1, 13))
        if(Player1 <= 21):
            print(Player1)
#Final results
    Result = Player1 + player2
    SResult = Player1 - player2
    if (SResult == 0): # and or
        print('Draw')
        print("player1:",str(Player1),"player2:",str(player2))
    if(Player1 > player2 and 42 > Result):
        print("player1:",str(Player1),"player2:",str(player2))
        print('you win')
        backpack = backpack + int(Bet)
        print("you got ",Bet)
    elif(Player1 < player2 and 42 > Result):
        print("player1:",str(Player1),"player2:",str(player2))
        backpack = backpack - int(Bet)
        print('You lose')
        print("you lost",Bet)
    elif(Player1 < player2 and 42 < Result):
        print("player1:",str(Player1),"player2:",str(player2))
        print('you win')
        backpack = backpack + int(Bet)
        print("you got ",Bet)
    elif(Player1 > player2 and 42 < Result):
        print("player1:",str(Player1),"player2:",str(player2))
        print('you lose(Over 21)')
        backpack = backpack - int(Bet)
        print("you lost",Bet)
    if int(backpack) <= 0:
        print("you lost.")
