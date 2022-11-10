# Projeto Inventory Report

Esse projeto foi realizado para exercitar o que foi aprendido na Seção 2 do Módulo de Ciência da Computação do curso da [Trybe](https://www.betrybe.com/), no qual foi sobre `Programação Orientada a Objetos` e `Aplicação de Design Pattern` utilizando a linguagem de programação `Python`.

Neste projeto foi desenvolvido um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados. Para isso, foi utilizada `Programação Orientada a Objetos` e `Design Pattern` para melhor estruturação e legibilidade do código.

Os dados de estoque podem ser obtidos de diversas fontes:

- Através da importação de um arquivo CSV;

- Através da importação de um arquivo JSON;

- Através da importação de um arquivo XML.

Além disso, o relatório final possui duas versões: __simples__ e __completa__.

## Tecnologias

  - Python
  - Pytest
  - Docker

## Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone git@github.com:Lucas-Almeida-SD/Trybe-Projeto_35-Inventory-Report.git

$ cd Projeto_35-Inventory-Report
```

Para iniciá-lo, siga os passos abaixo:

<details>
  <summary><strong>Com Docker</strong></summary>

  ```bash
  # Criar container e iniciar terminal bash
  $ docker-compose run --rm inventory bash 
  ```

  Para executar a aplicação,  utilize o terminal e insira o comando no seguinte formato:
  ```bash
  $ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
  ```

  Exemplo: 
  ```bash
  inventory_report inventory_report/data/inventory.csv simples
  ```

  Para executar os testes, utilize o terminal e insira o comando abaixo: 

  ```bash
  $ python3 -m pytest
  ```
</details>

<details>
  <summary><strong>Sem Docker</strong></summary>

  ```bash
  # criar o ambiente virtual
  $ python3 -m venv .venv

  # ativar o ambiente virtual
  $ source .venv/bin/activate

  # instalar as dependências no ambiente virtual
  $ python3 -m pip install -r dev-requirements.txt

  # instalar o próprio código como um pacote pip
  $ pip install .
  ```

  Para executar a aplicação, insira o comando no seguinte formato:
  ```bash
  $ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
  ```

  Exemplo: 
  ```bash
  inventory_report inventory_report/data/inventory.csv simples
  ```

  Para executar os testes, insira o comando abaixo: 

  ```bash
  $ python3 -m pytest
  ```
</details>
