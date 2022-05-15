blank = " "
token = ["X", "O"]


def criarBoard():
    board = [
        [blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if (i < 2):
            print("-" * 6)


def getInputValido(msg):
    try:
        n = int(input(msg))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("O número precisa estar entre 1 e 3")
            return getInputValido(msg)
    except:
        print("Número inválido")
        return getInputValido(msg)


def verificaMov(board, i, j):
    if board[i][j] == blank:
        return True
    else:
        return False


def fazMov(board, i, j, jogador):
    board[i][j] = token[jogador]


def verificaWin(board):
    # Linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != blank:
            return board[i][0]
    # Colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != blank:
            return board[0][i]
    # Diagonal principal
    for i in range(3):
        if board[0][0] != blank and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        # Diagonal principal
        for i in range(3):
            if board[0][2] != blank and board[0][2] == board[1][1] == board[2][0]:
                return board[0][2]
    for i in range(3):
        for j in range(3):
            if board[i][j] == blank:
                return False

    return "EMPATE"
