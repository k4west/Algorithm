# [Bronze I] T9 Spelling (Large) - 12608 

[문제 링크](https://www.acmicpc.net/problem/12608) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

구현, 문자열

### 제출 일자

2024년 7월 8일 14:21:30

### 문제 설명

<p>The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad. We would like to make it easier to write a message to your friend using a sequence of keypresses to indicate the desired characters. The letters are mapped onto the digits as shown below. To insert the character <code>B</code> for instance, the program would press <code>22</code>. In order to insert two characters in sequence from the same key, the user must pause before pressing the key a second time. The space character <code>' '</code> should be printed to indicate a pause. For example, <code>2 2</code> indicates <code>AA</code> whereas <code>22</code> indicates <code>B</code>.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12608/images-27.png"></p>

### 입력 

 <p>The first line of input gives the number of cases, <strong>N</strong>. <strong>N</strong> test cases follow. Each case is a line of text formatted as</p>

<pre>desired_message</pre>

<p>Each message will consist of only lowercase characters <code>a-z</code> and space characters <code>' '</code>. Pressing zero emits a space.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>N</strong> ≤ 100.</li>
	<li>1 ≤ length of message in characters ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #<strong>x</strong>: " followed by the message translated into the sequence of keypresses.</p>

