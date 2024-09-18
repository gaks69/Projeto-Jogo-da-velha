def inicializar_tabuleiro():
    #Esta Função ira Inicializar o tabuleiro do jogo da velha.
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro(tabuleiro):
    #Esta Função ira Imprimir o tabuleiro do jogo da velha.
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
     #Esta função ira Verificar se o jogador venceu o jogo."""
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for col in range(3):
        if all(tabuleiro[row][col] == jogador for row in range(3)):
            return True

    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    #Esta função ira Verificar se o jogo terminou em empate.
    return all(tabuleiro[row][col] != " " for row in range(3) for col in range(3))

def jogada(tabuleiro, jogador, linha, coluna):
    #Esta função ira Realizar uma jogada no tabuleiro.
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    return False

def jogo_da_velha():
     #Esta função ira  executar o jogo da velha(Função principal).
    tabuleiro = inicializar_tabuleiro()
    jogadores = ["X", "O"]
    turno = 0

    while True:
        jogador_atual = jogadores[turno % 2]
        print(f"É a vez do jogador {jogador_atual}.")
        imprimir_tabuleiro(tabuleiro)

        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
            print("Linha ou coluna inválida. Tente novamente.")
            continue

        if jogada(tabuleiro, jogador_atual, linha, coluna):
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
                break
            elif verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo terminou em empate!")
                break
            turno += 1
        else:
            print("A célula escolhida já está ocupada. Tente novamente.")

if __name__ == "__main__":
    jogo_da_velha()
