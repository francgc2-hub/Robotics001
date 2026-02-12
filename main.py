# Juego "Impostor" (variante Spy) - cada jugador revisa su carta en privado
import os, random, sys

PALABRAS = ["manzana","libro","reloj","perro","avión","teléfono","gato","fútbol","playa","árbol"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    try:
        n = int(input("Número de jugadores (mínimo 3): ").strip())
        if n < 3:
            print("Se necesitan al menos 3 jugadores."); return
    except:
        print("Entrada inválida."); return

    palabra = random.choice(PALABRAS)
    impostor = random.randrange(n)

    print("\nSe va a repartir. Pasa el dispositivo a cada jugador y sigue las instrucciones.\n")
    for i in range(n):
        input(f"Jugador {i+1}: pulsa Enter para ver tu carta...")
        clear()
        if i == impostor:
            print("=== ERES IMPOSTOR ===\n(No recibes la palabra; finge saberla.)")
        else:
            print(f"Palabra: {palabra}")
        input("\nPulsa Enter cuando termines y pasa el dispositivo al siguiente jugador...")
        clear()

    print("Reparto terminado. Empieza la discusión para encontrar al impostor. ¡Buena suerte!")

if __name__ == "__main__":
    main()