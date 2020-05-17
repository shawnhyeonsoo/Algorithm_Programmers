def solution(number, k):
    test = [number[0]]
    for _ in number[1:]:
        while (len(test) > 0) and (test[-1] < _) and (k > 0):
            k -= 1
            test.pop()
        test.append(_)
    if k != 0:
        test = test[:-k]
    return ''.join(test)