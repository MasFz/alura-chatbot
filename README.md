# Alura-chatbot
Projeto de ChatBot realizado durante a Imersão De Inteligência Artificial da Alura.

# Descrição
Imagine que você acaba de entrar em uma nova empresa e deve imediatamente entrar na correria da empresa e aprender tudo o mais rápido possível e tem em suas mãos apenas um guia em formato de texto gigante e não sabe nem como começar.

A ideia desse projeto é fornecer um chatbot com todas as intruções necessárias para um bom trabalho e salvar a vida do novo estagiário. Fique à vontade para testar o código e ver como funciona.

Esse código utiliza do chamado Retrieval Augmented Generation (RAG) para fazer buscas semânticas em documentos e retornar uma resposta personalizada sobre arquivos pessoais. Fique à vontade para inserir novos dados e adaptar o código para suas necessidades pessoais seja dentro do próprio guia.txt quanto criando outros arquivos mas sempre no formato "txt".


## Como executar o código
Você precisa criar um arquivo chamado .env dentro do seu diretório principal e colocar GOOGLE_API_KEY = "SUA CHAVE DE API".

Você precisa baixar os requirements que nada mais são do que as bibliotecas que usei no projeto, basta usar 'pip install -r "requirements.txt"'.

Verifique se você de fato possui o arquivo de texto chamado guia.txt na pasta chamada data.

Para sair do chatbot basta digitar "sair".

## Recomendação
Crie um ambiente virtual de python para rodar o código usando "python -m venv env" em windows ou "python3 -m venv env" em linux. Eu uso linux e para entrar no ambiente virtual basta rodar "source env/bin/activate" depois de ter criado o seu ambiente virtual, para windows "env/Scripts/activate".

## Observação
Usei Transformers ao invés de usar o embedding do próprio gemini para mostrar uma possibilidade de integração com outra ferramenta. Mas fique à vontade para utilizar o que foi visto por exemplo na aula 5 da imersão para realizar a busca semântica.

Se você já tem contato com PLN é legal fazer a busca por similaridade usando outras métricas como por exemplo busca em cosseno ou usando a distância euclidiana
