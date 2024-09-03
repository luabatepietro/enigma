import numpy as np
from enigma import para_one_hot, para_string, cifrar, de_cifrar, enigma, de_enigma

def demo():
    print("Olá!! Tudo bem? Hoje vou te mostrar alguns sistemas de codificação e decodificação.")
    msg = input("Digite sua frase/palavra que deseja decifrar: ") 

    print("\nPara cifrar esse seu texto/palavra vamos utilizar nossos conhecimentos de álgebra linear. Primeiro, iremos transformar essa frase em uma matriz! Confia em mim, isso vai facilitar o processo depois...")
    matriz = para_one_hot(msg)
    print(f'\nAqui está a matriz que representa sua frase:\n{matriz}\n')

    print("Nessa matriz, cada caractere de sua frase é representado por uma linha e o comprimento da mensagem define o número de colunas!")
    print("Dessa forma, se quisermos saber o que essa matriz significa, podemos usar a nossa função `para_string`, que converte a matriz de volta para uma string legível.")
    print(f'\nUsando `para_string`, recuperamos a frase original: {para_string(matriz)}\n')

    print("\nAgora, vamos aplicar uma cifra de permutação para embaralhar sua mensagem.")

    n = 27  # Tamanho do alfabeto incluindo o espaço
    P = np.eye(n)
    np.random.shuffle(P)  
    
    msg_cifrada = cifrar(msg, P)
    print(f'\nSua mensagem cifrada com a matriz de permutação é: {msg_cifrada}\n')

    print("Podemos também decifrar essa mensagem usando a função `de_cifrar` e a mesma matriz de permutação.")
    msg_decifrada = de_cifrar(msg_cifrada, P)
    print(f'\nSua mensagem decifrada é: {msg_decifrada}\n')

    print("Finalmente, vamos demonstrar a cifra Enigma, que usa duas permutações para codificar a mensagem.")
    
    E = np.eye(n)
    np.random.shuffle(E)  
    msg_enigma = enigma(msg, P, E)
    print(f'\nSua mensagem cifrada com o sistema Enigma é: {msg_enigma}\n')

    print("E agora, vamos decifrar a mensagem Enigma.")
    msg_enigma_decifrada = de_enigma(msg_enigma, P, E)
    print(f'\nSua mensagem decifrada usando o sistema Enigma é: {msg_enigma_decifrada}\n')

    print("Espero que você tenha gostado desta demonstração! Obrigado por participar.")

if __name__ == '__main__':
    demo()
