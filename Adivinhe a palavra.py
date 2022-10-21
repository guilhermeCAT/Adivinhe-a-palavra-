nome = input('qual o seu nome ? ')
secreto = input('Escolha a palavra secreta: ')
chances = input('escolha o numero de chances: ')
chances = int(chances)
letras = []

while True:
    if chances <= 0:
        print(f'{nome}, Você perdeu.')
        break

    letra = input('Digite a letra: ')

    if len(letra) > 1:
        print('Só vale uma letra.')
        continue

    letras.append(letra)

    if letra in secreto:
        print(f'essa letra "{letra}" existe na palavra secreta.')
    else:
        print(f'essa letra "{letra}" não existe na palavra secreta.')
        letras.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in letras:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')

    if secreto_temporario == secreto:
        print(f'Parabéns {nome}, Você ganhou!!! A palavra secreta era {secreto_temporario}.')
        break
    else:
        print(secreto_temporario)