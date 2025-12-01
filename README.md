# Cassino CLI – Fortune-Bald 

Cassino de linha de comando desenvolvido em **Python**, com foco em boas práticas de desenvolvimento de software:

- Organização em módulos (`cassino_cli/games`, `cassino_cli/utils`)
- Gerenciamento de dependências e build com **Poetry**
- **Testes automatizados** (unitários + uso de *mocks*) com **pytest**
- **Integração Contínua** com **Jenkins** (pipeline declarativa)
- Versionamento com **Git** e uso adequado de `.gitignore`

A aplicação implementa dois jogos:

- **Blackjack (21)**
- **Caça-Níquel (3 símbolos)**

Exposta como uma **CLI (Command Line Interface)**, pode ser executada diretamente via terminal.

---

##  Objetivos do projeto

- Demonstrar uma aplicação Python estruturada em módulos reutilizáveis.
- Gerenciar dependências, build e scripts com **Poetry**.
- Implementar **testes unitários** e testes com **mock/monkeypatch**.
- Automatizar o fluxo de **build, testes e execução** com uma pipeline no **Jenkins**.
- Aplicar boas práticas de **versionamento** (Git) e de organização de projeto.

---

##  Tecnologias utilizadas

- **Linguagem**: Python 3.10+
- **Gerenciador de dependências / build**: [Poetry](https://python-poetry.org/)
- **Testes**: [pytest](https://docs.pytest.org/)
- **CLI**: [Click](https://click.palletsprojects.com/)
- **Interface de terminal**: [Rich](https://rich.readthedocs.io/)
- **CI/CD**: Jenkins (Pipeline Declarativa)
- **Versionamento**: Git

---

##  Estrutura do projeto

```text
.
├── cassino_cli/
│   ├── __init__.py
│   ├── __main__.py          # Ponto de entrada da aplicação (CLI)
│   ├── games/
│   │   ├── __init__.py
│   │   ├── blackjack.py     # Lógica do Blackjack
│   │   └── slots.py         # Lógica do Caça-Níquel
│   └── utils/
│       ├── __init__.py
│       └── deck.py          # Funções de baralho (novo deck, valor da mão, formatação)
├── tests/
│   ├── test_blackjack.py    # Testes do Blackjack
│   └── test_slots.py        # Testes do Caça-Níquel
├── .gitignore               # Arquivos e pastas ignorados pelo Git
├── Jenkinsfile              # Pipeline de CI (Jenkins)
├── poetry.lock              # Lockfile gerado pelo Poetry
├── pyproject.toml           # Configuração do Poetry e metadados do projeto
└── README.md                # Documentação do projeto
