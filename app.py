import places
import menu
import alerts
import json
import random

# list que guarda todas as opções de roteiros
choices = []
choosen = dict()
transports = []
choosenTrasnport = ""

def main():
    try:

        # chamando a função de menu
        # menu.start()
        # alimentando a list de roteiros
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
                choosenTrasnport = transports[choice - 1]
                if choice < 1 or choice > len(transports):
                    alerts.error(f"Escolha uma opção de 1 a {len(transports)}!")
                print(sort(len(choosen["location"])))
                
            

    except KeyboardInterrupt:
        pass
    finally:
        print("Programa encerrado!")

def sort(lenght):
    sorted = []
    sort1 = random.randint(0, lenght)
    sort2 = random.randint(0, lenght)
    sorted.append(sort1)
    if sorted[0] == sort2:
        while sorted[0] == sort2:
            sort2 = random.randint(0, 2)
        sorted.append(sort2)
    else:
        sorted.append(sort2)
    return sorted


main()