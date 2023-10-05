import places
import menu
import alerts
import json
import random
import quests

# list que guarda todas as opções de roteiros
choices = []
choosen = dict()
transports = []
choosenTrasnport = ""
locations = []

# função para iniciar o programa
def main():
    try:
        # chamando a função de menu
        menu.start()
        # escolhendo opções de roteiros
        cont = "S"
        while cont.upper() == "S":
            print("\n"+("=" * 45) + "Escolha o tipo de roteiro" + ("=" * 45) + "\n")
            choices = places.get()
            control = 1
            for i in choices:
                print(f"({control}) -> {i['name']}: {i['types']}")
                control += 1
            print("\nEscolha uma das opções:")
            choice = int(input("> "))
            if choice < 1 or choice > len(choices):
                alerts.error(f"Escolha uma opção de 1 a {len(choices)}!")
            else:
                choosen = choices[choice - 1]
                with open("db/transports.txt", "r", encoding="utf-8") as file:
                    transports = json.loads(file.read())["transports"]
                control = 1
                for i in transports:
                    print(f"({control}) -> {i}")
                    control += 1
                print("\nEscolha uma das opções:")
                choice = int(input("> "))
                if choice < 1 or choice > len(transports):
                    alerts.error(f"Escolha uma opção de 1 a {len(transports)}!")
                else:
                    choosenTrasnport = transports[choice - 1]
                    sorted = sort(len(choosen["location"]))
                    locations = [choosen["location"][sorted[0]], choosen["location"][sorted[1]]]
                    print(f"De acordo com as suas informações\n-O tipo de turismo escolhido é: {choosen['name']}\n-O seu transporte     será: {choosenTrasnport}\n-O trajeto que recomendamos é: {locations[0]} -> {locations[1]}")
                    print("="*100)
                    cont  = input("Deseja escolher mais uma opção de trajeto ? (S/N) ").upper()
                    if quests.validate(cont) == False:
                        alerts.error("Digite um valor válido!")
                        cont  = input("Deseja escolher mais uma opção de trajeto ? (S/N) ")
    except KeyboardInterrupt:
        pass
    finally:
        user = dict()
        with open("db/users/logged.txt", "r", encoding="utf-8") as file:
            user = json.loads(file.read())
        with open("db/users/logged.txt", "w") as file:
            file.write("")
        print(f"Obrigado por usar o pathfinder, até mais {user['username']}!")
        print("Programa encerrado!")

# função para sortear destinos de acordo com o tamanho da list
def sort(lenght):
    sorted = []
    sort1 = random.randint(0, (lenght - 1))
    sort2 = random.randint(0, (lenght - 1))
    sorted.append(sort1)
    if sorted[0] == sort2:
        while sorted[0] == sort2:
            sort2 = random.randint(0, 2)
        sorted.append(sort2)
    else:
        sorted.append(sort2)
    return sorted

# chamando a função main
main()