def validate(quest):
    if str(quest).upper() != "S" and str(quest).upper() != "N":
        raise ValueError