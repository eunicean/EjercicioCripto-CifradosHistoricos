from collections import Counter
from tabulate import tabulate
from cifrados import cesarCifrado, cesarDesifrado, rot13, vigenereCifrado, vigenereDescifrado

def analisis_frecuencia(mensaje):
    contador = Counter(mensaje)
    total = sum(contador.values())
    tabla = []
    tabla.append(("Letra", "#", "Porcentaje"))
    # ordenar por cuenta descendente y luego por caracter para estabilidad
    for ch in sorted(contador, key=lambda x: (-contador[x], x)):
        cuenta = contador[ch]
        porcentaje = (cuenta / total) * 100 if total > 0 else 0.0
        tabla.append((ch, cuenta, porcentaje))
    return tabla

def tablaAnalisisCifrados():
    msg = "MI EJERCICIO DE CRIPTO"
    clave = "SEGURIDAD"
    desplazamiento = 10

    cifrado_vig = vigenereCifrado(msg, clave)
    # descifrado_vig = vigenereDescifrado(cifrado_vig, clave)
    cif_cesar = cesarCifrado(msg, desplazamiento)
    # desc_cesar = cesarDesifrado("def ABC", desplazamiento)
    rot = rot13(msg)

    freq_mensaje = []

    freq_mensaje.append(("Mensaje normal", analisis_frecuencia(msg), msg))
    freq_mensaje.append(("Cifrado Cesar", analisis_frecuencia(cif_cesar), cif_cesar))
    freq_mensaje.append(("ROT13", analisis_frecuencia(rot), rot))
    freq_mensaje.append(("Cifrado Vigenère", analisis_frecuencia(cifrado_vig), cifrado_vig))

    for cifrado in freq_mensaje:
        print("="*35)
        print(f" {cifrado[0]}".center(35))
        print("="*35)

        print(f" - Mensaje: {cifrado[2]}")

        print(tabulate(cifrado[1][1:], headers=cifrado[1][0], tablefmt="grid"))


# Frecuencias


# for register in freq_mensaje:
#     print(f"Caracter: {register[0]}\n  - Cantidad de aparciciones: {register[1]}\n  - Porcentaje de aparición: {register[2]:.2f}")

# print(tabulate(freq_mensaje[1:], headers=freq_mensaje[0], tablefmt="grid"))

tablaAnalisisCifrados()