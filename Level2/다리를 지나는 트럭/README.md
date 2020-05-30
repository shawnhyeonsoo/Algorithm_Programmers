[Level 2- 스택/큐 - 다리를 지나는 트럭] </br>
출처: 프로그래머스 </br>
문제 링크: <https://programmers.co.kr/learn/courses/30/lessons/42583> </br>

</br>
문제 설명:
</br>
</br>
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.

※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.</br>


|경과 시간	|다리를 지난 트럭|다리를 건너는 트럭|대기 트럭|
|--------|--------|--------|---------|
|0	|[]	|[]	|[7,4,5,6]|
|1~2	|[]	|[7]	|[4,5,6]|
|3	|[7]	|[4]	|[5,6]|
|4	|[7]	|[4,5]	|[6]|
|5	|[7,4]	|[5]	|[6]|
|6~7	|[7,4,5]	|[6]	|[]|
|8	|[7,4,5,6]	|[]	|[]|


따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

</br>
</br>
제한 사항 </br>

* bridge_length는 1 이상 10,000 이하입니다.
* weight는 1 이상 10,000 이하입니다.
* truck_weights의 길이는 1 이상 10,000 이하입니다.
* 모든 트럭의 무게는 1 이상 weight 이하입니다.

</br>
</br>
솔루션: </br>

```python

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    n = len(truck_weights)
    passing_weight = [0] * n
    passed = []
    passing = []

    i = 0
    j = -1
    while len(passed) < n:
        if len(truck_weights) > 0 and sum(passing) + truck_weights[-1] <= weight:
            passing.append(truck_weights.pop())
            j += 1
        passing_weight[:j + 1] = [passing_weight[z] + 1 for z in range(j + 1)]

        if passing_weight[i] == bridge_length:
            passed.append(passing[0])
            passing = passing[1:]
            i += 1

    return passing_weight[0] + 1
```

> 스택과 큐에 관한 문제로 스택에서 pop 해주며 문제 그대로 구현을 해보았다. 수학적 방법을 통해 보다 더 최적화시킬 수 없을까 생각을 해봤는데, 아직 성공적으로
  구현하진 못했다. 위의 코드는 주어진 테스트 케이스에 대해서 6691ms까지 나와서 이보다 더 효율적인 방법을 찾아봐야 할 것 같다.


```python
def solution(bridge_length,weight,truck_weights):
    from collections import deque
    test = deque(truck_weights)
    time = 0
    bridge = [0] * bridge_length
    while bridge:
        time += 1
        bridge.pop(0)
        if test:
            if sum(bridge) + test[0] <= weight:
                bridge.append(test.popleft())
            else:
                bridge.append(0)
    return time

```

> deque를 사용하여 시간을 줄여봤는데, 코드는 우선 더 간결해짐을 볼 수 있었다. 우선 길이 만큼 0을 가진 bridge라는 다리의 상황을 배열로 구현하여 시간이 지날때마다   제일 앞의 0 혹은 트럭을 pop 시키면서 while문을 돌리는것인데, 전 코드보다 대부분의 상황에서 효율적임을 볼 수 있었다. 


</br>
정확성: 100.0</br>
합계: 100.0/100.0

