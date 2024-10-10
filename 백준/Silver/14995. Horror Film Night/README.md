# [Silver II] Horror Film Night - 14995 

[문제 링크](https://www.acmicpc.net/problem/14995) 

### 성능 요약

메모리: 225092 KB, 시간: 796 ms

### 분류

그리디 알고리즘, 구현

### 제출 일자

2024년 10월 10일 22:32:10

### 문제 설명

<p>Emma and Marcos are two friends who love horror films. This year, and possibly the years hereafter, they want to watch as many films together as possible. Unfortunately, they do not exactly have the same taste in films. So, inevitably, every now and then either Emma or Marcos has to watch a film she or he dislikes. When neither of them likes a film, they will not watch it. To make things fair they thought of the following rule: They can not watch two films in a row which are disliked by the same person. In other words, if one of them does not like the current film, then they are reassured they will like the next one. They open the TV guide and mark their preferred films. They only receive one channel which shows one film per day. Luckily, the TV guide has already been determined for the next 1 million days.</p>

<p>Can you determine the maximal number of films they can watch in a fair way?</p>

### 입력 

 <p>The input consists of two lines, one for each person. Each of these lines is of the following form:</p>

<ul>
	<li>One integer 0 ≤ k ≤ 1000000 for the number of films this person likes;</li>
	<li>followed by k integers indicating all days (numbered by 0, . . . , 999999) with a film this person likes.</li>
</ul>

### 출력 

 <p>Output a single line containing a single integer, the maximal number of films they can watch together in a fair way.</p>

