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