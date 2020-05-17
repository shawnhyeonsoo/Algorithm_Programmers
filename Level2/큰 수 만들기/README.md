[Level 2- 연습문제 - 큰 수 만들기] </br>
출처: 프로그래머스 </br>
문제 링크: <https://programmers.co.kr/learn/courses/30/lessons/42883> </br>

</br>
문제 설명:
</br>
</br>
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

</br>
</br>
제한 사항 </br>

* number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
* k는 1 이상 number의 자릿수 미만인 자연수입니다.

</br>
</br>

입출력 예:

|number	|k|return|
|-------|--|------|
|1924	|2	|94|
|1231234	|3	|3234|
|4177252841	|4	|775841|

</br>
1번 Trial: </br>

```python

def delete(array):
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            array.pop(i)
            break
    return array


def find_out(array):
    A = []
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            A.append(i)
            break
    if len(A) == 0:
        return False
    else:
        return True


def solution(number,k):
    test = []
    if len(set(number)) == 1:
        test = [number[0]*(len(number)-k)]
    else:
        for j in range(len(number)):
            test.append(number[j])
        for _ in range(k):
            if len(set(number)) == 1:
                test.pop()
            elif find_out(test):
                delete(test)
            else:
                test.pop()
    answer = str("".join(test))
    return answer
```

</br>
정확성: 83.3</br>
합계: 83.3/100.0

> 개인적으로 되게 어렵게 푼 문제이므로 한 번의 시도로 끝나지 않았다. 위의 코드와 같이 앞의 수가 바로 뒤의 수보다 작으면 빼주는 식으로 코드를 짰는데, 테스트 케이스
  8번과 10번에서 계속 시간 초과로 실패로 채점되었다. 10번 테스트 케이스가 매우 큰 99999....99999 와 같은 수가 입력 되었을 때로 생각하면 된다고 다른 분들이
  설명해주신 것을 보고 그거에 맞게 나름 코드를 짜봤으나 시간 복잡도 면에서 계속 걸리는 것이었다. 다른 분들이 올리신 코드를 찾아보며 내가 생각한 방법과 비슷한 
  알고리즘을 찾아봤지만, 비슷한 방법은 찾기가 쉽지 않았다. 결국에 비슷한 방법을 찾아 참고하여 두 번째 시도를 해봤다. 
  
</br>
</br>
2번 Trial (solution):
</br>

```python
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
 ```
    
</br>
정확성: 100.0</br>
합계: 100.0/100.0


