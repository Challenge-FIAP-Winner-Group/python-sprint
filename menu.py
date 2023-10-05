import alerts
import json
import quests
import validators
import routes

usersFilePath = "db/users/users.json"
user = dict()

# função para dar start no menu principal
def start():
    try:
        print("\n"+("=" * 45) + "PathFinder" + ("=" * 45))
        print("Bem vindo ao PathFinder!")
        init()
    except ValueError:
        alerts.error("Digite um valor válido!")


# função de inicialização do programa verificando se o usuário já possui login
def init():
    valid = False
    while valid == False:
        loginExists = input("Já tem login? (S/N) ").upper()
        if quests.validate(loginExists) == False:
            alerts.error("Digite um valor válido!")
        else:
            valid = True
    if loginExists == "S":
        login()
    else:
        register()


# funcção de realizar login
def login():
    valid = False
    while valid == False:
            username = input("Digite o seu username: ")
            password = input("Digite a sua senha: ")
            fields = [username, password]
            validate(fields)
            with open(usersFilePath, "r") as file:
                obj = json.loads(file.read())
                users = obj["users"]
                found = False
                for item in users:
                    if item["username"] == username:
                        found = True
                        if item["password"] == password:
                            user = item
                            with open("db/users/logged.json", "w", encoding="utf-8") as file:
                                file.write(json.dumps(item))
                            alerts.success(f"Bem-vindo(a) {user['username']}")
                            valid = True
                            break
                        else:
                            alerts.error("Senha incorreta!")
                            break
                    else:
                        found = False
                if found == False:
                    alerts.error("Usuário não encontrado!")
    routes.routesOpt()



# função de realizar cadastro
def register():
    valid = False
    while valid == False:
        name = input("Digite o seu nome: ")
        username = input("Digite o seu username: ")
        zipCode = input("Digite o seu cep no formato (00000-000): ")
        document = input("Digite o seu cpf no formato (000.000.000-00): ")
        age = input("Digite a sua idade: ")
        password = input("Digite a sua senha: ")
        passwordRepeat = input("Repita a sua senha: ")
        fields = [name, username, zipCode, document, password]
        try:
            age = int(age)
        except ValueError:
            age = ""
        if validate(fields):
            alerts.error("Digite valores válidos!")
        else:
            if validators.cep(zipCode) and validators.cpf(document):  
                if password != passwordRepeat:
                    alerts.error("A confirmação da senha precisa ser igual a senha!")
                else:
                    data = dict(username = username, password = password, name = name, zipCode = zipCode, age = age, document =     document)
                    obj = dict()
                    with open(usersFilePath, "r") as file:
                        obj = json.loads(file.read())
                        for item in obj['users']:
                            if item["username"] == data["username"]:
                                alerts.error("Este usuário já exite!")
                    with open(usersFilePath, "w") as save:
                        obj["users"].append(data)
                        save.write(json.dumps(obj))
                        alerts.success("Cadastro feito com sucesso!")
                    cont = input("Deseja realizar login e prosseguir com o programa? (S/N) ").upper()
                    quests.validate(cont)
                    if cont == "S":
                        valid = True
                        login()
                    else:
                        alerts.bye(data["username"])
                        valid = True
            else:
                alerts.error("Digite valores válidos!")

        
def getUser():
    return user

# função para validar todos os campos do formulário
def validate(arr):
    for i in arr:
        if len(i) == 0:
            return True
    return False
