<<<<<<< HEAD
=======
#me falta sacar el promedio de las horas y que aparezcan en matricez 

>>>>>>> 9803494eaa6dabcee4751b5948e2c085d48feb97
def cal_tiempo(t_t,c_v):
    hora_prom=[]
    dias_horas_prom=[]
    axuliar=0
    ronda=0
    
    for i in t_t:
        axuliar=i//c_v[ronda]
        hora_prom.append(axuliar)
        ronda+=1
        
    for i in hora_prom:
            
        dias = i // 24
            
        horas = i % 24
            
        dias_horas_prom.append([dias,"d", horas,"h"])

    return dias_horas_prom

def ingreso_de_datos():
    camiones = []
    distancia = []
    toneladas = []
    horas = []
    cantidad=[]
    
    a = int(input("Ingrese numero del camion: "))

    while a != -1:
        d = int(input("Ingrese numero de horas manejadas: "))
        b = int(input("Ingrese distancia: "))
        c = int(input("Ingrese cantidad de toneladas transportadas: "))


        if a < 0 or b < 0 or c < 0 or d < 0:
            print("Datos Invalidos, introduccir datos positivos")
            
        else:
            encontrar=False
            i=0
            while i < len(camiones):

                if camiones[i] == a:
                    
                    distancia[i]+=b
                    
                    toneladas[i]+=c
                    
                    horas[i]+=d
                    
                    cantidad[i]+=1
                    
                    encontrar = True
                    
                    i=len(camiones)
                else:
                
                    i += 1

            if not encontrar:
                camiones.append(a)
                distancia.append(b)
                toneladas.append(c)
                horas.append(d)
                cantidad.append(1)
                
        a = int(input("Ingrese numero del camion: "))
        
    hora_prom=cal_tiempo(horas,cantidad)
    

    lista_total=[camiones, distancia, toneladas, hora_prom]
  
    return lista_total

def orden_lista(a,b,c,d):
        
    for i in range(len(a)-1):
            
        for j in range(i+1, len(a)):
            if a[i]< a[j]: 
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
                    
            lista=[a,b,c,d]
    return lista

lista=ingreso_de_datos()

lista_camiones=lista[0]
lista_distancias=lista[1]
lista_toneladas=lista[2]
lista_horas=lista[3]

if len(lista_camiones)>1:
    
    lista=orden_lista(lista_camiones,lista_distancias,lista_toneladas,lista_horas)

    lista_camiones=lista[0]
    lista_distancias=lista[1]
    lista_toneladas=lista[2]
    lista_horas=lista[3]

print("===============================================================================")
print("N-Camiones------Tiempo Promedio--------------Distancia Total--------Carge Total")
print("===============================================================================")

for i in range(len(lista_camiones)):
    if lista_distancias[i]>20000:
        print("|   ",lista_camiones[i],"      ",lista_horas[i],"           ",lista_distancias[i],"Km","                 ",lista_toneladas[i],"Tn","  |Revisión mecánica")
        print()
    else:  
        print("|   ",lista_camiones[i],"      ",lista_horas[i],"           ",lista_distancias[i],"Km","                 ",lista_toneladas[i],"Tn","  |")
        print()