# [Silver III] Hard Refactoring - 13996 

[문제 링크](https://www.acmicpc.net/problem/13996) 

### 성능 요약

메모리: 31120 KB, 시간: 44 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2024년 3월 14일 15:00:01

### 문제 설명

<p>Helen had come upon a piece of code that uses a lot of “magical constants”. She found a logical expression that checks if an integer x belongs to a certain set of ranges, like the one shown below:</p>

<pre><code>x >= 5 && x <= 10 || 
x >= 7 && x <= 20 || 
x <= 2 || 
x >= 21 && x <= 25 || 
x >= 8 && x <= 10 || 
x >= 100 </code></pre>

<p>Helen does not like “magical constants”, so she decided to refactor this expression and all similar ones in such a way, that the refactored expression still has the same Boolean result for all integers x, but it uses as few integer constants in its text as possible.</p>

<p>Integers in this problem, including integer x, come from the range of all signed 16 bit integers starting from −2<sup>15</sup> (−32 768) to 2<sup>15</sup> − 1 (32 767) inclusive.</p>

### 입력 

 <p>The input file contains at most 1000 lines. Each line consists of either one comparison or two comparisons separated by logical and operator “&&”. Each comparison starts with “x”, followed by greater-or-equals operator “>=” or less-or-equals operator “<=”, followed by an integer constant. When two comparisons are in the same line, the first one is always greater-or-equals, followed by less-or-equals.</p>

<p>All lines, but the last one, are terminated by logical or operator “||”. All tokens in a line are separated by a single space and there are no trailing or leading spaces.</p>

### 출력 

 <p>Write the refactored expression to the output file in the same format as in the input. You can arrange lines in any order, as long as the resulting expression has the right format, produces the same Boolean result on all integers x, and contains the minimal possible number of integer constants in its text. Numbers must be formatted without leading zeros and there must be precisely one space between tokens on a line.</p>

<p>Write a single line with the word “true” if the expression is true on all integers. Write a single line with the word “false” if the expression is false on all integers.</p>

