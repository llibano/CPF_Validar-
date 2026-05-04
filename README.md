# 🧾 Validador de CPF em Python

 Descrição do projeto
Este projeto em Python tem como objetivo criar um programa simples que recebe um CPF digitado pelo usuário e verifica se ele possui a quantidade correta de dígitos

O programa também remove caracteres especiais como pontos e traços antes da verificação.

Funcionamento do programa

O usuário digita o CPF através do comando:

## cpf = input("Digite seu CPF: ")
Em seguida, o programa remove os pontos e traços para deixar apenas os números
cpf = cpf.replace(".", "").replace("-", "")
Depois disso, o programa verifica se o CPF possui exatamente 11 dígitos utilizando a função len()
if len(cpf) != 11:
Se a quantidade de dígitos for diferente de 11, o programa exibe
print("CPF inválido!")
Se o CPF tiver 11 dígitos o programa exibe 
print("CPF Válido") 

fim do programa !!! 
