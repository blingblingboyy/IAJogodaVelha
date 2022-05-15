from jogo_da_velha import *
from minimax import movimentoIA
jogador = 0  # Jogador 1
board = criarBoard()
ganhador = verificaWin(board)
while not ganhador:
    printBoard(board)
    print("=" * 15)
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        i = getInputValido("Digite a linha ")
        j = getInputValido("Digite a coluna ")
    if verificaMov(board, i, j,):
        fazMov(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("Movimento inválido!")
    ganhador = verificaWin(board)

print("=" * 15)
printBoard(board)
print(f"GANHADOR = {ganhador}")
print("=" * 15)