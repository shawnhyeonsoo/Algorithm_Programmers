[Level 2- 연습문제 - 124 나라의 숫자] </br>
출처: 프로그래머스 </br>
문제 링크: https://programmers.co.kr/learn/courses/30/lessons/12899 </br>

</br>
문제 설명:
</br>
</br>
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

1. 124 나라에는 자연수만 존재합니다.
2. 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.

예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

|10진법	|124 나라	|10진법	|124 나라|
|------|-------|------|-------|
|1	|1	|6	|14|
|2	|2	|7	|21|
|3	|4	|8	|22|
|4	|11	|9	|24|
|5	|12	|10	|41|

</br>

자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

</br>
</br>
제한 사항 </br>

* n은 500,000,000이하의 자연수 입니다.

</br>
</br>
솔루션: </br>

```python

def recursion(number,list):
    i = number%3
    if i == 0:
        list.append('4')
        j = (number-1)//3
        if j == 0:
            return list
        else:
            return recursion(j,list)

    else:
        list.append(str(i))
        j = number//3
        if j == 0:
            return list
        else:
            return recursion(j,list)

def solution(n):
    answer_list = recursion(n,[])[::-1]
    answer = "".join(answer_list)
    return answer
```

> 규칙을 찾는 것이 핵심인 문제인데, 3으로 나눈 나머지와 몫을 이용해 숫자를 변환해 푸는 과정을 담았다. 몫이 0이 될때까지 계속해서 3으로 나눠 매번 나머지를 기록해
  주었는데, 여기서 나머지가 0인 경우는 '4'로 저장했다. 그렇게 1의자리가 배열의 앞에서부터 저장되었기 때문에 모든 재귀가 끝나면 배열을 뒤집은 후, 문자열로 출력
  하도록 했다.
  
</br>
정확성: 70.0</br>
효율성: 30.0
합계: 100.0/100.0

