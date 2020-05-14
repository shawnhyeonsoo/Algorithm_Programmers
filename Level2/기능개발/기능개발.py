progresses = [93,30,55]
speeds = [1,30,5]


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