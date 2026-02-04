# ------------------------
# Cifrado cesar
# ------------------------
def cesarCifrado(mensaje, desplazamiento):
    alfabeto_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alfabeto_minus = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for caracter in mensaje:
        if caracter in alfabeto_mayus:
            posicion = alfabeto_mayus.index(caracter)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += alfabeto_mayus[nueva_posicion]

        elif caracter in alfabeto_minus:
            posicion = alfabeto_minus.index(caracter)
            nueva_posicion = (posicion + desplazamiento) % 26
            resultado += alfabeto_minus[nueva_posicion]

        else:
            resultado += caracter

    return resultado

def cesarDesifrado(cifrado, desplazamiento):
    return cesarCifrado(cifrado, -desplazamiento)

def cesarFuerzaBruta(mensaje):
    for i in range(26): # solo para mensajes con letras
        resultado = cesarCifrado(mensaje,i)
        print(f"Intento {i}: {cesarCifrado(mensaje, i)}")

# ------------------------
# Cifrado ROT13
# ------------------------
def rot13(mensaje):
    # ROT13 es César con desplazamiento 13
    return cesarCifrado(mensaje, 13)

# ------------------------
# Cifrado Vigenere
# ------------------------
def vigenereCifrado(mensaje, llave):
    key = list(llave)
    if len(mensaje) == len(key):
        return key
    else:
        for i in range(len(mensaje) - len(key)):
            key.append(key[i % len(key)])
    clave_limpia = "".join(key)

    if len(clave_limpia) == 0: return mensaje

    encrypted_text = []

    for i in range(len(mensaje)):
        char = mensaje[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def vigenereDescifrado(mensaje, llave): 
    key = list(llave)
    if len(mensaje) == len(key):
        return key
    else:
        for i in range(len(mensaje) - len(key)):
            key.append(key[i % len(key)])
    clave_limpia = "".join(key)

    if len(clave_limpia) == 0: return mensaje

    decrypted_text = []
    for i in range(len(mensaje)):
        char = mensaje[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)
# lógica de https://www.geeksforgeeks.org/dsa/vigenere-cipher/


# mensaje = "krnwenwrmxb j lroajmxb"

# print(cesarCifrado(mensaje, 17))

# print(cesarFuerzaBruta(mensaje))

# mensaje = "MI EJERCICIO de CIFRADO HISTORICO"
# llave = "CLAVE"

# print(vigenereCifrado(mensaje, llave))
# print(vigenereDescifrado(vigenereCifrado(mensaje, llave), llave))

