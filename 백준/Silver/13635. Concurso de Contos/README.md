# [Silver IV] Concurso de Contos - 13635 

[문제 링크](https://www.acmicpc.net/problem/13635) 

### 성능 요약

메모리: 31120 KB, 시간: 48 ms

### 분류

문자열

### 제출 일자

2024년 5월 27일 21:33:42

### 문제 설명

<p>Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez, além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de submissão do conto.</p>

<p>As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras do concurso, e precisa de sua ajuda.</p>

<p>Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto utilizaria seguindo as regras do concurso.</p>

### 입력 

 <p>A primeira linha de um caso de teste contém três inteiros N, L e C, que indicam, respectivamente, o número de palavras do conto de Machado, o número máximo de linhas por página e o número máximo de caracteres por linha. O conto de Machado é inovador e não contém nenhum caractere além de letras maiúsculas e minúsculas e espaços em branco, sem letras acentuadas e sem cedilha. A segunda linha contém o conto de Machado, composto de N palavras separadas por espaços em branco; há espaço em branco somente entre duas palavras, e entre duas palavras há exatamente um espaço em branco.</p>

<p>Restrições</p>

<ul>
	<li>2 ≤ N ≤ 1000</li>
	<li>1 ≤ L ≤ 30</li>
	<li>1 ≤ C ≤ 70</li>
	<li>1 ≤ comprimento de cada palavra ≤ C</li>
</ul>

### 출력 

 <p>Para cada caso de teste imprima uma única linha, contendo um único número inteiro, indicando o número mínimo de páginas que o conto de Machado ocupa, considerando as regras do concurso.</p>

