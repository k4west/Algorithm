import sys

# flag: A를 11로 계산한 경우 True
def scores(cards, score=0, flag=False):
    for card in cards:
        # 점수 더하기
        if card.isdigit(): score += int(card)
        elif card in "TJQK": score += 10
        elif score + 11 <= 21:
            score += 11
            flag = True
        else: score += 1

        # A를 11로 해서 bust가 되는 경우에
        # A를 1로 취급한 경우로 재계산
        if score > 21 and flag:
            score -= 10
            flag = False

        # 점수가 17이고 A를 11로 센 경우 > Hit
        if score == 17 and flag: continue

        # 그 외에는 16 이하인 경우 Hit > 초과는 종료
        elif score > 16: break
    return score, flag


def plays(init, cards):
    score, flag = scores(init.split())

    # 처음에 A(11) + 10 => 21 => blackjack 반환
    if score == 21: return "blackjack"
    
    # Hit 실행 조건 > Hit
    if score <= 16 or (score == 17 and flag): score, _ = scores(cards.split(), score, flag)
    
    # 21 초과는 bust 이하는 점수 반환
    if score > 21: return "bust"
    return score


def main():
    input = sys.stdin.readline
    ans = []
    N = int(input())
    for _ in range(N): ans.append(plays(input().rstrip(), input().rstrip()))

    # 줄 나눔으로 구분해서 출력
    print("\n".join(map(str, ans)))

main()
