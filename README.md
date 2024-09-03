# Sistema de Codificação e Decodificação com Álgebra Linear

## Visão Geral

Este projeto demonstra a aplicação de álgebra linear para codificação e decodificação de mensagens. A mensagem de texto é transformada em uma matriz "one-hot", que é manipulada através de operações matriciais para cifrar e decifrar o texto.

## Funcionalidades

### 1. Transformação de Texto para Matriz One-Hot (`para_one_hot`)

A função `para_one_hot` converte uma mensagem de texto em uma matriz "one-hot". Para cada caractere da mensagem, é gerada uma coluna na matriz, onde a posição correspondente ao caractere no alfabeto recebe o valor 1, e todas as outras posições recebem o valor 0.

**Exemplo:**

Dada a mensagem "ab" e considerando um alfabeto simplificado com três caracteres ("a", "b", "c"), a matriz "one-hot" correspondente seria:

$$
M = \begin{bmatrix}
1 & 0 \\
0 & 1 \\
0 & 0
\end{bmatrix}
$$

### 2. Conversão de Matriz para String (`para_string`)

A função `para_string` reverte a matriz "one-hot" de volta para a string original. Ela identifica a posição do valor 1 em cada coluna da matriz para determinar o caractere correspondente.

**Exemplo:**

Para a matriz acima:

$$
\text{Mensagem original: "ab"}
$$

### 3. Cifragem de Mensagem (`cifrar`)

A função `cifrar` aplica uma permutação à matriz "one-hot", multiplicando a matriz por uma matriz de permutação `P`. Isso embaralha as linhas da matriz, resultando em uma nova sequência de caracteres.

**Exemplo:**

Se `P` for:

$$
P = \begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

A matriz cifrada \( M' \) será:

$$
M' = P \times M = \begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix} \times \begin{bmatrix}
1 & 0 \\
0 & 1 \\
0 & 0
\end{bmatrix} = \begin{bmatrix}
0 & 1 \\
1 & 0 \\
0 & 0
\end{bmatrix}
$$

A mensagem cifrada seria "ba".

### 4. Decifragem de Mensagem (`de_cifrar`)

Para decifrar a mensagem, multiplica-se a matriz cifrada pela transposta da matriz de permutação \( P^T \), revertendo o processo de cifragem.

**Exemplo:**

Multiplicando a matriz cifrada \( M' \) pela transposta de \( P \):

$$
M = P^T \times M' = \begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}^T \times \begin{bmatrix}
0 & 1 \\
1 & 0 \\
0 & 0
\end{bmatrix} = \begin{bmatrix}
1 & 0 \\
0 & 1 \\
0 & 0
\end{bmatrix}
$$

A mensagem decifrada retorna para "ab".

### 5. Sistema Enigma Simples (`enigma`)

A função `enigma` utiliza duas matrizes de permutação `P` e `E` para aplicar uma cifragem dupla à mensagem. O processo de cifragem é realizado em três etapas:

1. Cifrar a mensagem com `P`.
2. Cifrar o resultado com `E`.
3. Cifrar o resultado novamente com `P`.

**Exemplo:**

Se `E` for:

$$
E = \begin{bmatrix}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
$$

A mensagem cifrada final será obtida por:

$$
M'' = P \times (E \times (P \times M))
$$

### 6. Decifragem Enigma (`de_enigma`)

A função `de_enigma` reverte o processo de cifragem, multiplicando a matriz cifrada sucessivamente pelas transpostas de `P` e `E`.

**Exemplo:**

$$
M = P^T \times (E^T \times (P^T \times M''))
$$

## Demonstração (`demo`)

A função `demo` é um exemplo interativo que mostra o processo completo de codificação e decodificação de uma mensagem. Ela permite ao usuário ver como a mensagem é convertida em uma matriz, cifrada, e depois decifrada.

## 
