# Análise de Satisfação de Clientes com Teste de Hipóteses

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Analysis-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## Visão Geral

Este projeto analisa o impacto de uma mudança no layout de equipamentos de uma academia sobre a satisfação dos clientes.

A análise foi conduzida utilizando métodos estatísticos para apoiar a tomada de decisão baseada em dados, simulando um cenário real de negócio.

---

## Problema de Negócio

A academia realizou alterações no layout com o objetivo de melhorar a experiência dos usuários.

A principal questão é:

**A mudança no layout gerou aumento significativo na satisfação dos clientes?**

A resposta a essa pergunta é fundamental para decidir se a nova configuração deve ser mantida ou revisada.

---

## Abordagem Analítica

A análise seguiu uma abordagem estruturada:

1. Exploração e validação dos dados
2. Análise descritiva e visual
3. Formulação de hipóteses
4. Teste estatístico
5. Interpretação dos resultados
6. Tradução dos resultados em decisão de negócio

---

## Dataset

Os dados foram simulados para representar avaliações de satisfação em escala de 0 a 10:

* `satisfacao_antes`
* `satisfacao_depois`

A estrutura simula medições do mesmo grupo de clientes antes e depois da intervenção.

## Estrutura do Projeto

* `notebooks/analise_satisfacao.ipynb` — notebook principal com geração de dados, EDA e teste de hipótese.
* `requirements.txt` — dependências mínimas necessárias para reproduzir a análise.

## Instalação

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Executar

Abra o notebook com:
```bash
jupyter notebook notebooks/analise_satisfacao.ipynb
```

Em seguida, execute todas as células para reproduzir a análise.

---

## Preparação dos Dados

* Validação de tipos e consistência
* Tratamento de limites (0 a 10)
* Análise estatística descritiva
* Preparação para testes inferenciais

---

## Análise Exploratória

A análise exploratória indicou:

* Deslocamento da distribuição de satisfação
* Redução de valores mais baixos
* Tendência de aumento após a mudança

Visualizações utilizadas:

* Histogramas
* Boxplots

---

## Metodologia Estatística

### Hipóteses

* **H0:** não há diferença na média de satisfação
* **H1:** há diferença na média de satisfação

---

### Teste Aplicado

Foi utilizado o **teste t pareado**, adequado para comparar medições do mesmo grupo em dois momentos distintos.

---

### Validação dos Pressupostos

* Teste de normalidade de Shapiro-Wilk aplicado às diferenças
* Suposição de independência respeitada
* Dados adequados para teste paramétrico

---

## Resultados Estatísticos

* **p-valor:** < 0.05
* **Diferença média:** aumento na satisfação
* **Intervalo de confiança (95%):** (0.25, 1.04)

---

## Insights Analíticos

* Há evidência estatística de aumento na satisfação
* O intervalo de confiança não inclui zero, reforçando o resultado
* O efeito observado é consistente entre os usuários
* O impacto é pequeno a moderado, porém relevante

---

## Interpretação para Negócio

A mudança no layout teve efeito positivo mensurável na experiência dos clientes.

Mesmo com um efeito moderado, o resultado é relevante porque:

* Afeta diretamente a percepção do cliente
* Pode influenciar retenção e fidelização
* Melhora a experiência geral no ambiente

---

## Impacto de Negócio

Com base nos resultados, recomenda-se:

* Manutenção do novo layout
* Monitoramento contínuo da satisfação
* Aplicação de melhorias incrementais no ambiente

Possíveis impactos:

* Aumento de retenção de clientes
* Melhoria na avaliação da academia
* Maior engajamento dos usuários

---

## Limitações

* Dados simulados (não reais)
* Não considera segmentação de clientes
* Não avalia fatores externos (horário, lotação, perfil do usuário)

---

## Próximos Passos

* Segmentação por perfil de cliente
* Aplicação de testes não paramétricos
* Análise de impacto por frequência de uso
* Construção de dashboard interativo
* Integração com base de dados real

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* Seaborn

---

## Como Executar

```bash
# Clonar repositório
git clone https://github.com/FilipeMadeira13/analise-satisfacao-teste-hipoteses.git

# Acessar diretório
cd analise-satisfacao-teste-hipoteses

# Instalar dependências
pip install -r requirements.txt

# Executar notebook
jupyter notebook
```

---

## Estrutura do Projeto

```
analise-satisfacao-teste-hipoteses/
│
├── data/
├── notebooks/
├── src/
├── requirements.txt
└── README.md
```

---

## Autor

**Filipe Madeira**
Data Analyst | Python | SQL | Estatística Aplicada

Projeto desenvolvido com foco em análise de dados aplicada à tomada de decisão.

---

## Diferencial deste Projeto

Este projeto demonstra na prática:

* Aplicação de estatística inferencial em contexto real
* Capacidade de traduzir dados em decisões de negócio
* Comunicação clara de resultados analíticos
* Estrutura profissional de projeto para portfólio
