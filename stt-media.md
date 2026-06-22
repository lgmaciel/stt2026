# Média Aritmética

Média é como o "ponto de equilíbrio" em uma série de dados.

Imagine que você quer saber a nota média ao longo do ano. Se tirou 7, 8, 9 em três provas, qual foi o desempenho geral?

Não é tão bom dizer "tirei 7, 8 e 9" — isso são três notas diferentes. Mas se você disser "tirei 8 em média", todos entendem: você está indo bem, mas não é excepcional.

## Conceito-Chave:

- Média: Soma de todos os valores​ dividida pela quantidade de valores

$média = \frac{somatorio(x)}{quantidade(x)}$


### Exemplo 1: Notas Simples

Notas: $7, 8, 9$

$Média = (7 + 8 + 9) ÷ 3 = 24 ÷ 3 = 8$

Você tirou $8$ de média.


### Exemplo 2: Usando Tabela de Frequência

Voltando às notas do Exercício 2:

|Nota|	Frequência (f)|	Nota × f|
|----|----------------|---------|
|5|	2|	$5 × 2 = 10$|
|6|	3|	$6 × 3 = 18$|
|7|	4|	$7 × 4 = 28$|
|8|	3|	$8 × 3 = 24$|
|9|	2|	$9 × 2 = 18$|
|10|	1|	10 × 1 = 10|
|**Total**|	**15**|	**108**|



$Média= \frac{108}{15}​ = 7.2$


A turma tirou $7,2$ de média.

Note que assim:

- Você não precisa lembrar de 15 notas diferentes
- Uma única média (7,2) resume tudo
- Comparação fica fácil: Se outra turma tirou 6,8 de média, você sabe que a primeira foi melhor

## Exercício 3:

Alturas (em cm) de 8 alunos:

```
162, 168, 155, 170, 165, 162, 168, 160
```

### Tarefa:

- Calcule a altura média
- Crie uma tabela de frequência
- Quantos alunos estão acima da média? Quantos abaixo?
- Explique: "A média é 164 cm. O que isso significa?"


# Média com Dados Agrupados (Intervalos)

Agora vamos:

- Trabalhar com dados contínuos
- Entender por que agrupar facilita a análise

## Conceito-Chave:

- intervalos (faixas, classes)

Quando você tem muitos dados diferentes, agrupar em intervalos (faixas) deixa tudo mais limpo.

Por exemplo, em vez de listar 200 alturas diferentes, você agrupa em "150-160 cm", "160-170 cm", etc.

## Demonstração Prática:

Alturas de 30 alunos (dados brutos):

```
152, 155, 158, 160, 162, 163, 164, 165, 166, 167, 
168, 169, 170, 171, 172, 173, 175, 176, 177, 178,
180, 182, 183, 184, 185, 186, 188, 190, 192, 195
```

### Agrupado em intervalos:

|Intervalo (cm)|	Frequência|	Ponto Médio|	f × Ponto Médio|
|--------------|--------------|------------|-------------------|
|150 a 160|	3|	155|	465|
|160 a 170|	12|	165|	1.980|
|170 a 180|	10|	175|	1.750|
|180 a 190|	4|	185|	740|
|190 a 200|	1|	195|	195|
|Total    |	30|	—	|5.130|

$Média=5.130/30 ​ = 171 cm$

Por que "Ponto Médio"?

1. Você não sabe a altura exata de cada aluno no intervalo 150-160
1. Então você supõe que todos têm a altura média do intervalo: 155 cm
1. assim temos só uma aproximação, mas é rápido e funciona bem

