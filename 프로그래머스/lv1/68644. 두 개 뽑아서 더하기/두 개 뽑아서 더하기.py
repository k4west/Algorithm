def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j, k in enumerate(numbers):
            if i == j:
                continue
            answer.add(numbers[i]+k)
    return sorted(answer)