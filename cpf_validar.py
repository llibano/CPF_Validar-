def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "").strip()

    
    if len(cpf) != 11 or not cpf.isdigit() or len(set(cpf)) == 1:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[9]):
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10 or resto == 11:
        resto = 0
    if resto != int(cpf[10]):
        return False

    return True


cpf = input("Digite seu CPF: ")

if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
