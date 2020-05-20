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