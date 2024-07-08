# [Bronze III] 팰린드롬 소떡소떡 - 25630 

[문제 링크](https://www.acmicpc.net/problem/25630) 

### 성능 요약

메모리: 31120 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2024년 7월 8일 13:48:09

### 문제 설명

<p>소떡소떡은 기다란 꼬치에 소세지와 떡을 끼운 음식이다. 편의상 소떡소떡을 알파벳 <code>s</code>와 <code>t</code>로만 구성된 길이 $N$의 문자열로 생각하자. 알파벳 <code>s</code>는 소세지를, <code>t</code>는 떡을 의미한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/609c4d0e-99eb-4410-980d-4fe807e8b8cd/-/preview/"></p>

<p>위 그림은 길이가 $7$인 소떡소떡의 예시이다. 유진이는 소떡소떡을 먹기 전에 소떡소떡을 <em>팰린드롬 소떡소떡</em>으로 만들려고 한다. 팰린드롬이란, 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때가 같은 문자열을 말한다. 예를 들어 <code>sts</code>, <code>tsst</code>, <code>tt</code>는 팰린드롬이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/6c2a5f1c-d548-46fe-94de-c7e32754536b/-/preview/"></p>

<p>유진이는 특별한 마법을 사용해서 꼬치에 꽂힌 소세지 하나를 떡으로 바꾸거나, 반대로 떡 하나를 소세지로 바꿀 수 있다. 위 그림은 마법을 한 번 사용해서 떡 하나를 소세지로 바꾼 그림이다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d0d7f346-7cfc-423d-b514-9ed4530b31e4/-/preview/"></p>

<p>위 그림은 마법을 한 번 더 사용해서 떡 하나를 소세지로 바꾼 그림이다. 이제 이 소떡소떡은 <em>팰린드롬 소떡소떡</em>이 되었다.</p>

<p>유진이가 먹으려고 하는 소떡소떡이 주어질 때, 이 소떡소떡을 <em>팰린드롬 소떡소떡</em>으로 만들기 위해서는 마법을 최소 몇 번 사용해야 할까?</p>

### 입력 

 <p>첫째 줄에 소떡소떡의 길이 $N(1 \le N \le 100)$이 주어진다.</p>

<p>둘째 줄에 소떡소떡을 의미하는 길이 $N$의 문자열이 주어진다. 이 문자열은 알파벳 <code>s</code>와 <code>t</code>로만 구성되어 있다.</p>

### 출력 

 <p>소떡소떡을 <em>팰린드롬 소떡소떡</em>으로 만들기 위해서 마법을 최소 몇 번 사용해야 하는지 출력한다.</p>

