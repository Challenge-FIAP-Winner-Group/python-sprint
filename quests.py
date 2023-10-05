# função para validar se a questão foi respondida corretamente
def validate(quest):
    if str(quest).upper() != "S" and str(quest).upper() != "N":
        return False