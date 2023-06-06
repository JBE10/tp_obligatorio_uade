def cal_tiempo(t_t, c_v):
    hora_prom = []
    dias_horas_prom = []

    for i in range(len(t_t)):
        auxiliar = t_t[i] // c_v[i]
        hora_prom.append(auxiliar)

    for i in hora_prom:
        dias = i // 24
        horas = i % 24
        dias_horas_prom.append([dias, "d", horas, "h"])

    return dias_horas_prom


def ingreso_de_datos(camiones, distancia, toneladas, horas, cantidad, a, b, c, d):
    encontrar = False
    i = 0
    while i < len(camiones):
        if camiones[i] == a:
            distancia[i] += b
            toneladas[i] += c
            horas[i] += d
            cantidad[i] += 1
            encontrar = True
            break
        else:
            i += 1

    if not encontrar:
        camiones.append(a)
        distancia.append(b)
        toneladas.append(c)
        horas.append(d)
        cantidad.append(1)

    hora_prom = cal_tiempo(horas, cantidad)

    lista_total = [camiones, distancia, toneladas, hora_prom]

    return lista_total


def orden_lista(a, b, c, d):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
                c[i], c[j] = c[j], c[i]
                d[i], d[j] = d[j], d[i]

    lista = [a, b, c, d]
    return lista


lista_camiones = []
lista_distancias = []
lista_toneladas = []
lista_horas = []

camiones = []
distancia = []
toneladas = []
horas = []
cantidad = []

camion = int(input("Ingrese número del camión: "))
while camion != -1:
    if camion < 0:
        print("Datos inválidos, introducir datos positivos")
    else:
        horas_manejadas = int(input("Ingrese número de horas manejadas: "))
        distancia_recorrida = int(input("Ingrese distancia: "))
        toneladas_transportadas = int(
            input("Ingrese cantidad de toneladas transportadas: ")
        )
        lista = ingreso_de_datos(
            camiones,
            distancia,
            toneladas,
            horas,
            cantidad,
            camion,
            distancia_recorrida,
            toneladas_transportadas,
            horas_manejadas,
        )
        lista_camiones = lista[0]
        lista_distancias = lista[1]
        lista_toneladas = lista[2]
        lista_horas = lista[3]

    camion = int(input("Ingrese número del camión: "))

if len(lista_camiones) > 1:
    lista = orden_lista(lista_camiones, lista_distancias, lista_toneladas, lista_horas)
    lista_camiones = lista[0]
    lista_distancias = lista[1]
    lista_toneladas = lista[2]
    lista_horas = lista[3]

print("===============================================================================")
print("N-Camiones-------Tiempo Promedio--------------Distancia Total-------Carga Total")
print("===============================================================================")

for i in range(len(lista_camiones)):
    if lista_distancias[i] > 20000:
        print(
            "|   ",
            lista_camiones[i],
            "      ",
            lista_horas[i],
            "           ",
            lista_distancias[i],
            "Km",
            "                 ",
            lista_toneladas[i],
            "Tn",
            "  | Revisión mecánica",
        )
        print()
    else:
        print(
            "|   ",
            lista_camiones[i],
            "      ",
            lista_horas[i],
            "           ",
            lista_distancias[i],
            "Km",
            "                 ",
            lista_toneladas[i],
            "Tn",
            "  |",
        )
        print()
