def solution(heights):

    A = []
    for _ in range(len(heights)):
        A.append(0)

    test = heights[::-1] #heights뒤집은거
    #해당 숫자보다 크면 해당 주소 +=1 해주고 break


    for i in range(len(test)):1
        if i == len(test)-1:
            pass
        else:
            test1 = test[i+1:]
            for j in range(len(test1)):
                if test1[j] > test[i]:
                    if A[i] != 0:
                        pass
                    else:   
                        A[i] = len(heights) - (i+j+1)
                else:
                    pass

    A = A[::-1]
    return A