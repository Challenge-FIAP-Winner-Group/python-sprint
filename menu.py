import alerts
import json
import quests

usersFilePath = "db/users/users.txt"
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
    loginExists = input("Já tem login? (S/N) ").upper()
    quests.validate(loginExists)
    if loginExists == "S":
        login()
    else:
        register()


# funcção de realizar login
def login():
    username = input("Digite o seu username: ")
    password = input("Digite a sua senha: ")
    fields = [username, password]
    validate(fields)
    data = dict(username = username, password = password)
    with open(usersFilePath, "r") as file:
        obj = json.loads(file.read())
        users = obj["users"]
        found = False
        for item in users:
            if item["username"] == username:
                found = True
                if item["password"] == password:
                    user = item
                    alerts.success(f"Bem-vindo(a) {user['username']}")
                    break
                else:
                    alerts.error("Senha incorreta!")
                    login()
                    break
            else:
                found = False
        if found == False:
            alerts.error("Usuário não encontrado!")
            login()


# função de realizar cadastro
def register():
    name = input("Digite o seu nome: ")
    username = input("Digite o seu username: ")
    zipCode = input("Digite o seu cep no formato (00000-000): ")
    document = input("Digite o seu cpf no formato (000.000.000-00): ")
    age = int(input("Digite a sua idade: "))
    password = input("Digite a sua senha: ")
    passwordRepeat = input("Repita a sua senha: ")
    fields = [name, username, zipCode, document, password]
    validate(fields)
    if password != passwordRepeat:
        alerts.error("A confirmação da senha precisa ser igual a senha!")
        register()
    else:
        data = dict(username = username, password = password, name = name, zipCode = zipCode, age = age, document = document)
        with open(usersFilePath, "r") as file:
            obj = json.loads(file.read())
            for item in obj['users']:
                if item["username"] == data["username"]:
                    alerts.error("Este usuário já exite!")
                    register()
                    break
            obj["users"].append(data)
            with open(usersFilePath, "w") as save:
                save.write(json.dumps(obj))
                alerts.success("Cadastro feito com sucesso!")
                cont = input("Deseja realizar login e prosseguir com o programa? (S/N) ").upper()
                quests.validate(cont)
                if cont == "S":
                    login()
                else:
                    alerts.bye(data["username"])

        


# função para validar todos os campos do formulário
def validate(arr):
    for i in arr:
        if len(i) == 0:
            raise ValueError
