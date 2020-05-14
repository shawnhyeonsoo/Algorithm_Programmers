[Level 2- 연습문제 - 기능개발] </br>
출처: 프로그래머스 </br>
문제 링크: <https://programmers.co.kr/learn/courses/30/lessons/42586> </br>

</br>
문제 설명:
</br>
</br>
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.</br>
</br>

</br>
</br>
제한 사항 </br>

* 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
* 작업 진도는 100 미만의 자연수입니다.
* 작업 속도는 100 이하의 자연수입니다.
* 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.</br>

</br>
</br>
솔루션: </br>

```python

def solution(progresses,speeds):
    days = []

    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] != 0:
            duration = ((100-progresses[i])//speeds[i]) +1
        else:
            duration = (100-progresses[i])//speeds[i]

        days.append(duration)

    A = []
    B = []
    count = 1
    for j in range(len(days)):
        if len(A) == 0:
            A.append(days[j])
        elif days[j] > A[-1]:
            B.append(count)
            A.append(days[j])
            count = 1
        elif days[j] <= A[-1]:
            count += 1

        if j == len(days) -1:
            B.append(count)
    return B
```

> 처음 문제를 접했을 때, while문을 쓸까 고민을 많이 했지만, for문을 통해 문제를 풀어보고자 한번 시도해봤다. 우선 각 기능마다 앞으로 완성까지 걸리는 시간을 
  duration이라는 변수에 저장해주었으며, 그 다음에 days라는 배열에다가 정보를 저장했다. 그 후, 각각 걸리는 기간을 바탕으로 앞선 기능이 완성여부에 따라
  조건을 걸어 새로운 배열에다가 저장했다. 
  
</br>
정확성: 100.0</br>
합계: 100.0/100.0

