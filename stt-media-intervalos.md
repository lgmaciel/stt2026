# Média com Dados Agrupados (Intervalos)

Agora vamos:

- Trabalhar com dados contínuos
- Entender por que agrupar facilita a análise

## Conceito-Chave

- intervalos (faixas, classes)

Quando você tem muitos dados diferentes, agrupar em intervalos (faixas) deixa tudo mais limpo.

Por exemplo, em vez de listar 200 alturas diferentes, você agrupa em "150-160 cm", "160-170 cm", etc.

## Demonstração Prática

Alturas de 30 alunos (dados brutos):

```
152, 155, 158, 160, 162, 163, 164, 165, 166, 167, 
168, 169, 170, 171, 172, 173, 175, 176, 177, 178,
180, 182, 183, 184, 185, 186, 188, 190, 192, 195
```

### Agrupado em intervalos

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
