# Sistema de Codificação e Decodificação de Mensagens

Este projeto usa matrizes de permutação e álgebra linear para codificar e decodificar mensagens de texto. A mensagem é transformada em uma matriz "one-hot" e passa por operações matriciais para ser cifrada e depois decifrada.

## Funcionalidades

### 1. `gerar_permutacoes(N)`

- Gera duas matrizes de permutação `P` e `Q` de tamanho \(N \times N\).
- Essas matrizes são usadas para cifrar e decifrar a mensagem.
  
### 2. `one_hot(mensagem, alfabeto)`

- Converte a mensagem de texto em uma matriz "one-hot", onde cada linha corresponde a um caractere e a coluna onde há um valor 1 indica o índice desse caractere no alfabeto.

### 3. `encriptar(msg, P, Q)`

- Cifra a mensagem usando duas matrizes de permutação `P` e `Q`.
- A mensagem é multiplicada por `P`, e depois passa por `Q` iterativamente.
- Retorna a mensagem cifrada.

### 4. `decriptar(msg_enc, P, Q)`

- Decifra a mensagem cifrada multiplicando-a pelas transpostas de `Q` e `P`.
- Reverte o processo de cifragem e restaura a mensagem original.


```python
msg_original = input("Digite sua mensagem: ")
P, Q = gerar_permutacoes(27)

msg_enc = encriptar(msg_original, P, Q)
print("Mensagem encriptada:", msg_enc)

msg_dec = decriptar(msg_enc, P, Q)
print("Mensagem decriptada:", msg_dec)
>>>>>>> 9547b9dfe7a34fcc98656ec27582977005b66aaf
