def solution(numbers,target):
    #array1 = [1,2,3,4,5]
    B = [0]

    for i in numbers:
        array = []
        for j in B:
            array.append(j+i)
            array.append(j-i)
        B = array
    answer = B.count(target)
    return answer
