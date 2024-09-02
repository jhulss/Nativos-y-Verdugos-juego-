from AgenteMapu import AgenteMapu
from Rio import Rio

if __name__ == "__main__":
    juego = Rio()
    juan = AgenteMapu()
    juego.insertar(juan)
    juego.run()
