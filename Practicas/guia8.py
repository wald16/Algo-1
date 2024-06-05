from numpy import *
from queue import LifoQueue as Pila


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


def flush_pila(pila: Pila) -> list:
    res = []
    while not pila.empty():
        res.append(pila.get())
    return res


def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila_nums = Pila()
    for i in range(cantidad):
        num = random.randint(desde, hasta)
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

    return flush_pila(p)


# EJ 10
def buscar_el_maximo(p: Pila[int]) -> int:
    pila2 = Pila()
    while not p.empty():
        pila2.put(p.get())

    maximo = pila2.get()
    while not pila2.empty():
        num = pila2.get()
        if maximo < num:
            maximo = num

    while not pila2.empty():
        p.put(pila2.get())

    return maximo


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
# print(flush_pila(generar_nros_al_azar(cant, desde, hasta)))
# print(cantidad_elementos(save_random))
# print(flush_pila(save_random))
print(buscar_el_maximo(pilaej))
