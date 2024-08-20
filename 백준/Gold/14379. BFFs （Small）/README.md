# [Gold V] BFFs (Small) - 14379 

[문제 링크](https://www.acmicpc.net/problem/14379) 

### 성능 요약

메모리: 173784 KB, 시간: 15188 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2024년 8월 20일 18:48:08

### 문제 설명

<p>You are a teacher at the brand new Little Coders kindergarten. You have N kids in your class, and each one has a different student ID number from 1 through N. Every kid in your class has a single best friend forever (BFF), and you know who that BFF is for each kid. BFFs are not necessarily reciprocal -- that is, B being A's BFF does not imply that A is B's BFF.</p>

<p>Your lesson plan for tomorrow includes an activity in which the participants must sit in a circle. You want to make the activity as successful as possible by building the largest possible circle of kids such that each kid in the circle is sitting directly next to their BFF, either to the left or to the right. Any kids not in the circle will watch the activity without participating.</p>

<p>What is the greatest number of kids that can be in the circle?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of two lines. The first line of a test case contains a single integer N, the total number of kids in the class. The second line of a test case contains N integers F<sub>1</sub>, F<sub>2</sub>, ..., F<sub>N</sub>, where F<sub>i</sub> is the student ID number of the BFF of the kid with student ID i.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>1 ≤ F<sub>i</sub> ≤ N, for all i.</li>
	<li>F<sub>i</sub> ≠ i, for all i. (No kid is their own BFF.)</li>
	<li>3 ≤ N ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the maximum number of kids in the group that can be arranged in a circle such that each kid in the circle is sitting next to his or her BFF.</p>

