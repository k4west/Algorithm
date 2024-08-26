# [Silver V] Stacking Cups - 14769 

[문제 링크](https://www.acmicpc.net/problem/14769) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

자료 구조, 정렬, 문자열

### 제출 일자

2024년 8월 26일 13:43:40

### 문제 설명

<p>You are programming a cup stacking module for your robot. This robot is equiped with several sensors that can accurately determine the radius and color of a cup. The problem is that there is a glitch in the robot’s core routine that processess sensor inputs so the radius is doubled, if the result of the color sensor arrives to the routine after the radius.</p>

<p>For instance, for a red cup with a radius of 5 units, your module will receive either “red 5” or “10 red” message.</p>

<p>Given a list of messages from the core routine, each describing a different cup, can you put the cups in order of the smallest to the largest?</p>

### 입력 

 <p>The first line of the input file contains an integer N, the number of cups (1 ≤ N ≤ 20). Next N lines will contain two tokens each, either as “color radius” or “diameter color”. The radius of a cup R will be a positive integer less than 1000. The color of a cup C will be a non-empty string of lower case English letters of length at most 20. All cups will be different in both size and color.</p>

### 출력 

 <p>Output colors of cups, one color per line, in order of increasing radius.</p>

