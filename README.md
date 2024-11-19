# Pipeline de Dados do Telegram - Análise de Mensagens em Tempo Real (Ebac Módulo 42)

  

## 🎯 Objetivo do Projeto

Desenvolver um pipeline de dados completo para coletar, processar e analisar mensagens do Telegram em tempo real, utilizando serviços da AWS.

**Links:** [Notebook Kaggle](https://www.kaggle.com/code/dicarvalhoti/pipeline-dados-telegram)

  

## 🏗️ Arquitetura da Solução

![Arquitetura](https://raw.githubusercontent.com/dicarvalhoti/pipeline-data-telegram/main/imgs/architecture.png)

  

### Componentes Principais:

1.  **Ingestão de Dados**

- Bot do Telegram como fonte de dados (WebHook)

- AWS API Gateway para receber webhooks

- AWS Lambda para processamento inicial

- AWS S3 (bucket raw) para armazenamento dos dados brutos

  

2.  **Processamento (ETL)**

- AWS Lambda para transformação

- Conversão de JSON para Parquet

- AWS S3 (bucket enriched) para dados processados

- AWS EventBridge para automação

  

3.  **Análise**

- AWS Athena para consultas SQL

- Visualização de dados

  

## 📊 Principais Métricas Analisadas

- Volume de mensagens por dia

- Tipos de usuários mais ativos

- Horários de pico de mensagens

- Análise de conteúdo das mensagens

  

## 💡 Insights Obtidos 

1. Padrões de uso do bot

2. Comportamento dos usuários

3. Tendências de comunicação

  

## 🛠️ Tecnologias Utilizadas


## 🛠️ Tecnologias Utilizadas

  

### 👨‍💻 Linguagens de Programação

- 🐍 **Python**: Linguagem de programação principal, escolhida por sua versatilidade e rico ecossistema de bibliotecas para processamento de dados.

  

### ☁️ Serviços AWS

- ⚡ **AWS Lambda**: Serviço de computação serverless que executa código em resposta a eventos, usado para processar as mensagens do Telegram.

- 🗄️ **AWS S3**: Serviço de armazenamento em nuvem, utilizado para armazenar dados brutos e processados em diferentes camadas (raw e enriched).

- 🌐 **AWS API Gateway**: Serviço para criar, publicar e gerenciar APIs RESTful, usado para receber webhooks do Telegram.

- 🔄 **AWS EventBridge**: Serviço de barramento de eventos serverless, utilizado para automatizar o pipeline de dados.

- 📊 **AWS Athena**: Serviço de análise interativa que facilita a análise de dados no S3 usando SQL padrão.

  

### 🤖 APIs e Frameworks

- 📱 **Telegram Bot API**: Interface de programação oficial do Telegram para desenvolvimento de bots, permitindo interação automatizada com usuários.

  

### 🔧 Ferramentas de Processamento de Dados

- 🏹 **PyArrow**: Biblioteca Python para processamento de dados em memória e operações de I/O, otimizada para big data.

- 📦 **Parquet**: Formato de arquivo colunar otimizado para análise de big data, oferecendo compressão eficiente e desempenho superior em consultas.

  
## APIs e Frameworks

-  **Telegram Bot API**: Interface de programação oficial do Telegram para desenvolvimento de bots, permitindo interação automatizada com usuários.

  

### Ferramentas de Processamento de Dados

-  **PyArrow**: Biblioteca Python para processamento de dados em memória e operações de I/O, otimizada para big data.

-  **Parquet**: Formato de arquivo colunar otimizado para análise de big data, oferecendo compressão eficiente e desempenho superior em consultas.

  

## 📈 Resultados

- Pipeline automatizado e escalável

- Dados estruturados e prontos para análise

- Insights em tempo real sobre interações

  

## 🔄 Próximos Passos

1. Implementar análise de sentimentos

2. Criar dashboards automatizados

3. Expandir análises estatísticas

  

## 📝 Conclusão

Este projeto demonstra a capacidade de construir um pipeline de dados completo, desde a ingestão até a análise, utilizando tecnologias modernas e práticas de engenharia de dados.



---

*Projeto desenvolvido como projeto Final do curso de Análise de Dados da EBAC*
