import pymysql
  
while True:


      
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Ingresar registros")
        print("[2] Mostrar reistros    ")
        print("[3] Borrar registros")
        print("[4] Actualizar registros")
        print("[5] Salir     ")


        option = input("Seleccione una opcion")

        if option == '1':
            
            while True:  
                  nombre=input("ingrese producto")
                  if len(nombre) >0 and nombre [0]!=" ":
                      break
                  else:
                      print("no se ha ingresado un nombre")

            while True: 
                 try:
                      precio= int(input("ingrese valor producto"))  
                      break
                 except ValueError:
                      print("el precio debe ser entero")

            Connection = pymysql.connect(host="localhost",user="root",password="",db="test")
            cur = Connection.cursor()
            try:
              
               
               sql1 = "INSERT INTO productos(nombre,precio) VALUES ('{0}','{1}')".format(nombre,precio)
               cur.execute(sql1)
               Connection.commit()
               print("<-----registros añadidos!!----->")
         
            except pymysql.OperationalError: 
                print("error")
            finally:
                Connection.close()


            

        elif option == '2':
            Connection = pymysql.connect(host="localhost",user="root",password="",db="test")
            cur = Connection.cursor()
                 
            
            
            try:
               cur.execute("SELECT * FROM productos ")
               datos = cur.fetchall()
               for dato in datos:
                  print(dato)
            except pymysql.OperationalError:
                  print("error")
            finally:
                Connection.close()

        elif option == '3':
            Connection = pymysql.connect(host="localhost",user="root",password="",db="test")
            cur = Connection.cursor()
            
            while True:  
                  nombre=input("ingrese nombre a eliminar")
                  if len(nombre) >0 and nombre [0]!=" ":
                      break
                  else:
                      print("no se ha ingresado un nombre")
            
            try:
               sql1 = "DELETE FROM productos WHERE nombre = '{0}'  ".format(nombre)
               cur.execute(sql1)
               Connection.commit()
               print("<-----registros eliminados!!----->")
                  
            except pymysql.OperationalError:
                  print("error")
            finally:
                Connection.close()

Connection.close()