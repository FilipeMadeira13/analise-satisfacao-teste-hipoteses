# 📊 Análise de Satisfação com Teste de Hipóteses

## 🧠 Contexto

Uma academia realizou uma mudança no layout dos equipamentos com o objetivo de melhorar a experiência dos clientes.

Diante disso, surge a seguinte pergunta de negócio:

> A nova disposição dos equipamentos realmente aumentou a satisfação dos usuários?

Este projeto simula um cenário real de tomada de decisão orientada por dados, utilizando técnicas estatísticas para validar hipóteses.

---

## 🎯 Objetivo

Avaliar se houve uma diferença estatisticamente significativa na satisfação dos clientes antes e depois da mudança no layout, e interpretar se essa diferença possui relevância prática.

---

## 📦 Dataset

Os dados foram simulados para representar avaliações de satisfação em uma escala de 0 a 10:

* `satisfacao_antes`: avaliação antes da mudança
* `satisfacao_depois`: avaliação após a mudança

A simulação foi construída para reproduzir um cenário realista de análise de negócio.

---

## 🧹 Tratamento de Dados

* Verificação de tipos e estrutura dos dados
* Análise descritiva (média, desvio padrão, distribuição)
* Limitação dos valores ao intervalo válido (0 a 10)
* Preparação dos dados para aplicação de testes estatísticos

---

## 📊 Análise Exploratória (EDA)

Foram utilizadas técnicas de visualização para compreender o comportamento dos dados:

* Histogramas para análise de distribuição
* Boxplot para comparação entre os períodos

A análise indicou um deslocamento da distribuição de satisfação após a mudança, sugerindo um possível aumento.

---

## 🧪 Metodologia Estatística

### Hipóteses

* **H0 (hipótese nula):** não há diferença na satisfação média
* **H1 (hipótese alternativa):** há diferença na satisfação média

---

### Teste aplicado

Foi utilizado o **teste t pareado**, apropriado para comparar duas amostras dependentes (mesmos indivíduos em momentos diferentes). ([wilson0106.github.io][1])

---

### Validação dos pressupostos

Foi realizado teste de normalidade (Shapiro-Wilk) sobre a diferença entre os grupos, garantindo a adequação do teste paramétrico.

---

### Interpretação do p-valor

O p-valor representa a probabilidade de observarmos um resultado tão extremo quanto o obtido, assumindo que a hipótese nula seja verdadeira.

---

## 📈 Resultados

* **P-valor:** < 0.05
* **Diferença média:** aumento na satisfação após a mudança
* **Intervalo de confiança (95%):** (0.25, 1.04)

---

## 🧠 Interpretação dos Resultados

O intervalo de confiança indica que, com 95% de confiança, o aumento médio na satisfação está entre **0.25 e 1.04 pontos**.

Como o intervalo não inclui o valor zero, isso reforça a evidência de que houve um aumento real na satisfação dos clientes.

Além disso, o tamanho do efeito sugere um impacto **pequeno a moderado**, indicando que a mudança teve efeito consistente na experiência dos usuários.

---

## 🏁 Conclusão

A análise estatística fornece evidências de que a mudança no layout teve impacto positivo na satisfação dos clientes.

Principais conclusões:

* A hipótese nula foi rejeitada com base no p-valor
* O aumento na satisfação é estatisticamente significativo
* O intervalo de confiança confirma a existência de efeito real
* O impacto observado possui relevância prática

Do ponto de vista de negócio, a mudança pode ser considerada eficaz e recomenda-se sua manutenção.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## ▶️ Como Executar

```bash
# Clonar repositório
git clone https://github.com/FilipeMadeira13/analise-satisfacao-teste-hipoteses.git

# Acessar pasta
cd analise-satisfacao-teste-hipoteses

# Instalar dependências
pip install -r requirements.txt

# Executar notebook
jupyter notebook
```

---

## 📌 Possíveis Extensões

* Aplicação de testes não paramétricos (Mann-Whitney)
* Segmentação de clientes (idade, frequência, perfil)
* Construção de dashboard interativo (Streamlit ou Power BI)
* Integração com banco de dados e SQL

---

## 👨‍💻 Autor

**Filipe Madeira**
Projeto desenvolvido com foco em análise de dados aplicada à tomada de decisão, como parte da construção de portfólio profissional.
