"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.

f
"""
from collections import Counter, OrderedDict

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    col2 = [(z[1]) for z in archivo] 
    sumc = 0   
    for z in range(len(col2)):
        sumc = int(col2[z]) + sumc    
    return sumc


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    letter = [i[0] for i in archivo]
    letter = Counter(letter)
    letter = list(letter.keys())
    letter.sort()
    col1 = [z[0] for z in archivo]
    val = [col1.count(letter[z]) for z in range(len(letter))]
    tuppla = list(zip(letter, val))
    return tuppla


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    letter = [i[0] for i in archivo]
    letter = Counter(letter)
    letter = list(letter.keys())
    letter.sort()
    total = []
    
    col12 = [(z[0], z[1]) for z in archivo]
    for j in range(5):
        suma =0
        for i in range(len(col12)):
            if col12[i][0] == letter[j]:
                suma = suma + int(col12[i][1]) # Extraer valores 
        elemento = (letter[j], suma)
        total.append(elemento)
    return total

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    fecha = [z[2] for z in archivo]
    mes = [fecha[z][5:7] for z in range(len(fecha))]
    registros = Counter(mes)
    registros = registros.items()
    registros = sorted(registros)
    
    return registros


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    letter = [z[0] for z in archivo]
    letter = Counter(letter)
    letter = list(letter.keys())
    letter.sort()
    minimo = []
    maximo =[]
    col12 = [(z[0], z[1]) for z in archivo]
    
    for i in range(len(letter)):
        total=[]
        for j in range(len(col12)):
            if col12[j][0] == letter[i]:
                val= col12[j][1]
                total.append((val))
        minimo.append(int(min(total)))
        maximo.append(int(max(total)))
    total = list(zip(letter, maximo, minimo))
    
    return total

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    clave = [z[4] for z in archivo]
    listase = [clave[z].split(",") for z in range(len(clave))]
    listafin=[[listase[i][j].split(":") for j in range(len(listase[i]))] for i in range(len(listase))]
    claves = list(Counter([z[0:3] for z in clave]).keys())
   
    a =listafin[:][0]
    for i in range(1,len(listafin)):
        b =listafin[:][i]
        a.extend(b)
    
    claves.sort()
    minimo = []
    maximo =[]
    
    for i in range(len(claves)):
        total=[]
        for j in range(len(a)):
            if a[j][0] == claves[i]:
                val= a[j][1]
                total.append((int(val)))
        minimo.append(min(total))
        maximo.append(max(total))
    total = list(zip(claves, minimo, maximo))
    
    
        
    return total


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    col2= [(int(z[1]), z[0]) for z in archivo]
    num = list(Counter([int(z[1]) for z in archivo]).keys())
    num.sort()
    letraf =[]
    for i in range(len(num)):
        letra= [col2[j][1] for j in range(len(col2)) if i == col2[j][0]]
        letraf.append(letra)

    total = list(zip(num, letraf))        
    return total

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    col2= [(int(z[1]), z[0]) for z in archivo]
    num = list(Counter([int(z[1]) for z in archivo]).keys())
    num.sort()
    letraf =[]
    for i in range(len(num)):
        letra= [col2[j][1] for j in range(len(col2)) if i == col2[j][0]]
        a=list(set(letra))
        a.sort()
        letraf.append(a)

    total = list(zip(num, letraf))
    return total


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    clave = [z[4] for z in archivo]
    listase = [clave[z].split(",") for z in range(len(clave))]
    listafin=[[listase[i][j].split(":") for j in range(len(listase[i]))] for i in range(len(listase))]
   
    a =listafin[:][0]
    for i in range(1,len(listafin)):
        b =listafin[:][i]
        a.extend(b)
    
    claves =dict(Counter([a[i][0] for i in range(len(a))]))
    
    clavesor =dict(sorted(claves.items()))  
    return clavesor

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    col1= [z[0] for z in archivo] # col1 = [ col1[i][0] for i in range(len(archivo))]
    col3= [len(z[3].split(",")) for z in archivo]
    col4= [len(z[4].split(",")) for z in archivo]
    total = [(col1[i], col3[i], col4[i]) for i in range(len(col1))]
    
    return total

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    col24= [(z[1], z[3].split(",")) for z in archivo] 
    
    col4= [z[3].split(",") for z in archivo]
    a =col4[:][0]
    for i in range(1,len(col4)):
        b =col4[:][i]
        a.extend(b)
    letras =sorted(Counter(a).keys())
    zeros = [ 0 for _ in letras]
    dic = dict(zip(letras, zeros))
       
    for i in range(len(col24)):
        for j in col24[i][1]:
            for l in letras: 
                if j == l:
                    dic[l]= dic[l]+int(col24[i][0])
        
    ##### extraer el numero col24[i][0]
    #print(col4)
       
        # print(b)
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    archivo = open("data.csv", "r").readlines()
    archivo = [z.replace("\n", "") for z in archivo]
    archivo = [z.split() for z in archivo]
    letter = [z[0] for z in archivo]
    col1 = [z[0] for z in archivo]
    letter = Counter(letter)
    letter = list(letter.keys())
    letter.sort()
    zeros = [ 0 for _ in letter]
    dic = dict(zip(letter, zeros))
    clave = [z[4].replace(":", ",").split(",") for z in archivo]
    k=0
    for i in clave:
        suma = 0
        for j in i[1::2]:
            suma = suma + int(j)
        for l in letter:
            if col1[k] == l:
                dic[l]= dic[l]+int(suma)     
        k =k+1    
    return dic

# Prueba git 