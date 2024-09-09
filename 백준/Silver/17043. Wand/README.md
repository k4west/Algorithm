# [Silver I] Wand - 17043 

[문제 링크](https://www.acmicpc.net/problem/17043) 

### 성능 요약

메모리: 68588 KB, 시간: 148 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2024년 9월 9일 11:31:32

### 문제 설명

<p>Kile really liked Nikola's task with wizards and a wand (see task Elder) so he decided to make his own version. He imagined that instead of the 26 wizards there are N of them labeled with integers from 1 to N and that M duels must be held among the wizards. It is possible that a duel between the same pair of wizards will be held multiple times.</p>

<p>As in Nikola's task, if before the match the wand belonged to the loser, after the match the wand will be assigned to the winner.</p>

<p>If we know in advance for each duel which pair of wizards will fight, as well as which of them will win and if we can choose the order in which the duels will be held, then Kile wants to know in whose hands the wand can end up in after all M duels.</p>

<p>In the beginning, the wand belongs to the wizard with the label 1.</p>

### 입력 

 <p>The first line contains two integers N and M (1 ≤ N, M ≤ 100 000).</p>

<p>In the following M lines there are two numbers X<sub>i</sub> and Y<sub>i</sub> (1 ≤ X<sub>i</sub>, Y<sub>i</sub> ≤ N, X<sub>i</sub> ≠ Y<sub>i</sub>). The wizard Xi will win the fight against wizard Y<sub>i</sub>.</p>

### 출력 

 <p>Print N characters in the first and only line. The character at the k<sup>th</sup> position should be '1' if the wizard labeled with k can rule over the wand after all M duels and '0' otherwise.</p>

