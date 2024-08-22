# [Bronze I] Hockeymatchen - 24189 

[문제 링크](https://www.acmicpc.net/problem/24189) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

사칙연산, 많은 조건 분기, 구현, 수학

### 제출 일자

2024년 8월 22일 13:39:42

### 문제 설명

<p>Malin älskar att kolla på ishockey. Tyvärr hade hon alldeles för många läxor att göra förra kvällen och kunde inte kolla på direktsändningen av hennes favoritlags senaste match, så nu är hon nyfiken på vad som hände under matchen.</p>

<p>Vanligtvis går hon in på Kvällspapprets sportsidor för att ta reda på det, men tyvärr är en stor del av deras hemsida trasig (de behöver bättre programmerare, lika bra som PO-deltagare) och endast en viss del av statistiken går att utläsa. Malin är främst intresserad av tre olika frågor för varje lag: antalet mål de gjorde, antalet skott deras målvakt räddade, och det totala antalet skott de sköt på motståndarens mål. Givet en del av denna statistik för respektive lag, återkonstruera så mycket av statistiken som möjligt.</p>

### 입력 

 <p>Den första raden innehåller tre heltal: antalet räddningar det första lagets målvakt gjorde, antalet mål som gjordes av det första laget, samt antalet skott som det första laget sköt på motståndarens mål. Den andra raden innehåller motsvarande information för det andra laget.</p>

<p>Alla tal i statistiken som är kända är mellan <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container> och <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msup><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msup><mn>10</mn><mn>9</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10^9$</span></mjx-container>. Om ett tal i statistiken saknas ersätts det med <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-1$</span></mjx-container>.</p>

<p>Det är garanterat att det finns minst ett sätt att ersätta alla <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-1$</span></mjx-container> med tal så att den resulterande statistiken är korrekt.</p>

### 출력 

 <p>Skriv ut statistiken för de två lagen på samma format som i indatan. All saknad statistik som går att unikt bestämma utifrån övriga tal ska skrivas ut istället för <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-1$</span></mjx-container>. Om det inte går att unikt bestämma ett visst tal, skriv ut <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$-1$</span></mjx-container>.</p>

