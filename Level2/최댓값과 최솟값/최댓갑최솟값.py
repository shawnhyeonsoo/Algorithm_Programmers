import heapq
def solution(s):
    t = list(map(int,s.split()))
    maxheap= []
    minheap = []
    answer_list= []

    for j in t:
        heapq.heappush(maxheap, -j)
        heapq.heappush(minheap, j)

    answer_list.append(str(minheap[0]))
    answer_list.append(str(-maxheap[0]))

    answer = " ".join(answer_list)
    return answer
