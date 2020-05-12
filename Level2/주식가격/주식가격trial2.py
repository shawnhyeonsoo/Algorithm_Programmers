def solution(prices):
    A = [0* m for m in range(len(prices))]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j] >= prices[i]:
                A[i] += 1
            else:
                A[i] +=1
                break
    return A