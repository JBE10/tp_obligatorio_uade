# def que sirve para promediar la cantidad de  tiempo cada camion, t_t=tiempo total c_v=cantidad de viajes hechos por ese numero de camion
# lo primero que se hace es sacar el promedio en horas es decir que los datos recibidos dividido a la cantiad de viajes
# luego esas horas se dividen por 24 ya que 24 horas=un dia y luego se utiliza la funcion resto(%) para sacar las horas que quedan
# luego se devuelve la lista dias y horas ya promediada
def cal_tiempo(t_t, c_v):
    hora_prom = []
    dias_p = []
    horas_p = []

    axuliar = 0

    for i in range(len(t_t)):
        axuliar = t_t[i] // c_v[i]
        hora_prom.append(axuliar)

    for i in range(len(hora_prom)):
        dias_p.append(hora_prom[i] // 24)
        horas_p.append(hora_prom[i] % 24)

    lista_total = [dias_p, horas_p]

    return lista_total


def ordenar_lista_insercion(a, b, c, d, e):
    for i in range(1, len(a)):
        aux = a[i]
        aux_b = b[i]
        aux_c = c[i]
        aux_d = d[i]
        aux_e = e[i]
        j = i
        while j > 0 and a[j - 1] > aux:
            a[j] = a[j - 1]
            b[j] = b[j - 1]
            c[j] = c[j - 1]
            d[j] = d[j - 1]
            e[j] = e[j - 1]
            j -= 1
        a[j] = aux
        b[j] = aux_b
        c[j] = aux_c
        d[j] = aux_d
        e[j] = aux_e
    lista = [a, b, c, d, e]

    return lista


# programa principal en donde se ingresan los datos y se almacenan

camiones = []
distancia = []
toneladas = []
horas = []
cantidad = []

n_camion = int(input("Ingrese numero del camion: "))

while n_camion != -1:
    cant_horas = int(input("Ingrese numero de horas manejadas: "))
    cant_km = int(input("Ingrese distancia: "))
    cant_tn = int(input("Ingrese cantidad de toneladas transportadas: "))

    if n_camion < 0 or cant_horas < 0 or cant_km < 0 or cant_tn < 0:
        print("Datos Invalidos, introduccir datos positivos")
    # aca se busca si el dato del camion no esta repetido con un bucle while , si lo esta se le suman los valores de km horas y toneladas, si el n camion
    # no existe en la lista se agrega
    else:
        encontrar = False
        i = 0
        while i < len(camiones):
            if camiones[i] == n_camion:
                distancia[i] += cant_km

                toneladas[i] += cant_tn

                horas[i] += cant_horas

                cantidad[i] += 1

                encontrar = True

                i = len(camiones)
            else:
                i += 1

        if encontrar == False:
            camiones.append(n_camion)
            distancia.append(cant_km)
            toneladas.append(cant_tn)
            horas.append(cant_horas)
            cantidad.append(1)

    n_camion = int(input("Ingrese numero del camion: "))
# se llama a la funcion para sacar el promedio de horas.


hora_prom = cal_tiempo(horas, cantidad)
dia_total = hora_prom[0]
hora_total = hora_prom[1]

# este if se utiliza para ver cuantos elementos tiene la lsita, ya que si tiene solo un elemento no es necesario ordenarla
if len(camiones) > 1:
    lista = ordenar_lista_insercion(
        camiones, distancia, toneladas, dia_total, hora_total
    )
    # desarmamos la lista entragada por la funcion y creamos nuevas listas con el vactor de cada valor por ejemplo lista[0] se refiere al primer lugar
    # de lista que corresponde a el numero de camiones
    lista_camiones = lista[0]
    lista_distancias = lista[1]
    lista_toneladas = lista[2]
    lista_dias = lista[3]
    lista_horas = lista[4]

    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        "============================================================================================"
    )
    print(
        "------N-Camiones------------Tiempo Promedio--------------Distancia Total-----------Carge Total"
    )
    print(
        "============================================================================================"
    )
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    for i in range(len(lista_camiones)):
        # Este if es para diferenciar los camiones con mas de 20000 km y agregarles un cartel de revision mecanica
        if lista_distancias[i] > 20000:
            print(
                "|        ",
                lista_camiones[i],
                "           ",
                lista_dias[i],
                "dias",
                lista_horas[i],
                "horas",
                "              ",
                lista_distancias[i],
                "Km",
                "                 ",
                lista_toneladas[i],
                "Tn",
                "  |Revisión mecánica",
            )
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------"
            )
        else:
            print(
                "|        ",
                lista_camiones[i],
                "             ",
                lista_dias[i],
                "dias",
                lista_horas[i],
                "horas",
                "              ",
                lista_distancias[i],
                "Km",
                "                 ",
                lista_toneladas[i],
                "Tn",
                "  |",
            )
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------"
            )


else:
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    print(
        "=================================================================================="
    )
    print(
        "------N-Camiones------------Tiempo Promedio--------------Distancia Total-----------Carge Total"
    )
    print(
        "=================================================================================="
    )
    print(
        "------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    # atravez de este for in se imprimiran todos los elementos de la lista con sus valores correspondientes
    for i in range(len(camiones)):
        if distancia[i] > 20000:
            print(
                "|        ",
                camiones[i],
                "           ",
                dia_total[i],
                "dias",
                hora_total[i],
                "horas",
                "           ",
                distancia[i],
                "Km",
                "                  ",
                toneladas[i],
                "Tn",
                "  |Revisión mecánica",
            )
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------"
            )
        else:
            print(
                "|        ",
                camiones[i],
                "           ",
                dia_total[i],
                "dias",
                hora_total[i],
                "horas",
                "           ",
                distancia[i],
                "Km",
                "                 ",
                toneladas[i],
                "Tn",
                "  |",
            )
            print(
                "------------------------------------------------------------------------------------------------------------------------------------------------"
            )
