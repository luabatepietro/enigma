import numpy as np
from typing import Tuple

def gerar_permutacoes(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Gera duas matrizes de permutação de tamanho N x N.
    """
    P = np.eye(N) 
    Q = np.eye(N)
    
    np.random.shuffle(P) 
    np.random.shuffle(Q)  
    
    return P, Q

def one_hot(mensagem: str, alfabeto: str) -> list:
    N = len(alfabeto)
    matriz = []
    
    for char in mensagem:
        linha = [0] * N
        if char in alfabeto:
            idx = alfabeto.index(char)
            linha[idx] = 1
        matriz.append(linha)
    
    return matriz

def encriptar(msg: str, P: np.ndarray, Q: np.ndarray) -> str:
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    msg = msg.upper()
    N = len(alfabeto)
    
    hot = one_hot(msg, alfabeto)
    
    codificada = []
    for i in range(len(hot)):
        linha = hot[i]
        
        perm_P = [0] * N
        for j in range(N):
            for k in range(N):
                perm_P[j] += linha[k] * P[k][j]
        
        for _ in range(i + 1):
            nova_linha = [0] * N
            for j in range(N):
                for k in range(N):
                    nova_linha[j] += perm_P[k] * Q[k][j]
            perm_P = nova_linha
        
        codificada.append(perm_P)
    
    encriptada = ""
    for linha in codificada:
        idx = linha.index(1) if 1 in linha else -1
        if idx != -1:
            encriptada += alfabeto[idx]
    
    return encriptada

def decriptar(msg_enc: str, P: np.ndarray, Q: np.ndarray) -> str:
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    msg_enc = msg_enc.upper()
    N = len(alfabeto)
    
    hot = one_hot(msg_enc, alfabeto)
    
    decodificada = []
    for i in range(len(hot)):
        linha = hot[i]
        
        for _ in range(i + 1):
            nova_linha = [0] * N
            for j in range(N):
                for k in range(N):
                    nova_linha[j] += linha[k] * Q[j][k]  
            linha = nova_linha
        
        perm_P_inversa = [0] * N
        for j in range(N):
            for k in range(N):
                perm_P_inversa[j] += linha[k] * P[j][k]  
        
        decodificada.append(perm_P_inversa)
    
    decriptada = ""
    for linha in decodificada:
        idx = linha.index(1) if 1 in linha else -1
        if idx != -1:
            decriptada += alfabeto[idx]
    
    return decriptada

def main():
    msg_original = input("Digite sua mensagem: ")
    P, Q = gerar_permutacoes(27)

    msg_enc = encriptar(msg_original, P, Q)
    print("Mensagem encriptada:", msg_enc)

    msg_dec = decriptar(msg_enc, P, Q)
    print("Mensagem decriptada:", msg_dec)

if __name__ == "__main__":
    main()
