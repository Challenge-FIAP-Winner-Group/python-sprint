import re

# função para validar se o cpf é válido
def cpf(cpf):
    if re.search("\d{3}.\d{3}.\d{3}-\d{2}", cpf):
        # Remove caracteres não numéricos do CPF
        cpf = re.sub("\.", "", cpf)
        cpf = re.sub("-", "", cpf)

        # Verifica se o CPF possui 11 dígitos
        if len(cpf) != 11:
            return False

        # Calcula o primeiro dígito verificador
        total = 0
        for i in range(9):
            total += int(cpf[i]) * (10 - i)
        left = total % 11
        if left < 2:
            verify1 = 0
        else:
            verify1 = 11 - left

        # Calcula o segundo dígito verificador
        total = 0
        for i in range(10):
            total += int(cpf[i]) * (11 - i)
        left = total % 11
        if left < 2:
            verify2 = 0
        else:
            verify2 = 11 - left

        # Verifica se os dígitos verificadores estão corretos
        if int(cpf[9]) == verify1 and int(cpf[10]) == verify2:
            return True
        else:
            return False
    else:
        return False

# função para validar se o cep é válido
def cep(value):
    if re.search("\d{5}-\d{3}", value):
        return True
    else:
        return False
