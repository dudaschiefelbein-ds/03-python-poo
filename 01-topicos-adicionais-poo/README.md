# 📁01: Tópicos Adicionais de POO em Python

Este módulo expande os horizontes da Orientação a Objetos no projeto de gerenciamento de imóveis, introduzindo conceitos avançados de customização de classes, associação de objetos e escopos de métodos.

## 🧠 Conceitos Chave da Aula

*   **Sobrecarga de Operadores (Métodos Especiais):** Customização do comportamento de operadores nativos do Python ao lidar com objetos. Foi utilizado o `__add__` para permitir a soma direta de aposentos entre dois imóveis (`imovel1 + imovel2`), `__gt__` / `__lt__` para comparações de tamanho (maior que / menor que) e `__str__` para representação textual em formato de string.
*   **Composição de Objetos:** Técnica onde uma classe "contém" outra classe. No sistema, a classe `Imovel` possui uma composição com a classe `Categoria`, permitindo delegar funções específicas (como o cálculo de `taxaAgua` por tipo de estabelecimento).
*   **Métodos estáticos (`@staticmethod`) e de Classe (`@classmethod`):** Implementação de comportamentos que pertencem ao contexto geral da classe. O método de classe acessa atributos globais da estrutura (como `imposto`), enquanto o método estático opera como uma função comum encapsulada de forma lógica.

## 🚀 Arquivos da Aula

*   **`imoveis.py`**: Arquivo de código que unifica a lógica de sobrecarga de operadores matemáticos, métodos de classe, métodos estáticos e importação de módulos externos para formatação de dados.

---
*Estudos desenvolvidos durante as aulas de fundamentos de programação.*
