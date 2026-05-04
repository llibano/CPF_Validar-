cpf = input("Digite seu CPF: ")

cpf = cpf.replace(".", "").replace("-", "")

if len(cpf) != 11:

print("CPF inválido!")

else:

print("CPF válido!")
