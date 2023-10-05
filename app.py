import menu

# função para iniciar o programa
def main():
    try:
        # chamando a função de menu
        menu.start()
    except KeyboardInterrupt:
        pass
    finally:
        print("Programa encerrado!")

# chamando a função main
main()