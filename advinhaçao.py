import random

def jogar():
    print('***************')
    print('BEM VINDO AO JOGO DE ADIVINHAÇÃO!')
    print('***************')

    numero_secreto = random.randrange(1,11)
    total_de_tentativas = 0
    pontos = 50

    print('Qual nível de dificuldade você quer?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nível = int(input('Digite um dos níveis acima: '))

    if (nível == 1):
        total_de_tentativas = 3
    elif (nível == 2):
        total_de_tentativas = 2
    else:
        total_de_tentativas = 1

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        tentativa_str = input('Digite um número 0 e 10: ')
        print('Você digitou ', tentativa_str)
        tentativa = int(tentativa_str)

        if (tentativa < 1 or tentativa > 10):
            print('Você deve digitar um número entre 0 e 10!')
            continue
        acertou = tentativa == numero_secreto;
        maior = tentativa > numero_secreto;

        if(acertou):
            print('Você acertou e fez {} pontos, parabéns!'.format(pontos))
            break
        elif(maior):
            print('Você errou, o número digitado é maior!')
        else:
            print('Você errou, o número digitado é menor')

        pontos_perdidos = (abs(numero_secreto - tentativa)) / 3
        pontos = round(pontos - pontos_perdidos)

    print('Fim do jogo')
    print('O número era {}'.format(numero_secreto))

if(__name__ == '__main__'):
    jogar()