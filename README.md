# Fundamentos de Python para Dados

Repositório criado para documentar minha evolução no estudo de **Python**, com foco em lógica de programação, organização do código e preparação para projetos de Análise e Ciência de Dados.

Os exercícios foram desenvolvidos progressivamente, com funções bem definidas, validação de entradas e documentação dos conceitos praticados.

## Objetivo

Desenvolver uma base sólida em Python que possa ser aplicada posteriormente em projetos de análise de dados, automação e Ciência de Dados.

Os principais objetivos deste repositório são:

- Praticar lógica de programação;
- Compreender os principais tipos de dados;
- Utilizar estruturas condicionais e de repetição;
- Trabalhar com listas e outras coleções;
- Criar funções reutilizáveis;
- Validar dados informados pelo usuário;
- Tratar erros e entradas inválidas;
- Organizar arquivos e projetos;
- Praticar Git e GitHub com commits incrementais;
- Preparar a base para estudos de NumPy, Pandas e visualização de dados.

## Conteúdos praticados

- Variáveis;
- Tipos de dados;
- Operadores aritméticos e de comparação;
- Entrada e saída de dados;
- Conversão de tipos;
- Estruturas condicionais;
- Laços de repetição;
- Listas;
- Funções;
- Parâmetros e retornos;
- Tratamento de erros;
- Validação de intervalos;
- Formatação de resultados;
- Organização de programas em funções.

## Estrutura do repositório

- `exercicios/`: arquivos dos exercícios desenvolvidos;
- `exercicios/README.md`: documentação resumida de cada exercício;
- `.gitignore`: arquivos e diretórios que não devem ser versionados;
- `README.md`: documentação principal do projeto.

Dentro da pasta `exercicios`, estão os seguintes programas:

- `calculadora_media.py`;
- `conversor_temperatura.py`;
- `classificador_notas.py`;
- `pares_impares.py`.

## Exercícios desenvolvidos

### 1. Calculadora de média

Programa que solicita três notas, calcula a média aritmética e classifica a situação do estudante.

**Resultados possíveis:**

- Aprovado;
- Recuperação;
- Reprovado.

**Conceitos praticados:**

- Variáveis;
- Entrada de dados;
- Conversão para números decimais;
- Listas;
- Funções;
- Condicionais;
- Laços de repetição;
- Tratamento de entradas inválidas;
- Formatação da saída.

### 2. Conversor de temperatura

Programa que realiza conversões entre Celsius e Fahrenheit.

**Conversões disponíveis:**

- Celsius para Fahrenheit;
- Fahrenheit para Celsius.

**Conceitos praticados:**

- Funções;
- Parâmetros e retornos;
- Operações matemáticas;
- Condicionais;
- Laços de repetição;
- Menus interativos;
- Tratamento de erros;
- Formatação de resultados.

### 3. Classificador de notas

Programa que solicita o nome, a nota final e a frequência de um estudante.

A partir desses dados, o programa classifica o desempenho e determina a situação acadêmica.

**Classificações de desempenho:**

- Excelente;
- Bom;
- Regular;
- Insuficiente.

**Situações acadêmicas:**

- Aprovado;
- Recuperação;
- Reprovado por nota;
- Reprovado por frequência.

**Conceitos praticados:**

- Funções;
- Condicionais encadeadas;
- Validação de intervalos;
- Regras de negócio;
- Tratamento de erros;
- Formatação de resultados.

### 4. Identificador de números pares e ímpares

Programa que recebe uma quantidade definida de números inteiros e os separa em duas listas.

O programa apresenta:

- Números informados;
- Números pares;
- Números ímpares;
- Quantidade de números em cada grupo;
- Soma dos números pares;
- Soma dos números ímpares.

**Conceitos praticados:**

- Listas;
- Funções;
- Laços de repetição;
- Condicionais;
- Operador de módulo;
- Validação de entradas;
- Funções `sum` e `len`.

## Tecnologias e ferramentas

- Python;
- Visual Studio Code;
- Git;
- GitHub;
- GitHub Codespaces.

## Como executar

1. Faça o download ou clone este repositório.
2. Certifique-se de que o Python esteja instalado.
3. Abra um terminal na pasta principal do projeto.
4. Execute o arquivo correspondente ao exercício desejado.

Exemplo para executar a calculadora de média:

`python exercicios/calculadora_media.py`

Exemplo para executar o conversor de temperatura:

`python exercicios/conversor_temperatura.py`

Exemplo para executar o classificador de notas:

`python exercicios/classificador_notas.py`

Exemplo para executar o identificador de pares e ímpares:

`python exercicios/pares_impares.py`

Em alguns ambientes, pode ser necessário substituir `python` por `python3` ou `py`.

## Organização do desenvolvimento

Cada exercício foi desenvolvido seguindo estas etapas:

1. Definição do problema;
2. Planejamento da solução;
3. Implementação inicial;
4. Execução manual;
5. Validação dos resultados;
6. Tratamento de entradas inválidas;
7. Separação da lógica em funções;
8. Revisão do código;
9. Atualização da documentação;
10. Publicação no GitHub.

## Progresso

- [x] Calculadora de média;
- [x] Conversor de temperatura;
- [x] Classificador de notas;
- [x] Identificador de números pares e ímpares;
- [x] Organização dos programas em funções;
- [x] Tratamento básico de entradas inválidas;
- [x] Revisão dos exercícios;
- [x] Documentação inicial;
- [ ] Análise de vendas por categoria;
- [ ] Leitura e escrita de arquivos;
- [ ] Testes automatizados;
- [ ] Introdução ao Pandas.

## Aprendizados

Durante o desenvolvimento dos exercícios, pratiquei a divisão de um problema em partes menores e a criação de funções com responsabilidades específicas.

Também aprendi a diferença entre:

- Receber um valor com `input`;
- Converter textos para tipos numéricos;
- Retornar um resultado com `return`;
- Exibir informações com `print`;
- Repetir uma operação com `while` e `for`;
- Interromper ou continuar uma repetição;
- Organizar diferentes regras em funções separadas.

Outro aprendizado importante foi a validação de dados. Os programas verificam entradas inválidas, como textos no lugar de números, notas fora do intervalo permitido, frequências incorretas e quantidades menores ou iguais a zero.

A separação entre as funções de cálculo e a função principal tornou os programas mais legíveis e facilitou a revisão do código.

O uso de commits separados para cada exercício também permitiu registrar a evolução do projeto de forma progressiva.

## Próximos passos

Os próximos estudos e melhorias planejados são:

- Desenvolver uma análise de vendas por categoria;
- Praticar dicionários e conjuntos;
- Trabalhar com leitura e escrita de arquivos;
- Criar testes automatizados para as funções;
- Estudar NumPy;
- Iniciar a manipulação de dados com Pandas;
- Criar visualizações com Matplotlib e Seaborn;
- Utilizar Jupyter Notebook;
- Desenvolver um projeto completo de análise exploratória de dados.

## Autor

**Roddy Ramos Gonzáles**

Bacharelando em Tecnologia da Informação com ênfase em Ciência de Dados, em busca de uma oportunidade de estágio em Ciência de Dados, Análise de Dados ou Business Intelligence.

- [GitHub](https://github.com/RoddyRamosG)
- [LinkedIn](https://www.linkedin.com/in/roddy-ramos-g-38483a1a/)
- [E-mail](mailto:roddyramos@gmail.com)
