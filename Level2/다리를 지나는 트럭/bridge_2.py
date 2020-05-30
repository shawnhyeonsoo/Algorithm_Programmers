def solution(bridge_length,weight,truck_weights):
    from collections import deque
    test = deque(truck_weights)
    time = 0
    bridge = [0] * bridge_length
    while bridge:
        time += 1
        bridge.pop(0)
        if test:
            if sum(bridge) + test[0] <= weight:
                bridge.append(test.popleft())
            else:
                bridge.append(0)
    return time

