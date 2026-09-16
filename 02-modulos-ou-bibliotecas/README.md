# 📁 02: Módulos ou Bibliotecas em Python

Este módulo aborda a modularização de código em Python, cobrindo tanto a criação e importação de módulos customizados quanto a utilização de bibliotecas nativas essenciais para manipulação de datas, matemática e aleatoriedade.

## 🧠 Conceitos Chave da Aula

*   **Modularização Própria:** Técnica de separar funções específicas em arquivos independentes para organizar o projeto e permitir o reuso do código. Foi demonstrada na criação de um módulo utilitário de datas que é consumido pela regra de negócios de imóveis.
*   **Manipulação de Datas (`datetime`):** Uso de funções para formatação de strings em objetos de tempo (`strptime`) e conversão de datas internas para exibição legível ao usuário (`strftime`).
*   **Bibliotecas Nativas (`math` e `random`):** Exploração de recursos matemáticos complexos (como arredondamentos para baixo com `floor`, para cima com `ceil` e constante `pi`) e geração de números pseudoaleatórios (como inteiros dentro de intervalos específicos com `randint`).

## 🚀 Arquivos da Aula

*   **`data.py`**: Módulo customizado criado para concentrar funções utilitárias de manipulação, conversão e formatação de datas com base na biblioteca `datetime`.
*   **`imoveis.py`**: Arquivo principal que demonstra a integração de módulos, importando as funções do arquivo `data.py` para registrar cronologicamente a leitura e aplicação de taxas do imóvel.
*   **`operacoes_math.py`**: Script prático focado no estudo e aplicação de funções matemáticas da biblioteca padrão `math`, englobando constantes e regras de aproximação numérica.
*   **`operacoes_random.py`**: Código focado na utilização da biblioteca padrão `random` para simulações que necessitam de sorteios numéricos e valores aleatórios no sistema.

---
*Estudos desenvolvidos durante as aulas de fundamentos de programação.*
