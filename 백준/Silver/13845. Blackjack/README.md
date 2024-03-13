# [Silver IV] Blackjack - 13845 

[문제 링크](https://www.acmicpc.net/problem/13845) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 문제 설명


<p>Brian Jones is an undergraduate student at Advanced College of Metropolitan. Recently he was given an assignment in his class of Computer Science to write a program that plays a dealer of blackjack.</p>

<p>Blackjack is a game played with one or more decks of playing cards. The objective of each player is to have the score of the hand close to 21 without going over 21. The score is the total points of the cards in the hand. Cards from 2 to 10 are worth their face value. Face cards (jack, queen and king) are worth 10 points. An ace counts as 11 or 1 such a way the score gets closer to but does not exceed 21. A hand of more than 21 points is called bust, which makes a player automatically lose. A hand of 21 points with exactly two cards, that is, a pair of an ace and a ten-point card (a face card or a ten) is called a blackjack and treated as a special hand.</p>

<p>The game is played as follows. The dealer first deals two cards each to all players and the dealer himself. In case the dealer gets a blackjack, the dealer wins and the game ends immediately. In other cases, players that have blackjacks win automatically. The remaining players make their turns one by one. Each player decides to take another card (hit) or to stop taking (stand) in his turn. He may repeatedly hit until he chooses to stand or he busts, in which case his turn is over and the next player begins his play. After all players finish their plays, the dealer plays according to the following rules:</p>

<ul>
	<li>Hits if the score of the hand is 16 or less.</li>
	<li>Also hits if the score of the hand is 17 and one of aces is counted as 11.</li>
	<li>Stands otherwise.</li>
</ul>

<p>Players that have unbusted hands of higher points than that of the dealer win. All players that do not bust win in case the dealer busts. It does not matter, however, whether players win or lose, since the subject of the assignment is just to simulate a dealer.</p>

<p>By the way, Brian is not good at programming, thus the assignment is a very hard task for him. So he calls you for help, as you are a good programmer.</p>

<p>Your task is to write a program that counts the score of the dealer’s hand after his play for each given sequence of cards.</p>

### 입력 

<p>The first line of the input contains a single positive integer N, which represents the number of test cases. Then N test cases follow.</p>

<p>Each case consists of two lines. The first line contains two characters, which indicate the cards in the dealer’s initial hand. The second line contains eight characters, which indicate the top eight cards in the pile after all players finish their plays.</p>

<p>A character that represents a card is one of A, 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q and K, where A is an ace, T a ten, J a jack, Q a queen and K a king.</p>

<p>Characters in a line are delimited by a single space.</p>

<p>The same cards may appear up to four times in one test case. Note that, under this condition, the dealer never needs to hit more than eight times as long as he or she plays according to the rule described above.</p>

### 출력 

<p>For each case, print on a line “blackjack” if the dealer has a blackjack; “bust” if the dealer busts; the score of the dealer’s hand otherwise.</p>
