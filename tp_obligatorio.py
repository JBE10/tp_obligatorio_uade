#def que sirve para promediar la cantidad de  tiempo cada camion, t_t=tiempo total c_v=cantidad de viajes hechos por ese numero de camion
#lo primero que se hace es sacar el promedio en horas es decir que los datos recibidos dividido a la cantiad de viajes
#luego esas horas se dividen por 24 ya que 24 horas=un dia y luego se utiliza la funcion resto(%) para sacar las horas que quedan
#luego se devuelve la lista dias y horas ya promediada
def cal_tiempo(t_t, c_v):
    hora_prom = []
    dias_horas_prom = []
    axuliar = 0
    ronda = 0

    for i in t_t:
        axuliar = i // c_v[ronda]
        hora_prom.append(axuliar)
        ronda += 1

    for i in hora_prom:
        dias = i // 24

        horas = i % 24

        dias_horas_prom.append([dias, "d", horas, "h"])

    return dias_horas_prom

#esta funcion sirve para ordenar la lista de menor a mayor lo primero que se hace asignar un rango con len ya que el rango sera la cantidad de camiones
#j es +1 de i ya que ira buscando una osicion mas adelante, el auxiliar ayudara a guaradar el item de la lista que esta siendo cambiado
def orden_lista(a, b, c, d):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                auxiliar = a[i]
                a[i] = a[j]
                a[j] = auxiliar
                auxiliar_b = b[i]
                b[i] = b[j]
                b[j] = auxiliar_b
                auxiliar_c = c[i]
                c[i] = c[j]
                c[j] = auxiliar_c
                auxiliar_d = d[i]
                d[i] = d[j]
                d[j] = auxiliar_d

    lista = [a, b, c, d]
    return lista
#programa principal en dodne se ingresar los datos y se almacenan

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
#aca se busca si el dato del camion no esta repetido con un bucle while 
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

        if not encontrar:
            camiones.append(n_camion)
            distancia.append(cant_km)
            toneladas.append(cant_tn)
            horas.append(cant_horas)
            cantidad.append(1)

    n_camion = int(input("Ingrese numero del camion: "))

hora_prom = cal_tiempo(horas, cantidad)


if len(camiones) > 1:
    lista = orden_lista(camiones, distancia, toneladas, hora_prom)

    lista_camiones = lista[0]
    lista_distancias = lista[1]
    lista_toneladas = lista[2]
    lista_horas = lista[3]
    
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("============================================================================================")
    print("------N-Camiones------------Tiempo Promedio--------------Distancia Total-----------Carge Total")
    print("============================================================================================")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(lista_camiones)):
        if lista_distancias[i] > 20000:
            print("|        ",lista_camiones[i],"              ",lista_horas[i],"              ",lista_distancias[i],"Km","                 ",lista_toneladas[i],"Tn","  |Revisión mecánica",)
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("|        ",lista_camiones[i],"              ",lista_horas[i],"              ",lista_distancias[i],"Km","                 ",lista_toneladas[i],"Tn","  |",)
            print("------------------------------------------------------------------------------------------------------------------------------------------------")


else:
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    print("==================================================================================")
    print("------N-Camiones------------Tiempo Promedio--------------Distancia Total-----------Carge Total")
    print("==================================================================================")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(len(camiones)):
        if distancia[i] > 20000:
            print("|        ",camiones[i],"              ",hora_prom[i],"           ",distancia[i],"Km","                  ",toneladas[i], "Tn","  |Revisión mecánica",)
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("|        ",camiones[i],"              ",hora_prom[i],"           ",distancia[i], "Km","                 ",toneladas[i],"Tn","  |",)
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
