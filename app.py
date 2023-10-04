import places
import menu

# list que guarda todas as opções de roteiros
choices = []

def main():
    # alimentando a list de roteiros
    choices = places.get()

    # chamando a função de menu
    menu.start()

main()