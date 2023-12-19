from collections import deque
def solution(queue1, queue2):
    # 초기 상태에서 각 큐의 합 구하기
    # 매번 큐의 합을 구하지 않고 이 값을 변화를 줘서 큐의 합을 구함
    # 이 방법으로 시간 내에 풀이 가능
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    goal = sum1 + sum2
    
    # 두 큐 합 같게 만들려면 goal이 짝수여야 함
    if goal % 2:
        return -1
    
    goal //= 2
    count = 0
    n = len(queue1) + len(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while goal != sum1: # 한 큐의 합이 두 큐의 총합의 절반이 될때까지 반복
        # 모든 원소가 이동할 때까지 한 번도 조건들 달성하지 못하면 앞으로도 불가능함
        if count >= n:
            return -1  # -1 반환 후 종료

        # 한 큐의 합이 목표 값보다 크면 그 큐의 앞 원소를 다른 큐로 이동
        # 합은 이동한 원소에 맞게 값을 업데이트
        while sum1 > goal:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            count += 1
        
        # 한 큐의 합이 목표보다 크면 다른 큐의 앞 원소를 가져오기
        while sum1 < goal:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            count += 1

    # 합이 목표를 도달해서 while문이 종료됐음 -> conut 반환
    return count