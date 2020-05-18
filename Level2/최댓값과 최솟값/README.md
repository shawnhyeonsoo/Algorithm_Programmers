[Level 2- 연습문제 - 최댓값과 최솟값] </br>
출처: 프로그래머스 </br>
문제 링크: <https://programmers.co.kr/learn/courses/30/lessons/12939> </br>

</br>
문제 설명:
</br>
</br>
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.
</br>

</br>
</br>
제한 사항 </br>

* s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

</br>
</br>
입출력 예:</br>

|s	|return|
|---|-------|
|"1 2 3 4"	|"1 4"|
|"-1 -2 -3 -4"|"-4 -1"|
|"-1 -1"|	"-1 -1"|

</br>
솔루션: </br>

```python

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

```

> 문자열로 주어진 s에서 최댓값과 최솟값을 추출하는 문제인데, 정렬로도 구현할 수 있지만, 마침 heap 관련 알고리즘 문제를 풀었던 터라 연습해보고자 heap을 사용해서
  구현해보았다. heapq 라이브러리를 불러와 heap 관련 함수들을 사용할 수 있도록 했는데, 여기서 heapq 함수들은 Min Heap 을 구하는 것에 맞춰져 있기 때문에
  Max Heap 을 구현하기 위해선 push를 하는 과정에서 음수로 변환 후 넣어주었다. 그렇게 Min Heap 과 Max Heap 두 가지 배열을 만들어 각각에서 배열 제일
  앞에 있는 최댓값과 최솟값을 추출해 answer에 추가해주었다. 
  
</br>
정확성: 100.0</br>
합계: 100.0/100.0

