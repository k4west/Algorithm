from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = w_on_b = 0
    bridge = deque([0] * bridge_length)
    for truck in truck_weights:
        w_on_b -= bridge.pop()
        answer += 1
        w_on_b += truck
        while w_on_b > weight:
            bridge.appendleft(0)
            w_on_b -= bridge.pop()
            answer += 1
        bridge.appendleft(truck)
    return bridge_length + answer