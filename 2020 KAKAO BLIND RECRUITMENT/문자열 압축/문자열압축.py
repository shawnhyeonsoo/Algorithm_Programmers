def solution(test):

    C = []
    answer_length = None

    for z in range(1,len(test)+1):
        C.append(z)

    for _ in C:
        A = []
        B = []
        answer = ''
        for i in range(len(test)):
            if i%_ == 0:
                B.append(i)
            else:
                pass

        for j in B:
            if j == len(test):
                A.append()
            else:
                A.append(test[j:j+_])

        count = 1
        for k in range(len(A)):
            if k == len(A)-1:
                if count == 1:
                    answer += A[k]
                else:
                    answer += str(count) + A[k]
            elif A[k]==A[k+1]:
                count += 1
            elif A[k] != A[k+1]:
                if count == 1:
                    answer += A[k]
                else:
                    answer += str(count) + A[k]
                    count = 1
        if (answer_length == None) or (len(answer) < answer_length):
            answer_length = len(answer)
        else:
            pass

    return answer_length