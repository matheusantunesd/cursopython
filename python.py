comando = 2
match comando:
    case 1:
        print ("Iniciando novo jogo...")
    case 2:
        print("Carregando jogo salvo...")
    case 3:
        print("Abrindo configurações")
    case _:
        print("Comando invalido! Tente novamente novamente.")