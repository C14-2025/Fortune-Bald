# Cassino CLI (Blackjack + Caça-Níquel)

## Requisitos
- Python 3.10+
- Poetry (`pip install poetry` ou `python -m pip install poetry`)

## Instalação (Poetry)
```bash
poetry install
poetry run cassino --help
```

## Rodando
```bash
# Blackjack
poetry run cassino blackjack

# Caça-Níquel
poetry run cassino slots
```

## Gerando artefatos (build)
```bash
poetry build
# -> dist/cassino_cli-0.1.0-py3-none-any.whl e .tar.gz
```

## Instalando o pacote localmente
```bash
pip install dist/cassino_cli-0.1.0-py3-none-any.whl
cassino --help
```
