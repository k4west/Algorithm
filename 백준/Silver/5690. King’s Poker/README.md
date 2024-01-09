# [Silver V] King’s Poker - 5690 

[문제 링크](https://www.acmicpc.net/problem/5690) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

많은 조건 분기

### 제출 일자

2024년 1월 9일 10:26:43

### 문제 설명

<p>Poker is one of the most widely played card games, and King’s Poker is one of its variations. The game is played with a normal deck of 52 cards. Each card has one of 4 suits and one of 13 ranks. However, in King’s Poker card suits are not relevant, while ranks are Ace (rank 1), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack (rank 11), Queen (rank 12) and King (rank 13). The name of the game comes from the fact that in King’s Poker, the King is the highest ranked card. But this is not the only difference between regular Poker and King’s Poker. Players of King’s Poker are dealt a hand of just three cards. There are three types of hands:</p>

<ul>
	<li>A set, made of three cards of the same rank.</li>
	<li>A pair, which contains two cards of the same rank, with the other card unmatched.</li>
	<li>A no-pair, where no two cards have the same rank. Hands are ranked using the following rules:</li>
	<li>Any set defeats any pair and any no-pair.</li>
	<li>Any pair defeats any no-pair.</li>
	<li>A set formed with higher ranked cards defeats any set formed with lower ranked cards.</li>
	<li>If the matched cards of two pairs have different ranks, then the pair with the higher ranked matched cards defeats the pair with the lower ranked matched cards.</li>
	<li>If the matched cards of two pairs have the same rank, then the unmatched card of both hands are compared; the pair with the higher ranked unmatched card defeats the pair with the lower ranked unmatched card, unless both unmatched cards have the same rank, in which case there is a tie.</li>
</ul>

<p>A new software house wants to offer King’s Poker games in its on-line playing site, and needs a piece of software that, given a hand of King’s Poker, determines the set or pair with the lowest rank that beats the given hand. Can you code it?</p>

### 입력 

 <p>Each test case is described using a single line. The line contains three integers A, B, and C representing the ranks of the cards dealt in a hand (1 ≤ A, B, C ≤ 13).</p>

<p>The last test case is followed by a line containing three zeros.</p>

### 출력 

 <p>For each test case output a single line. If there exists a set or a pair that beats the given hand, write the lowest ranked such a hand. The beating hand must be written by specifying the ranks of their cards, in non-decreasing order. If no set or pair beats the given hand, write the character ‘*’ (asterisk).</p>

