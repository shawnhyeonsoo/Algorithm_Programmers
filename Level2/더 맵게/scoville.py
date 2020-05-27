def solution(scoville,K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if (len(scoville) == 1) and scoville[0] < K:
            answer = -1
            break
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, (a + (2 * b)))
            answer += 1

    return answer