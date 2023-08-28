import random

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
        print("Bem vindo ao PathFinder!\nDigite o seu nome: ")
        name = input()
        if len(name) == 0: 
            print("<ERROR> Digite um nome!")
            raise ValueError
        user_data.update({"name": name})
        print(f"Olá, {user_data['name']}!")
        print("="*100)
        while user_data["stop"] == False:
            menu()
    except ValueError:
        exit()

def menu(): 
    print("\nEscolha uma opção?")
    for i in choices:
        print(f"({i}) {choices[i]['name']} -> {choices[i]['types']}")
    choice = int(input())
    if choice > 6 and choice < 1:
        print("<ERROR> Escolha uma opção válida, escolha uma opção entre 1 e 6!")
        raise ValueError
    user_data.update({"choice": choices[choice]['name']})
    match choice:
        case 1: user_data.update({ "locations": cultural() })
        case 2: user_data.update({ "locations": historic() })
        case 3: user_data.update({ "locations": environmental() })
        case 4: user_data.update({ "locations": commercial() }) 
        case 5: user_data.update({ "locations": gastronomic() }) 
        case 6: user_data.update({ "locations": sportive() }) 

def sort():
    sorted = []
    sort1 = random.randint(0, 2)
    sort2 = random.randint(0, 2)
    sorted.append(sort1)
    if sorted[0] == sort2:
        while sorted[0] == sort2:
            sort2 = random.randint(0, 2)
        sorted.append(sort2)
    else:
        sorted.append(sort2)
    return sorted

def cultural():
    sorted = sort()
    loc1 = choices[1]["location"][sorted[0]]
    loc2 = choices[1]["location"][sorted[1]]
    return [loc1, loc2]

def historic():
    sorted = sort()
    loc1 = choices[2]["location"][sorted[0]]
    loc2 = choices[2]["location"][sorted[1]]
    return [loc1, loc2]

def environmental():
    sorted = sort()
    loc1 = choices[3]["location"][sorted[0]]
    loc2 = choices[3]["location"][sorted[1]]
    return [loc1, loc2]

def commercial():
    sorted = sort()
    loc1 = choices[4]["location"][sorted[0]]
    loc2 = choices[4]["location"][sorted[1]]
    return [loc1, loc2]

def gastronomic():
    sorted = sort()
    loc1 = choices[5]["location"][sorted[0]]
    loc2 = choices[5]["location"][sorted[1]]
    return [loc1, loc2]

def sportive():
    sorted = sort()
    loc1 = choices[6]["location"][sorted[0]]
    loc2 = choices[6]["location"][sorted[1]]
    return [loc1, loc2]
    
def typeTransport():
    print("De qual forma você pretende chegar ao destino?")
    for i in transport:
        print(f"({i}) {transport[i]}")
    choice = int(input())
    if choice < 1 and choice > 4:
        print("<ERROR> Escolha uma opção válida, escolha uma opção entre 1 e 4!")
        raise ValueError
    user_data.update({"transport": transport[choice]})

def end(): 
    print(f"De acordo com as suas informações\n-O tipo de turismo escolhido é: {user_data['choice']}\n-O seu transporte será: {user_data['transport']}\n-O trajeto que recomendamos é: {user_data['locations'][0]} -> {user_data['locations'][0]}")
    print("="*100)
    print("Desenja encerrar o programa ? (S/N)")
    stop = input()
    if stop.lower() == "s":
        user_data["stop"] = True

def exit(): 
    print("\nPrograma encerrado.")

main()