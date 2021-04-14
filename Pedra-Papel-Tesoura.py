from random import choice
from colorama import (
    init,
    Fore,
    Back,
    Style
)
init()

"""
Meu Segundo programa feito em Python,Criando Jogo Pedra,Papel e Tesoura com Random 
"""
def game():
    dice = ['Pedra', 'Papel', 'Tesoura']
    foite = choice(dice)
    print(Style.BRIGHT+Fore.GREEN+'Pedra = '+Fore.RED+ ' 1', Style.BRIGHT+Fore.GREEN+ 'Tesoura =' +Fore.RED+ ' 2' ,Style.BRIGHT+Fore.GREEN+ 'Papel = '+Fore.RED+'3')
    var = 0
    try:
         var = int(input(Style.BRIGHT+Fore.BLUE+'Escolha entre uns dos 3 '))
         while var > 3 or var == 0:
             print(Fore.RED +Style.BRIGHT+'Numero invalido')
             break
    except ValueError:
        print(Fore.RED  +Style.BRIGHT+'Valor incorreto ')
    except UnboundLocalError:
        print(Fore.RED +Style.BRIGHT+'Valor incorreta')
    pedra = 0
    tesoura = 0
    papel = 0
    if var == 1:
        pedra+=1
    elif var == 2:
        tesoura+=2
    elif var == 3:
        papel+=3
    def func1(args):
        if args == 1:
            print(Fore.BLUE  +Style.BRIGHT+'Você :--> Pedra')
        elif args == 2:
            print(Fore.BLUE  +Style.BRIGHT+'Você :--> Tesoura')
        elif args == 3:
            print(Fore.BLUE  +Style.BRIGHT+'Você :--> Papel')
    tst =  max(pedra, tesoura, papel)
    fiote = 0
    if tst == 1:
        fiote = 'Pedra'
    elif tst == 2:
        fiote = 'Tesoura'
    elif tst == 3:
        fiote = 'Papel'
    func1(tst)
    print(Fore.RED+Style.BRIGHT+'Computador :-->',foite)
    if fiote == foite:
        print(Fore.GREEN +Style.BRIGHT+'Impate')
    elif fiote == 'Pedra' and foite == 'Papel' :
        print('Computador'+Fore.GREEN+ Style.BRIGHT+' Wins')
        print(Fore.MAGENTA+'Papel ganha de Pedra')
    elif fiote == 'Pedra' and foite == 'Tesoura':
        print(Fore.YELLOW+Style.BRIGHT+'Parabéns')
        print(Fore.MAGENTA+'Tesoura ganha de Pedra')
    elif fiote == 'Papel' and foite == 'Pedra':
        print(Fore.YELLOW+Style.BRIGHT+'Parabéns')
        print(Fore.MAGENTA+'Papel ganha de Pedra')
    elif fiote == 'Papel' and foite == 'Tesoura':
        print('Computador'+Fore.GREEN+Style.BRIGHT+ ' Wins')
        print(Fore.MAGENTA+'Papel perde pra Tesoura')
    elif fiote == 'Tesoura' and foite == 'Pedra':
        print('Computador' + Fore.GREEN + Style.BRIGHT+' Wins')
        print(Fore.MAGENTA+'Tesoura perde pra Pedra')
    elif fiote == 'Tesoura' and foite == 'Papel':
        print(Fore.YELLOW+Style.BRIGHT+'Parabéns')
        print(Fore.MAGENTA+'Tesoura ganha  de Papel')


game()