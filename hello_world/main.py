from hello_world.enigma import gerar_permutacoes, encriptar, decriptar

def main():
    msg_original = input("Digite sua mensagem: ")
    P, Q = gerar_permutacoes(27)  

    msg_enc = encriptar(msg_original, P, Q)
    print("Mensagem encriptada:", msg_enc)

    msg_dec = decriptar(msg_enc, P, Q)
    print("Mensagem decriptada:", msg_dec)

if __name__ == "__main__":
    main()