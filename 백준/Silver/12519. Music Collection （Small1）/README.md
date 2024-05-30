# [Silver II] Music Collection (Small1) - 12519 

[문제 링크](https://www.acmicpc.net/problem/12519) 

### 성능 요약

메모리: 31120 KB, 시간: 80 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2024년 5월 30일 23:27:56

### 문제 설명

<p>Audio Phil has a huge music collection, and he is very particular about the songs he listens to. Each song has a name that is a string of characters. His music player has a search feature that lets Phil type a substring into the search box, and the player then lists all songs whose names contain the substring. If there is exactly one song that matches the search, then Phil can hit the Enter key to play that song.</p>

<p>Phil hates using the mouse, and he doesn't like typing too much, so he insists on always typing the shortest possible substring that will match exactly the one song that he wants to play at this moment. Could you help him find his optimal search query?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>.  <strong>T</strong> test cases follow. Each one starts with a line containing a single number <strong>N</strong>. The next <strong>N</strong> lines each contain one song name -- these are all of the songs in Phil's collection.</p>

<p>Each song name will consist of only letters, spaces and the hyphen character (-). All songs in Phil's collection will be unique and at most 100 characters in length. Song names are case insensitive, so "dZihan" is the same is "Dzihan". The search algorithm is also case insensitive.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 100.</li>
	<li>1 ≤ <strong>N</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>:", where <strong>x</strong> is the case number (starting from 1). After that, print <strong>N</strong> lines, one for each song in Phil's collection, in the order that the songs were given in the input. For each song, print the shortest string of characters that will uniquely find that song. If there are several correct answers, print the lexicographically smallest one. Put double quotes around each string. If there is no correct answer, print ":(" without the double quotes.</p>

<p>Note that upper case letters come lexicographically before lower case letters, hyphen comes before all letters, and space comes before hyphen.</p>

