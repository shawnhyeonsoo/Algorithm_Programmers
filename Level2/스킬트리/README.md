[Level 2- Summer/Winter Coding(~2018) - 스킬트리] </br>
출처: 프로그래머스 </br>
문제 링크: <https://programmers.co.kr/learn/courses/30/lessons/49993> </br>

</br>
문제 설명:
</br>
</br>
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

</br>
</br>
제한 사항 </br>

- 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
- 스킬 순서와 스킬트리는 문자열로 표기합니다.
- 예를 들어, C → B → D 라면 CBD로 표기합니다
- 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
- skill_trees는 길이 1 이상 20 이하인 배열입니다.
- skill_trees의 원소는 스킬을 나타내는 문자열입니다.
  - skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

</br>
</br>
입출력 예: </br>
</br>
 
|skill	|skill_trees	|return|
|------|-----------|---------|
|"CBD"	|["BACDE", "CBADF", "AECB", "BDA"]	|2|


솔루션: </br>

```python

def solution(skill,user_list):
    B = []
    answer = 0
    for j in range(len(skill)):  #선행스킬 정보 담아주기
        if j > 0:
            B.append((skill[j],skill[j-1]))
        else:
            B.append((skill[j],0))

    for skill_tree in user_list:
        A = []
        for k in skill_tree:
            if k in skill:
                indexer = skill.index(k)
                if (B[indexer][1] == 0) or (B[indexer][1] in A):
                    A.append(k)
                else:
                    pass
            else:
                A.append(k)


        if len(A) == len(skill_tree):
            answer += 1

    return answer
```

> 처음 문제를 접했을 때, 선행정보를 반영하려면 Tree 나 Trie를 이용해야할까 하다가 우선 문제에서 주어진 조건을 그대로 반영을 하여 코딩을 해봤는데, 우선 선행 스킬
  문자열을 받아와 새로운 배열에다가 각 문자의 선행정보를 담은 Tuple을 저장했다. 그 후, 유저가 만든 스킬트리의 배열에서 문자열을 하나씩 불러와 한 문자씩, 선행스킬
  정보가 있는지, 있는데 선행 스킬이 없는 스킬이라면 A라는 배열에 저장, 혹은 있는데 선행스킬이 A라는 학습된 스킬의 배열에 있는지 등을 바탕으로 알고리즘을 설계했다. 
  효율성 면에서 평균적으로 0.05ms, 10.8MB 으로 나쁘지 않은 효율을 보였는데, 다른 방법이 있는지 생각해봐야 할 것 같다. 
  
</br>
정확성: 100.0</br>
합계: 100.0/100.0

