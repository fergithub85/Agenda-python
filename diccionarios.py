
agenda = {"Luis",1234562,"fernando",29471234,"pedrito",23124123}

agendando = True

while agendando:
    print("      ")
    print("MIS CONTACTOS")
    print("1. CONSULTA")
    print("2. AÑADIR")
    print("3. SALIR")
    print("4. AÑADIR")
    print("5. SALIR")
    
    
    opcion = ""
    while opcion not in ("1","2","3","4","5"):
        opcion = input("")
        
        if opcion == "1":  
            nombre = input("NOMBRE  A BUSCAR: ")
            if nombre  not in agenda:
                print("No esta en agenda")
            else:
                telf= agenda[nombre]
                print(nombre,"",telf)
        elif opcion == "2":
              nombre= input("nombre: ")
              if nombre in agenda:
                 print("ya esta en agenda")
              else:
                 telf = int(input("telefono: "))
                 agenda[nombre]= telf
                 print("tel añadido")
        elif opcion =="3":
                nombre=input("nombre: ")   
                if nombre not in agenda:
                   print("no esta")
                else:
                    agenda[nombre]=telf
                    print("añadido")
        elif opcion=="4":
                 nombre=input("nombre: ")
                 if nombre not in agenda:
                    print("no esta ")
                 else:
                    del agenda[nombre]
                    print("se borro")
        elif opcion=="5":
             agendando=false


 