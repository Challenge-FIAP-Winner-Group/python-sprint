import random
import re

user_data = dict(stop = False)
choices = {
    1: {"name": "Cultural", "types": "Museus, galerias de arte, teatros e outros locais para conhecer a história e a cultura da cidade.", "location": ["MASP", "Pinacoteca", "Theatro de São Paulo"]},
    2: {"name": "Histórico", "types": "Monumentos, prédios antigos, sítios arqueológicos e outros locais para aprender sobre a história da cidade.", "location": ["Pátio do Colégio", "Museu do Ipiranga", "Mosteiro de São Bento"]},
    3: {"name": "Ambiental", "types": "Parques, reservas naturais, trilhas ecológicas e outros locais para apreciar a natureza e os ecossistemas da cidade.", "location": ["Parque do Ibirapuera", "Jardim Botânico de São Paulo", "Horto Florestal"]},
    4: {"name": "Comercial", "types": "Shoppings, feiras, lojas de artesanato e outros locais para comprar produtos típicos da cidade.", "location": ["Rua 25 de Março", "Galeria do Rock", "Shopping Iguatemi"]},
    5: {"name": "Gastronômico", "types": "Restaurantes, mercados e feiras para experimentar a culinária local.", "location": ["Fábrica da Bauducco", "Restaurante Figueira Rubaiyat", "Feira da Liberdade"]},
    6: {"name": "Esportivo", "types": "Arenas esportivas, estádios e outros locais para assistir ou praticar esportes na cidade.", "location": ["Estádio do Morumbi", "Museu do Futebol", "Allianz Parque"]},
}
transport = ["Uber", "Metrô", "Ônibus", "A pé"]

def main():
    try:
        print("\n"+("=" * 45) + "PathFinder" + ("=" * 45))
        print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
        name = input()
        if len(name) == 0 or re.search("\d", name): 
            raise ValueError
        user_data.update({"name": name})
        print(f"Olá, {user_data['name']}!")
        print("="*100)
        while user_data["stop"] == False:
            try:
                menu()
                typeTransport()
                end()
            except ValueError: 
                error(1)
            except KeyError:
                error(2)
    except ValueError:
        error(1)
    except KeyError:
        error(2)
    except KeyboardInterrupt:
        pass
    finally: 
        exit()    

def menu(): 
    print("\nEscolha uma opção:")
    for i in choices:
        print(f"({i}) {choices[i]['name']} -> {choices[i]['types']}")
    choice = int(input())
    if choice > 6 or choice < 1:
        raise KeyError
    user_data.update({"choice": choices[choice]['name']})
    length = len(choices[choice]["location"]) - 1
    user_data.update({ "locations": choose(choice, length) })

def sort(length):
    sorted = []
    sort1 = random.randint(0, length)
    sort2 = random.randint(0, length)
    sorted.append(sort1)
    if sorted[0] == sort2:
        while sorted[0] == sort2:
            sort2 = random.randint(0, 2)
        sorted.append(sort2)
    else:
        sorted.append(sort2)
    return sorted

def choose(choice, length):
    sorted = sort(length)
    loc1 = choices[choice]["location"][sorted[0]]
    loc2 = choices[choice]["location"][sorted[1]]
    return [loc1, loc2]
    
def typeTransport():
    print("\nDe qual forma você pretende chegar ao destino?")
    for i in range(len(transport)):
        print(f"({i+1}) {transport[int(i)]}")
    choice = int(input())
    if choice < 1 or choice > 4:
        raise KeyError
    user_data.update({"transport": transport[choice-1]})

def end(): 
    print("\n"+("=" * 45) + "Resultado" + ("=" * 46))
    print(f"De acordo com as suas informações\n-O tipo de turismo escolhido é: {user_data['choice']}\n-O seu transporte será: {user_data['transport']}\n-O trajeto que recomendamos é: {user_data['locations'][0]} -> {user_data['locations'][1]}")
    print("="*100)
    print("Desenja escolher mais uma opção de trajeto ? (S/N)")
    stop = input()
    if stop.lower() == "n":
        print(f"Obrigado por usar o Path Finder {user_data['name']}!")
        user_data["stop"] = True

def exit(): 
    print("\nPrograma encerrado.")

def error(value):
    print("="*100)
    match value:
        case 1:
            print("<ERROR> Digite um valor válido!")
        case 2:
            print("<ERROR> Essa opção não existe!")
    print("="*100)
        
main()