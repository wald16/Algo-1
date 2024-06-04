import numpy as np


# EJ 1
def pertenece(lista: list, elem: int) -> bool:
    return elem in lista


def divide_a_todos(lista: list, elem: int) -> bool:
    for i in range(len(lista)):
        if lista[i] % elem != 0:
            return False
    return True


def suma_total(lista: list) -> int:
    total = 0
    for elemento in lista:
        total += elemento
    return total


def ordenados(lista: list) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def long7(listapalabras: list) -> bool:
    for i in range(len(listapalabras)):
        if len(listapalabras[i]) > 7:
            return True
    return False


def palindromo(texto: str) -> str:
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


def contraseña(contra: str) -> str:
    if len(contra) < 5:
        return "ROJA"
    elif (
        len(contra) > 8
        and any(c.islower() for c in contra)
        and any(c.isupper() for c in contra)
        and any(c.isdigit() for c in contra)
    ):
        return "VERDE"
    else:
        return "AMARILLA"


def banco(listatuplas: list) -> int:
    total = 0
    for tupla in listatuplas:
        if tupla[0] == "I":
            total += tupla[1]
        else:
            total -= tupla[1]
    return total


def vocals(palabra: str) -> bool:
    palabra = palabra.lower()
    vocales = set()
    for letra in palabra:
        if letra in "aeiou":
            vocales.add(letra)
    if len(vocales) >= 3:
        return True
    return False


# -------------------------------------------------------------------------------------------
# EJ 2
def ceroenpar(listanum: list) -> list:
    for i in range(len(listanum)):
        if (i + 1) % 2 == 0:
            listanum[i] = 0
    return listanum


def ceroenpar_nueva(listanum: list) -> list:
    nueva_lista = [0 if (i + 1) % 2 == 0 else num for i, num in enumerate(listanum)]
    return nueva_lista


def cadenasinvocales(cadena: str) -> str:
    nueva_cadena = ""
    for letra in cadena:
        if letra.lower() not in "aeiou":
            nueva_cadena += letra
    return nueva_cadena


def reemplaza_vocales(palabra: str) -> str:
    nueva_palabra = ""
    for letra in palabra:
        if letra.lower() in "aeiou":
            nueva_palabra += "_"
        else:
            nueva_palabra += letra
    return nueva_palabra


def da_vuelta_str(palabra: str) -> str:
    nueva_palabra = ""
    for i in range(len(palabra)):
        nueva_palabra += palabra[len(palabra) - i - 1]
    return nueva_palabra


def eliminar_repetidos(palabra: str) -> str:
    nueva_palabra = ""
    for letra in palabra:
        if letra not in nueva_palabra:
            nueva_palabra += letra
    return nueva_palabra


# -----------------------------------------------------------------------------------------------------------------------
# EJ 3
def aprobado(notas: list) -> int:
    for nota in notas:
        if nota >= 4 and (suma_total(notas) / len(notas)) >= 7:
            return "1"
        elif (
            nota >= 4
            and (suma_total(notas) / len(notas)) >= 4
            and (suma_total(notas) / len(notas)) < 7
        ):
            return "2"
        elif nota < 4 or (suma_total(notas) / len(notas)) < 4:
            return "3"


# -------------------------------------------------------------------------------------------------------------------------------------
# EJ 4
def nombres() -> list:
    nombres = []
    while True:
        nombre = input("Ingrese nombres('listo' termina el programa)")
        if nombre == "listo":
            break
        nombres.append(nombre)
    return nombres


def monedero() -> list:
    lista = []
    while True:
        letra = input("""Ingrese:
                  "C" para cargar creditos
                  "D" para descontar creditos
                  "X" para finalizar
                  -> """)
        if letra == "X":
            print(lista)
            break
        elif letra == "C":
            creditos = input("Ingrese los creditos a cargar ->  ")
            lista.append((letra, creditos))
        elif letra == "D":
            creditos = input("Ingrese los creditos a descontar ->  ")
            lista.append((letra, creditos))


def checkifpierde(num: int) -> bool:
    if num > 7.5:
        return True
    return False


def repartir() -> int:
    carta = 8
    while carta == 8 or carta == 9:
        carta = np.random.randint(1, 12)
    return carta


def medio(num: float) -> float:
    a = [10, 11, 12]
    if num in a:
        return 0.5
    return num


def simulacion() -> list:
    lista = []
    entrada = ""
    usuario: float = 0

    carta: float = medio(repartir())
    print(f"Tu carta es {carta}")
    lista.append(carta)
    while entrada != "q":
        print("Desea pedir (p) o quedarse (q)?")
        entrada = input("-> ")
        if entrada == "p":
            carta = medio(repartir())
            print(f"Sacaste un: {carta}")
            lista.append(carta)
            usuario = suma_total(lista)
            if usuario > 7.5:
                print(f"Perdiste nashe, sumaste {usuario}")
                print(f"Lista de cartas obtenidas: {lista}")
                break
        elif entrada == "q":
            usuario = suma_total(lista)
            print(f"Te quedaste en {usuario}")
            print(f"Lista de cartas obtenidas: {lista}")
    return lista


def pertenece_a_cada_uno_version_1(lista, numero, res):
    for i in range(len(lista)):
        if pertenece(lista[i], numero):
            res.append(True)
        else:
            res.append(False)
    return res


# def pertenece_a_cada_uno_version_2(lista, numero, res):


def es_matriz(lista) -> bool:
    if len(lista) > 0 and len(lista[0]) > 0:
        for i in range(len(lista)):
            if len(lista[i]) != len(lista[0]):
                return False
        return True


def filas_ordenadas(lista, res):
    for i in range(len(lista)):
        if ordenados(lista[i]):
            res.append(True)
        else:
            res.append(False)
    return res


# --------------------------------------------------------------------------------------------------------------------
def transponer(matrix):
    res = []
    for i in range(len(matrix[0])):
        columna = []
        for fila in matrix:
            columna.append(fila[i])
        res.append(columna)
    return res


def matrix_mult(i, j):
    pass


listapalabras = ["hola", "chau", "nasheeeeee"]
lista = [1, 2, 4, 6]
listaListas = [[1, 4, 3], [2, 1, 2], [3, 2, 1]]
elem = 1
texto = "alas"
contra = "Nashee7"
listatuplas = [("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]
palabra = "nashe"
listanum = [4, 9, 9, 10]
res = []
# print(pertenece(lista, elem))
# print(divide_a_todos(lista, elem))
# print(suma_total(lista))
# print(ordenados(lista))
# print(long7(listapalabras))
# print(palindromo(texto))
# print(contraseña(contra))
# print(banco(listatuplas))
# print(vocals(palabra))
# print(ceroenpar(listanum))
# print(cadenasinvocales(palabra))
# print(reemplaza_vocales(palabra))
# print(da_vuelta_str(palabra))
# print(eliminar_repetidos(palabra))
# print(aprobado(listanum))
# print(nombres())
# print(monedero())
# print(simulacion())
# print(pertenece_a_cada_uno_version_1(listaListas, elem, res))
# print(es_matriz(listaListas))
# print(filas_ordenadas(listaListas, res))
print(transponer(listaListas))
