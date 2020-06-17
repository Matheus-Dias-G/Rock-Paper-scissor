import random

import os

def enemy():
    #generate random type of the rock, paper and scissor
    R = 'rock'
    P = 'paper'
    S = 'scissor'
    types = [R, S, P]

    i = types[random.randint(0, len(types)-1)]
    return i


def player():
    #the player chooses who he  prefers
    r_p_s = int(input('which one do you choose:\n1- rock\n2- paper\n3- scissor\n'))
    R = 'rock'
    P = 'paper'
    S = 'scissor'
    types =[R, P, S]

    if r_p_s == 1:
        return types[0]
    elif r_p_s == 2:
        return types[1]
    elif r_p_s == 3:
        return types[2]
    else:
        print('invalid type!')


def who_win():
    #who wil win a deal with your move
    #winning
    if player_move  == 'rock' and enemy_move == 'scissor':
        print('you win!')
    elif player_move  == 'paper' and enemy_move == 'rock':
        print('you win!')
    elif player_move == 'scissor' and enemy_move == 'paper':
        print('you win!')
    #losting
    if player_move == 'rock' and enemy_move == 'paper':
        print('you lost')
    elif player_move == 'paper' and enemy_move == 'scissor':
        print('you lost')
    elif player_move == 'scissor' and enemy_move == 'rock':
        print('you lost')
    elif player_move == enemy_move:
        print('draw')


repeat = False
yes = 'y'
no = 'n'

while repeat is not True:
    os.system('cls' if os.name == 'nt' else 'clear')
    player_move = player()
    print(player_move)
    enemy_move = enemy()
    print('enemy move', enemy_move)
    who_win()
    q = input('try again?[y/n]')
    if q == no:
        repeat = True
    elif q == yes:
        pass
