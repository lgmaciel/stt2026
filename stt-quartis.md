# DIA 8: Quartis e Diagrama de Caixa (Box Plot)

Objetivo: Entender dispersão dos dados; desenhar e interpretar box plots.

Conceito-Chave:

Se a mediana divide os dados em 2 partes iguais, os quartis dividem em 4 partes iguais:

    Q1 (1º quartil) = valor que deixa 25% abaixo e 75% acima
    Q2 (2º quartil) = mediana (50% abaixo, 50% acima)
    Q3 (3º quartil) = valor que deixa 75% abaixo e 25% acima


Hook do Mundo Real:

Você está analisando a renda de 100 famílias. Saber apenas a média (R$ 5.000) não diz tudo. E se:

    25% das famílias ganham menos de R$ 2.000 (Q1)?
    50% ganham menos de R$ 4.500 (Q2)?
    75% ganham menos de R$ 7.000 (Q3)?


Isso mostra a verdadeira distribuição. Muita desigualdade!

Demonstração Prática:

Dados: Notas de 20 alunos (já em rol)

```
Rol: 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 10, 10
```

Passo 1: Encontre a Mediana (Q2)

Com 20 valores (par), mediana = média das posições 10 e 11:

    Posição 10: 7
    Posição 11: 8
    Q2 = (7 + 8) ÷ 2 = 7,5

Passo 2: Encontre Q1 (mediana da metade inferior)

Metade inferior = primeiros 10 valores:

```
4, 5, 5, 6, 6, 6, 7, 7, 7, 7
```

Mediana dessa metade = (6 + 6) ÷ 2 = Q1 = 6

Passo 3: Encontre Q3 (mediana da metade superior)

Metade superior = últimos 10 valores:

```
8, 8, 8, 8, 8, 9, 9, 9, 10, 10
```

Mediana dessa metade = (8 + 9) ÷ 2 = Q3 = 8,5

Passo 4: Encontre Mínimo e Máximo

    Mínimo = 4
    Máximo = 10

Resumo (5-Número):


|Mínimo|	Q1|	Q2| (Mediana)|	Q3|	Máximo|
|-|-|-|-|-|-|
|4|	6|	7,5|	8,5|	10|
