# [Silver II] Mall - 18988 

[문제 링크](https://www.acmicpc.net/problem/18988) 

### 성능 요약

메모리: 75820 KB, 시간: 896 ms

### 분류

그리디 알고리즘

### 제출 일자

2024년 7월 24일 13:24:53

### 문제 설명

<p>Byton has been sent by his parents to a nearby shopping mall to buy $m$ products from the list, numbered $1$ through $m$. As he loves shopping, he plans to visit every shop in the mall, each of them exactly once. Byton is going to visit the shops in some order and in some of them, he will buy some products from the list that he has not bought yet.</p>

<p>As you can guess, some products may be available in multiple different shops. Unfortunately, Byton is a bit paranoid -- he fears random security checks very much. Therefore, he would like to avoid an awkward situation in which he enters a shop that sells a product that he has already purchased somewhere else.</p>

<p>Can you find a strategy of visiting all the shops and buying products, which will allow Byton to avoid awkward situations with security guards?</p>

### 입력 

 <p>The first line of the input contains two integers $n, m$ ($1 \le n, m \le 1000$) -- the number of shops in the mall and the number of products Byton needs to buy, respectively. The next $n$ lines describe shops in the mall; the $i$-th of them describes the $i$-th shop. Each description begins with a number $k_i$ ($1\leq k_i\leq m$) denoting the number of products of Byton's interest available in the $i$-th shop. Then, $k_i$ integers, each between $1$ and $m$, follow in ascending order. Each of them denotes a product from Byton's list.</p>

### 출력 

 <p>If there does not exists a correct strategy of shopping, you should output a single word <code>NO</code>. Otherwise, the first line of the input should contain the word <code>YES</code>. The second line of the output should contain $n$ distinct integers ranging from $1$ to $n$ -- the order of shops visited by Byton. The last, third line should contain $m$ integers ranging from $1$ to $n$; the $i$-th of them indicates the shop in which Byton should buy the product $i$. If there are multiple solutions, output any of them.</p>

