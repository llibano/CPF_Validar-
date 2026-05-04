# Validador de CPF em Python

Este projeto é um script simples em Python para validar números de CPF (Cadastro de Pessoas Físicas), verificando se eles são válidos de acordo com as regras oficiais.

## 📌 Funcionalidades

* Remove formatação (`.` e `-`)
* Verifica se o CPF possui 11 dígitos
* Rejeita CPFs com todos os números iguais (ex: `11111111111`)
* Calcula e valida os dois dígitos verificadores
* Informa se o CPF é válido ou inválido

## 🚀 Como usar

1. Clone este repositório ou copie o código:

```bash
git clone https://github.com/seu-usuario/validador-cpf.git
cd validador-cpf
```

2. Execute o script:

```bash
python validar_cpf.py
```

3. Digite o CPF quando solicitado:

```
Digite seu CPF: 123.456.789-09
```

4. O sistema retornará:

```
CPF válido!
```

ou

```
CPF inválido!
```

## 🧠 Como funciona

O algoritmo segue os passos oficiais de validação do CPF:

1. Remove caracteres não numéricos
2. Verifica o tamanho (11 dígitos)
3. Calcula o primeiro dígito verificador:

   * Multiplica os 9 primeiros dígitos por pesos decrescentes de 10 a 2
   * Soma os resultados
   * Calcula `(soma * 10) % 11`
4. Calcula o segundo dígito verificador:

   * Multiplica os 10 primeiros dígitos por pesos de 11 a 2
   * Repete o processo

Se os dígitos calculados coincidirem com os informados, o CPF é válido.

## 📁 Estrutura do projeto

```
validador-cpf/
│
├── validar_cpf.py
└── README.md
```

## 📜 Licença

Este projeto é livre para uso e modificação.

