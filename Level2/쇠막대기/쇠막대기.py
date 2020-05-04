def solution(arrangement):
    test = arrangement.replace('()', 'f')
    A = []
    answer = 0
    for i in range(len(test)):
        if test[i] == '(':
            A.append(('(', i))
        elif test[i] == ')':
            B = test[int(A[-1][1]):i]
            answer += B.count('f') + 1
            A.pop()

    return answer