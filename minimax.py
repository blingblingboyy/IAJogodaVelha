from jogo_da_velha import blank, token, verificaWin

def movimentoIA(board, jogador):
    possibilidades = getPosicoes(board)
    melhorVal = None
    melhorMov = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = blank
        if melhorVal is None:
            melhorVal = valor
            melhorMov = possibilidade
        elif jogador == 0:
            if valor > melhorVal:
                melhorVal = valor
                melhorMov = possibilidade
        elif jogador == 1:
            if valor < melhorVal:
                melhorVal = valor
                melhorMov = possibilidade
    print(f"Chance de vitória: {melhorVal * 100}%")
    return melhorMov[0], melhorMov[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == blank):
                posicoes.append([i, j])

    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}
def minimax(board, jogador):
    ganhador = verificaWin(board)
    if ganhador:
        return score[ganhador]

    jogador = (jogador + 1) % 2

    melhorVal = None
    melhorMov = None
    possibilidades = getPosicoes(board)
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = token[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = blank

        if melhorVal is None:
            melhorVal = valor
        elif jogador == 0:
            if (valor > melhorVal):
                melhorVal = valor
        elif jogador == 1:
            if valor < melhorVal:
                melhorVal = valor

    return melhorVal
