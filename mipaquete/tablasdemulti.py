def tablasdemulti():
    inicio_r = int(input("Ingresa el rango inicial: "))
    final_r = int(input("Ingresa el rango final: "))
    inicio_t = int(input("Ingresa el inicio de la tabla: "))
    final_t = int(input("Ingresa el final de la tabla: "))
    for i in range(inicio_r,final_r):
        print(f"Tabla del {i}")
        for j in range(inicio_t,final_t):
            print(f"{i} x {j} = {i*j}")
    print()