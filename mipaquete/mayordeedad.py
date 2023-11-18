def mayordeedad():

    edad = int(input("Introduce tu edad: "))
    if edad < 18:
        print("Eres menor de edad.")
    elif edad == 18:
        print("Tienes justo 18 años, ya eres mayor de edad.")
    else:
        print("Eres mayor de edad.")