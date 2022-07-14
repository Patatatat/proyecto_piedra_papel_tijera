import random

def game():
    Rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'


    
    juego = [Rock, paper, scissors]
    

    opponent = juego

    cpu = []

    for i in range(1):
        caracter_random = random.choice(opponent)
        cpu.append(caracter_random)

    cpu = "".join(cpu)
    return cpu

def Rock():
     rock = 'Rock'
     paper = 'Paper'
     scissors = 'Scissors'

     cpu = game()
     player = input('')
     print(cpu)
     if cpu == rock and player == rock:
         print('tie')
         print('please exit with ctrl + C')
     elif cpu == rock and player == paper:
         print('you win')
         print('please exit with ctrl + C')
     elif cpu  == rock and  player == scissors:
         print('you lose')
         print('please exit with ctrl + C')

def Paper():
     rock = 'Rock'
     paper = 'Paper'
     scissors = 'Scissors'

     cpu = game()
     player = input('')
     print(cpu)
     if cpu == paper and player == rock:
         print('tie')
         print('please exit with ctrl + C')
     elif cpu == paper and player == paper:
         print('you win')
         print('please exit with ctrl + C')
     elif cpu  == paper and  player == scissors:
         print('you lose')
         print('please exit with ctrl + C')

def Scissors():
     rock = 'Rock'
     paper = 'Paper'
     scissors = 'Scissors'

     cpu = game()
     player = input('')
     print(cpu)
     if cpu == scissors and player == rock:
         print('tie')
         print('please exit with ctrl + C')
     elif cpu == scissors and player == paper:
         print('you win')
         print('please exit with ctrl + C')
     elif cpu  == scissors and  player == scissors:
         print('you lose')
         print('please exit with ctrl + C')
    

def run():
    print('welcome to Rock, paper, scissors, what do you choose? ')
    print(Rock(), Paper(),  Scissors())


if __name__ == '__main__':
    run()