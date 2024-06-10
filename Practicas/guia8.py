from numpy import *  # noqa: F403
from queue import LifoQueue as Pila
from queue import Queue as Cola


def maximo(lista: list) -> int:
    max = lista[0]
    for elem in lista:
        if max < elem:
            max = elem
    return max


# EJ 1
def contar_lineas(nombre: str) -> int:
    lineas = 0
    with open(nombre, "r") as f:
        for line in f:
            lineas += 1
        return lineas


def existe_palabra(palabra: str, nombre: str) -> bool:
    with open(nombre, "r") as f:
        for line in f:
            if palabra in line:
                return True
        return False


def cantidad_apariciones(nombre: str, palabra: str) -> int:
    res = 0
    with open(nombre, "r") as f:
        for line in f:
            if palabra in line:
                res += 1
        return res


# EJ 2
def es_comment(linea: str) -> bool:
    for i in linea:
        if i != " ":
            if i == "#":
                return True
            pass
    return False


def clonarSinComentarios(nombre: str):
    with open(nombre) as f:
        nuevo = []
        for i in f.readlines():
            if not es_comment(i):
                nuevo.append(i)
    with open(f"clon_{nombre}", "w") as g:
        g.writelines(nuevo)
    return "LISTO NASHE"


# EJ 3
def invertir_lineas(nombre: str):
    with open(nombre) as f:
        lineas = f.readlines()
    reversed = lineas[::-1]
    with open(f"reversed_{nombre}", "w") as g:
        g.writelines(reversed)
    return "LISTO NASHE"


# EJ 4
def agregar_frase_al_final(nombre: str, frase: str):
    with open(nombre, "a") as f:
        f.write(frase + "\n")


# EJ 5
def agregar_frase_al_principio(nombre: str, frase: str):
    with open(nombre, "r+") as f:
        lineas = f.read()
        f.seek(0)
        f.write(frase + "\n" + lineas)


# EJ 6
def listar_palabras_de_archivo(nombre: str) -> list:
    with open(nombre, "rb") as f:
        contenidob = f.read()
        contenido = contenidob.decode("utf-8")
        res = []
        for palabra in contenido.split():
            if palabra.isalnum() and len(palabra) >= 5:
                res.append(palabra)
        return res


# Ej 7
def calcular_promedio_por_estudiante(archivo_notas: str, archivo_promedios: str):
    with open(archivo_notas, "r") as f:
        contenido = f.readline().strip().split(",")
        num = contenido[0]
    promedio = promedio_estudiante(archivo_notas, num)
    with open(archivo_promedios, "a") as g:
        linea = f"{num}, {promedio}"
        g.write(linea)


def promedio_estudiante(archivo: str, lu: str) -> float:
    with open(archivo, "r") as f:
        contenido = f.readlines()
        notas = []
        for fila in contenido:
            valores = fila.strip().split(",")
            if len(valores) == 4:
                nro, materia, fecha, nota_str = valores
                nota = float(nota_str)
                if nro == lu:
                    notas.append(nota)
        if notas:
            promedio = sum(notas) / len(notas)
            return promedio
        else:
            return 0.0


# EJ 8


def pila_a_lista(pila: Pila) -> list:
    res = []
    while not pila.empty():
        res.append(pila.get())
    for i in res[::-1]:
        pila.put(i)
    return res


def cola_a_lista(cola: Cola) -> list:
    res = []
    while not cola.empty():
        res.append(cola.get())
    for i in res:
        cola.put(i)
    return res


def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila_nums = Pila()
    for i in range(cantidad):
        num = random.randint(desde, hasta)  # noqa: F405
        pila_nums.put(num)
    return pila_nums


# EJ 9
def cantidad_elementos(p: Pila[int]) -> int:
    pila2 = Pila()
    res = 0
    while not p.empty():
        pila2.put(p.get())
        res += 1
    while not pila2.empty():
        p.put(pila2.get())

    return pila_a_lista(p)


# EJ 10
def buscar_el_maximo(p: Pila[int]) -> int:
    elementos = []
    while not p.empty():
        elemento = p.get()
        elementos.append(elemento)
    maxi = maximo(elementos)
    for elem in elementos:
        p.put(elem)
    return maxi


# EJ 11
def esta_bien_balanceada(s: str) -> bool:
    parentesis = []
    for char in s:
        if char == "(":
            parentesis.append(char)
        elif char == ")":
            if not parentesis:
                return False
            else:
                parentesis.pop()
    return True


# EJ 12
def evaluar_expresion(s: str) -> float:
    p = Pila()
    for elem in s.split():
        if elem not in "+-*/":
            p.put(float(elem))
        else:
            oper2 = p.get()
            oper1 = p.get()
            if elem == "+":
                result = oper1 + oper2
            elif elem == "-":
                result = oper1 - oper2
            elif elem == "*":
                result = oper1 * oper2
            elif elem == "/":
                result = oper1 / oper2
            p.put(result)
    return pila_a_lista(p)


# EJ 13
def generar_nros_al_azar2(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()
    for i in range(cantidad):
        num = random.randint(desde, hasta)  # noqa: F405
        c.put(num)
    return pila_a_lista(c)


# EJ 14
def cantidad_elementos2(c: Cola) -> int:
    lista = []
    res = 0
    while not c.empty():
        lista.append(c.get())
        res += 1
    for i in lista:
        c.put(i)
    return res


# EJ 15
def buscar_el_maximo2(c: Cola[int]) -> int:
    elementos: list = []
    while not c.empty():
        elemento = c.get()
        elementos.append(elemento)
    maxi = maximo(elementos)
    for elem in elementos:
        c.put(elem)
    return maxi


# EJ 16
def armar_secuencia_de_bingo() -> Cola[int]:
    cola: Cola[int] = Cola()
    while cantidad_elementos2(cola) < 100:
        num: int = random.randint(0, 100)  # noqa: F405
        if num not in cola_a_lista(cola):
            cola.put(num)
    return cola


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    numsllenos: int = 0
    cantjugadas: int = 0
    while numsllenos < 12:
        numobtenido = bolillero.get()
        if numobtenido in carton:
            numsllenos += 1
        cantjugadas += 1
    return cantjugadas


# EJ 17
def n_parcientes_urgentes(c: Cola[(int, str, str)]) -> str:
    lista: list = cola_a_lista(c)
    res: int = 0
    for num, _, _ in lista:
        if "1" in str(num) or "2" in str(num) or "3" in str(num):
            res += 1
    return res


# EJ 18
def atencion_a_clientes(
    c: Cola[(str, int, bool, bool)],
) -> Cola[(str, int, bool, bool)]:
    prio: list[(str, int, bool, bool)] = []
    prefer: list[(str, int, bool, bool)] = []
    demas: list[(str, int, bool, bool)] = []
    res: Cola[(str, int, bool, bool)] = Cola()
    lista: list[(str, int, bool, bool)] = cola_a_lista(c)
    for nom, dni, pref, prioridad in lista:
        if prioridad:
            prio.append((nom, dni, pref, prioridad))
        elif pref:
            prefer.append((nom, dni, pref, prioridad))
        else:
            demas.append((nom, dni, pref, prioridad))
    res.put(prio)
    res.put(prefer)
    res.put(demas)
    return res


# --------------------------------------------------------------------------------
# EJ 19


def contar(lista: list[int], num: int) -> int:
    res: int = 0
    for elem in lista:
        if elem == num:
            res += 1
    return res


def agrupar_por_longitud(nombre: str) -> dict:
    tuple_list: list[(int, int)] = []
    list_longitudes: list[int] = []
    with open(nombre, "r") as f:
        palabra: str = ""
        letra = f.read(1)

        while letra:
            if letra != " " and letra != "\n":
                palabra += letra
            else:
                if palabra:
                    list_longitudes.append(len(palabra))
                    palabra = ""
            letra = f.read(1)
    list_longitudes.append(len(palabra))
    for i in list_longitudes:
        tuple_list.append((i, contar(list_longitudes, i)))
    return dict(tuple_list)


# EJ 20
def calcular_promedio_por_estudiante2(nombre: str) -> dict[str, float]:
    lista: list[(str, float)] = []
    numero: str = ""
    with open(nombre, "r") as f:
        lines = f.readlines()
        for line in lines:
            for char in line:
                if char == ",":
                    lista.append((numero, promedio_estudiante(nombre, numero)))
                    numero = ""
                    break
                numero += char

    return dict(lista)


# EJ 21
def la_palabra_mas_frecuente(nombre: str) -> str:
    dic: dict = {}
    with open(nombre, "r") as f:
        palabra: str = ""
        for letra in f.read():
            if letra != " " and letra != "\n":
                palabra += letra
            else:
                if palabra:
                    if palabra in dic:
                        dic[palabra] += 1
                    else:
                        dic[palabra] = 1
                    palabra = ""
        if palabra:
            if palabra in dic:
                dic[palabra] += 1
            else:
                dic[palabra] = 1
    maximo: int = 0
    res: str = ""
    for key, value in dic.items():
        if maximo < value:
            maximo = value
            res = key

    return res


nombre = "file"
palabra = "nashe"
archivo_notas = "archivo_notas.csv"
archivo_promedios = "archivo_promedios.csv"
lu = "350"
desde = 1
hasta = 100
cant = 3
save_random = generar_nros_al_azar(5, 0, 10)
pilaej = Pila()
pilaej.put(10)
pilaej.put(20)
pilaej.put(30)
colaej = Cola()
colaej.put(10)
colaej.put(20)
colaej.put(30)
formula = "10 * ( 1 + ( 2 * ( =1)))"
expresion = "3 4 + 5 * 2 -"
pacientes = Cola()
pacientes.put((2, "j", "k"))
pacientes.put((1, "a", "b"))
pacientes.put((6, "f", "k"))
carton: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
bolillero = armar_secuencia_de_bingo()
clientes = Cola()
clientes.put(("Manuel Wald", "4", True, False))
clientes.put(("Manuel W", "3", False, True))
clientes.put(("Manuel", "2", True, True))
clientes.put(("Man", "1", False, False))
dic = "diccionario"


# print(pila_a_lista(pilaej))
# print(contar_lineas(nombre))
# print(existe_palabra(palabra, nombre))
# print(cantidad_apariciones(nombre, palabra))
# print(clonarSinComentarios(nombre))
# print(invertir_lineas(nombre))
# print(agregar_frase_al_final(nombre, palabra))
# print(agregar_frase_al_principio(nombre, palabra))
# print(listar_palabras_de_archivo(nombre))
# print(promedio_estudiante(archivo_notas, lu))
# print(calcular_promedio_por_estudiante(archivo_notas, archivo_promedios))
# print(pila_a_lista(generar_nros_al_azar(cant, desde, hasta)))
# print(cantidad_elementos(save_random))
# print(pila_a_lista(save_random))
# print(buscar_el_maximo(pilaej))
# print(esta_bien_balanceada(formula))
# print(evaluar_expresion(expresion))
# print(generar_nros_al_azar2(cant, desde, hasta))
# print(cantidad_elementos2(colaej))
# print(buscar_el_maximo2(colaej))
# print(armar_secuencia_de_bingo())
# print(carton)
# print(cola_a_lista(bolillero))
# print(jugar_carton_de_bingo(carton, bolillero))
# print(n_parcientes_urgentes(pacientes))
# print(atencion_a_clientes(clientes))
# print(agrupar_por_longitud(dic))
# print(calcular_promedio_por_estudiante2(archivo_notas))
print(la_palabra_mas_frecuente(dic))
