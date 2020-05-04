def solution(n):
    count = 1
    answer = 0
    number = 1
    prev = 0
    while count < n:
        answer = (number + prev)
        prev = number
        number = answer
        count += 1

    return (answer % 1234567)