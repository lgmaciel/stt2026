# Amplitude, Intervalo Interquartil (IQR) e Comparação de Distribuições

Agora vamos:

- Medir dispersão
- Comparar dois conjuntos de dados usando gráficos

## Conceito-Chave

Duas turmas podem ter a mesma média, mas distribuições muito diferentes:

Turma A (notas): 6, 7, 7, 8, 8, 8, 9, 9, 10

- Média = 7,8
- Maioria concentrada no meio

Turma B (notas): 1, 3, 5, 7, 8, 9, 10, 10, 10

- Média = 7,0
- Muito espalhada (desigual)

Essas são distribuições muito diferentes, mas você só percebe se medir a dispersão.

### Medidas de Dispersão

|Medida|	Fórmula|	O que mostra|
|-|-|-|
|Amplitude|	Máximo − Mínimo|	Quanto os dados se estendem|
|IQR (Intervalo Interquartil)|	Q3 − Q1|	Onde está a "massa" dos dados (50% do meio)|

## Demonstração Prática

Voltando ao Box Plot que vimos:

- Mínimo = 4, Máximo = 10
- Q1 = 6, Q3 = 8,5

Amplitude = 10 − 4 = 6
Os dados se estendem por 6 unidades

IQR = 8,5 − 6 = 2,5
O "meio" dos dados ocupa 2,5 unidades (bem concentrado)

Interpretação:

- Se IQR é pequeno → dados concentrados → turma com desempenho consistente
- Se IQR é grande → dados espalhados → turma com desempenho variável

Comparação de Duas Turmas com Box Plots Lado a Lado:

Turma A (desempenho bom e consistente):

```
        0   2   4   6   8   10
        |   |   |   |   |   |
    |------[|====|]--|
        3   5   6,5 7,5 9
```

- Mín=3, Q1=5, Q2=6,5, Q3=7,5, Máx=9
- Amplitude = 6; IQR = 2,5

Turma B (desempenho variável):

```
        0   2   4   6   8   10
        |   |   |   |   |   |
    |---[|====|]--------|
        1   3   5   8    10
```

- Mín=1, Q1=3, Q2=5, Q3=8, Máx=10
- Amplitude = 9; IQR = 5

Conclusão:

- Turma A é mais consistente (IQR menor)
- Turma B é mais desigual (IQR maior)
- Turma A tem melhor desempenho geral

> IQR é como a 'altura da caixa' no box plot.
>
> - Caixa baixa = dados concentrados
> - Caixa alta = dados espalhados

Exercício 8:

Você é um treinador de futebol que está comparando dois atacantes:

Atacante A (gols por jogo nos últimos 10 jogos):

```
1, 2, 2, 2, 2, 2, 3, 3, 3, 4
```

Atacante B (gols por jogo nos últimos 10 jogos):

```
0, 0, 1, 2, 2, 2, 3, 4, 4, 5
```

Tarefa:

- Calcule média, mediana, amplitude, IQR de cada um
- Desenhe box plots lado a lado para ambos
- Qual atacante você escalaria no próximo jogo? Por quê?
- Qual é mais consistente (previsível)?
