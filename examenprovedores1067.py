class Provedores:
    ID = 0
    Nombre= ""
    Contacto= ""
    Telefono = 0
    Direccion= ""
    TipoProducto= ""
    Calificacion= 0

    def mostrarID():
        ID = ["ID_10", "ID_11", "ID_12","ID_13","ID_14"]
        for i in range(len(ID)):
            print(ID[i])

    def mostrarNombre():
        Nombre = ("Adriel", "Carlos", "Melany", "Joselyn","David")
        for x in Nombre:
            print(x)

    def mostrarContacto():
        Contacto = {"adriel12@gmail.com", "carlosmel@gmail.com", "MelanyC@gmail.com",
        "joselynperez@gmail.com","elmen777@gmail.com"}
        for x in Contacto:
            print(x)

    def mostrarTelefono():
        Telefono = ("656 578 8989", "656 767 0909", "656 755 8555", "656 909 7878","656 545 6555")
        for x in Telefono:
            print(x)

    def mostrarDireccion():
        Direccion = ("C.cesar", "C.Hiedra", "C.Nose", "C.Egipto","C.Anubis")
        for x in Direccion:
            print(x)

    def mostrarTipoProductos():
        TipoProducto = ("Peliculas miedo", "Pelicula guerra", "Pelicula accion", "Pelicula miedo","Pelicula Accion")
        for x in TipoProducto:
            print(x)

    def mostrarCalificacion():
        Calificacion = ("10/10", "9/10", "9/10", "10/10","8/10")
        for x in Calificacion:
            print(x)



print("")
print("---IDs---")
Provedores.mostrarID()
print("")
print("---Nombres---")
Provedores.mostrarNombre()
print("")
print("---Contacto---")
Provedores.mostrarContacto()
print("")
print("---Telefono---")
Provedores.mostrarTelefono()
print("")
print("---Direccion---")
Provedores.mostrarTelefono()
print("")
print("---TipoProductos---")
Provedores.mostrarTelefono()
print("")
print("---Calificacioncls---")
Provedores.mostrarTelefono()