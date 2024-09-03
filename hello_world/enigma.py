import numpy as np

def para_one_hot(msg: str) -> np.array:
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    n = len(alfabeto)
    T = len(msg)
    M = np.zeros((n, T), dtype=int)
    
    for j, char in enumerate(msg):
        i = alfabeto.index(char)
        M[i, j] = 1
    
    return M

def para_string(M: np.array) -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    msg = ''
    for j in range(M.shape[1]):
        i = np.argmax(M[:, j])
        msg += alfabeto[i]
    
    return msg

def cifrar(msg: str, P: np.array) -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    n = len(alfabeto)
    T = len(msg)
    M = np.zeros((n, T), dtype=int)

    for j, char in enumerate(msg):
        i = alfabeto.index(char)
        M[i, j] = 1
    
    M_permutada = P @ M
    
    msg_cifrada = ''
    for j in range(M_permutada.shape[1]):
        i = np.argmax(M_permutada[:, j])
        msg_cifrada += alfabeto[i]
    
    return msg_cifrada

def de_cifrar(msg: str, P: np.array) -> str:
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    n = len(alfabeto)
    T = len(msg)
    M_cifrada = np.zeros((n, T), dtype=int)
    
    for j, char in enumerate(msg):
        i = alfabeto.index(char)
        M_cifrada[i, j] = 1
    
    M_original = P.T @ M_cifrada
    
    msg_original = ''
    for j in range(M_original.shape[1]):
        i = np.argmax(M_original[:, j])
        msg_original += alfabeto[i]
    
    return msg_original

def enigma(msg: str, P: np.array, E: np.array) -> str:
    msg_cifrada_P = cifrar(msg, P)
    msg_cifrada_E = cifrar(msg_cifrada_P, E)
    
    msg_final = cifrar(msg_cifrada_E, P)
    
    return msg_final

def de_enigma(msg: str, P: np.array, E: np.array) -> str:
    msg_decifrada_P1 = de_cifrar(msg, P)
    msg_decifrada_E = de_cifrar(msg_decifrada_P1, E)
    
    msg_original = de_cifrar(msg_decifrada_E, P)
    
    return msg_original

