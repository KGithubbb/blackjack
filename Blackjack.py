import random
from random import randint, randrange

text = 'blackJack'
print(text)
Player1 = randint(1, 13)  # 0～5の範囲の整数値をランダムに取得
print("Youre Card:" + str(Player1))
player2 = randint(1, 13)
print("Player2 First card:" + str(player2))
#until 21 or over
while(player2 <= 21):
    player2 = (int(player2) + randint(1,12))
    
    
while(Player1 <= 21):
    hit = input("hit or else (hit/n)")
    if(Player1 == 21):
    #text = ('it is BlackJack. You won',Player1)
        print('it is BlackJack. You won',Player1)
    if(hit == "hit", hit == "Hit",hit == "y",hit == "h", hit == "yes"):
        Player1 = (int(Player1) + randint(1, 13))
    if(Player1 <= 21):
        print(Player1)
if(Player1 >= 21):
    print("player1:",str(Player1),"player2:",str(player2))
#Final results
Result = Player1 + player2
SResult = Player1 - player2
if (SResult == 0):
    print('Draw')
elif(Player1 > player2 & 42 > Result):
    print('you win')
elif(Player1 < player2 & 42 > Result):
    print('you lose')
if(Player1 < player2 & 42 < Result):
    print('you win(Over 21)')
elif(Player1 > player2 & 42 < Result):
    print('you lose')