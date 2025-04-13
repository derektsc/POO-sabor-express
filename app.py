from models.restaurant import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Derek', 8)
restaurante_praca.receber_avaliacao('Teste', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()