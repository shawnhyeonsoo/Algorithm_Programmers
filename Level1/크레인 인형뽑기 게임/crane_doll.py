def solution(board,moves):
    basket = []
    count = 0
    for _ in moves:
        A = []
        for i in board:
            if i[_-1] == 0:
                pass
            else:
                A.append(i)

        if len(A) == 0:
            pass
        else:
            if len(basket) == 0:
                basket.append(A[0][_-1])
                board[board.index(A[0])][_-1] = 0
            else:
                if basket[-1] == A[0][_-1]:
                    basket.pop()
                    board[board.index(A[0])][_ - 1] = 0
                    count += 2
                else:
                    basket.append(A[0][_ - 1])
                    board[board.index(A[0])][_ - 1] = 0

    return count