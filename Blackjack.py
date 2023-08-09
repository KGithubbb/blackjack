import random
from random import randint, randrange

text = 'blackJack'
print(text)

Player1 = randint(1, 13)  # 0～5の範囲の整数値をランダムに取得
print("Youre  Card:     " + str(Player1))
player2 = randint(1, 13)
print("Player2 card:    " + str(player2))
#until 21 or over
while(player2 < 21): #1/3でストップ
    half = randint(1, 3)
    print(half)
    if(half == 1):
        player2 = (int(player2) + randint(1,13))
    elif(half == 2):
        player2 = (int(player2) + randint(1,13))
    if(half == 3):
        break

while(Player1 <= 21):
    if(Player1 == 21):
        print('it is BlackJack. You won',Player1)
        break
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
elif(Player1 < player2 and 42 > Result):
    print("player1:",str(Player1),"player2:",str(player2))
    print('you lose')
elif(Player1 < player2 and 42 < Result):
    print("player1:",str(Player1),"player2:",str(player2))
    print('you win(Over 21)')
elif(Player1 > player2 and 42 < Result):
    print("player1:",str(Player1),"player2:",str(player2))
    print('you lose(Over 21)')
