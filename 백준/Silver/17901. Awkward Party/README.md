# [Silver III] Awkward Party - 17901 

[문제 링크](https://www.acmicpc.net/problem/17901) 

### 성능 요약

메모리: 47088 KB, 시간: 76 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

### 제출 일자

2024년 8월 13일 13:54:40

### 문제 설명

<p>Martin has invited everyone he knows to celebrate his 535th birthday, and a whopping n people from all over the world have accepted the invitation.</p>

<p>When deciding the seating arrangement, Martin’s mother Margarethe have decided that all the guests should be seated with maximum awkwardness; this is to ensure that nobody has anything meaningful to discuss during dinner, and everyone would instead silently enjoy her rather tasty coriander soup (as the saying goes; “when the food is good, conversation dies”).</p>

<p>Margarethe knows that awkwardness is maximized if the guests are seated in a long row along a single table, in such a way that nobody sits next to someone speaking the same language as themselves. Better yet, she has defined the awkwardness level of a seating arrangement to be the minimum number of seats separating any two guests speaking the same language. If no two people speak the same language, the awkwardness level is defined to be n (the number of guests). Two seats next to each other are said to be separated by 1.</p>

<p>Given the languages spoken in a proposed seating arrangement, can you help Margarethe determine the awkwardness level?</p>

### 입력 

 <p>The first line contains an integer n (1 ≤ n ≤ 100 000) denoting the number of guests. On the second line follows n integers, the i’th of which x<sub>i</sub> (0 ≤ x<sub>i</sub> ≤ 10<sup>9</sup>) indicating the language spoken by the guest seated at position i in the proposed arrangement (each guest speaks exactly one language).</p>

### 출력 

 <p>A single integer, the awkwardness level of the proposed seating arrangement.</p>

