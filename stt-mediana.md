# Mediana - O Valor do Meio

Agora vamos:

- Entender mediana como alternativa à média
- Quando usar média e mediana

## Conceito-Chave:

- Mediana: o valor que divide os dados no meio (50% abaixo, 50% acima)
- Não é afetada por valores extremos (ao contrário da média)
- Útil quando há "outliers" (valores muito diferentes do resto)

### Exemplo

Imagine que você quer saber o salário típico de uma empresa com 5 funcionários:

```
Funcionário 1: R$ 2.000
Funcionário 2: R$ 2.500
Funcionário 3: R$ 3.000
Funcionário 4: R$ 3.500
Funcionário 5: R$ 50.000

```

- Média: $(2.000 + 2.500 + 3.000 + 3.500 + 50.000) ÷ 5 = R\$ 12.200$

Esse resultado nos engana. Nenhum funcionário ganha perto de R$ 12.200.

- Mediana: O valor do meio quando organizados $= R\$ 3.000$

Isso reflete melhor a realidade. Três ganham R$ 3.000 ou menos; dois ganham R$ 3.000 ou mais.

### Demonstração

Caso 1: Número Ímpar de Dados

Notas de 5 alunos:

```python
5, 6, 8, 8, 9
```

Mediana = valor do meio = 8 (posição 3)

```python
5, 6, [8], 8, 9
```

Caso 2: Número Par de Dados

Notas de 6 alunos:

```python
5, 6, 7, 8, 8, 9
```

Mediana = média dos dois valores do meio = $(7 + 8) ÷ 2 = 7,5$

```
5, 6, [7, 8], 8, 9
```

> Para encontrar a posição do meio em n dados:
>
> - Se n é ímpar: $posição = (n + 1) ÷ 2$
> - Se n é par: pegue as posições $n÷2$ e $(n÷2)+1$, depois calcule a média


## Comparação: Média vs. Mediana

|Situação|	Média|	Mediana|	Qual Usar?|
|--------|-------|---------|--------------|
|Dados normais (sem extremos)|	7,2|	7,0|	Ambas funcionam|
|Dados com outlier (ex: 1, 2, 3, 4, 100)|	22|	3|	Mediana (mais honesta)|
|Queremos o "valor típico"|	—|	Boa|	Mediana|
|Queremos o "resultado geral"|	Boa|	—|	Média|


### Exercício 5:

Preços de 7 smartphones em uma loja (em reais):

```
800, 1.200, 950, 1.100, 850, 2.500, 900
```

#### Tarefa:

- Organize em rol
- Encontre a mediana
- Calcule a média
- Qual valor é mais representativo? Por quê?
