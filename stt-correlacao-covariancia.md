# Correlação e Covariância

## Conceito 

Imagine que você mede **peso** e **altura** de 50 pessoas. Ao plotar os dados em um gráfico de dispersão, nota um padrão: pessoas mais altas tendem a pesar mais. Mas como **quantificar** essa relação?

- Variância nos diz o quanto **uma variável** se espalha.
- Covariância nos diz o quanto **duas variáveis** se espalham **juntas**.
- Correlação nos diz o quanto **duas variáveis** se movem **na mesma direção**, numa escala padronizada.

---

## Covariância

A covariância mede como duas variáveis variam **conjuntamente**.

$$\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

### Significado das variáveis

| Símbolo | Significado |
|---------|-------------|
| $X, Y$ | As duas variáveis que estamos comparando (ex: peso e altura) |
| $n$ | Número de observações (tamanho da amostra) |
| $x_i$ | O valor da $i$-ésima observação de $X$ |
| $y_i$ | O valor da $i$-ésima observação de $Y$ |
| $\bar{x}$ | Média aritmética de todas as observações de $X$ |
| $\bar{y}$ | Média aritmética de todas as observações de $Y$ |
| $(x_i - \bar{x})$ | O quanto o $i$-ésimo valor de $X$ **se desvia** da média de $X$ |
| $(y_i - \bar{y})$ | O quanto o $i$-ésimo valor de $Y$ **se desvia** da média de $Y$ |

### Como ler a fórmula

Cada termo $(x_i - \bar{x})(y_i - \bar{y})$ multiplica os desvios de $X$ e $Y$ na mesma observação. Se ambos estão **acima** da média (ou ambos **abaixo**), o produto é **positivo**. Se um está acima e o outro abaixo, o produto é **negativo**. A soma de todos esses produtos, dividida por $n$, nos dá a covariância.

---

### Interpretação do sinal

| Sinal | Significado |
|-------|-------------|
| **Positivo (+)** | Quando X aumenta, Y tende a aumentar |
| **Negativo (−)** | Quando X aumenta, Y tende a diminuir |
| **Próximo de 0** | Não há relação linear aparente |

### Limitação

O valor absoluto da covariância **depende da escala** das variáveis. Covariância = 100 pode ser "muito" para variáveis pequenas ou "pouco" para variáveis grandes. **Não conseguimos comparar covariâncias entre datasets diferentes.**

---

## Coeficiente de Correlação de Pearson (r)

Para resolver o problema da escala, normalizamos a covariância dividindo pelos desvios padrão de cada variável:

$$r = \frac{\text{Cov}(X, Y)}{\sigma_X \cdot \sigma_Y}$$

A correlação pergunta:

"Quando X está 1 desvio padrão acima da média, Y tende a estar quantos desvios padrão acima da média?"

Isso dá uma resposta na mesma escala, sempre entre −1 e +1.


### Propriedades

- **Sempre entre −1 e +1**
- **r = +1** → correlação linear perfeita positiva
- **r = −1** → correlação linear perfeita negativa
- **r = 0** → sem correlação linear

### Interpretação prática


| Valor de r | Força da relação |
|------------|------------------|
| 0.8 — 1.0 | Muito forte |
| 0.5 — 0.8 | Forte |
| 0.3 — 0.5 | Moderada |
| 0.0 — 0.3 | Fraca |
| ≈ 0 | Sem relação linear |

---

## ⚠️ Armadilha: Correlação ≠ Causalidade

Dois dados podem estar fortemente correlacionados sem que um **cause** o outro.

**Exemplo clássico:**
- Correlação entre vendas de sorvete e afogamentos: **r ≈ 0.8**
- Conclusão errada: "comer sorvete causa afogamentos"
- Explicação real: um **terceiro fator** (temperatura) afeta ambos

---

## ⚠️ Armadilha: Correlação mede apenas relação **linear**

Uma variável pode ter uma relação forte com outra e a correlação de Pearson ser ≈ 0.

**Exemplo:** dados distribuídos em forma de parábola ($y = x^2$). A correlação linear é próxima de zero, mas a relação é perfeitamente determinística — só que **não-linear**.

---

## Resumo

| Conceito | O que mede | Escala | Faixa |
|----------|-----------|--------|-------|
| Variância | Dispersão de **uma** variável | Depende da unidade | 0 a ∞ |
| Covariância | Dispersão conjunta de **duas** variáveis | Depende das unidades | −∞ a +∞ |
| Correlação | Direção e força da relação linear | **Padronizada** | −1 a +1 |

