# [Silver V] Treasure Hunt - 15437 

[문제 링크](https://www.acmicpc.net/problem/15437) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 9월 11일 13:22:17

### 문제 설명

<p>Jill has created a new smartphone game that leads players to find a treasure. The app uses the phone's GPS to determine the player's location. The app then tells the player the direction in which to go on a route to find the treasure. When the player reaches some specific location, the app rewards the player with a (virtual) treasure.</p>

<p>Can you help the player determine how long it will take to find the treasure?</p>

### 입력 

 <p>The first line of input contains two integers <em>R</em> and <em>C</em>, each between 1 and 200, inclusive. These integers define the number of rows and columns in the playing area, respectively. The next <em>R</em> lines of input describe the playing area. Each line contains exactly <em>C</em> letters, and each letter defines the action to take in each location in the playing area. There are five possible letters: <code>N</code> indicates a move to the previous row, <code>S</code> indicates a move to the next row, <code>W</code> indicates a move to the previous column, <code>E</code>indicates a move to the next column, and <code>T</code> indicates the location of the treasure. Exactly one location contains the treasure.</p>

### 출력 

 <p>The player begins playing at the location in the first column of the first row. The player follows the directions at each location. If the player eventually reaches the treasure by following the directions, output a line containing an integer, the number of moves required to reach the treasure. If the directions cause the player to leave the playing area, output a line containing the word <code>Out</code>. If the directions cause the player to stay in the playing area but never reach the treasure, output a line containing the word <code>Lost</code>.</p>

