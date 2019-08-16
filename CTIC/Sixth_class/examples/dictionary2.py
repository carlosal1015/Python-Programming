#from chalk import Chalk as ck

#white = ck('white', bold=True, underline=True)

def my_decorator(function):
    def welcome():
        print("La creación de la base de datos gerencias.", end = "\n")
        function()
        print("Base de datos de la gerencia.", end = "\n")
    return welcome

@my_decorator
def main():
    empleados_dictionary = {
        1000:dict(Nombre = "Juan", Fecha_ingreso = '10-10-17', Department = 103),
        1001:dict(Nombre = "María", Fecha_ingreso = '12-11-13', Department = 104),
        1002:dict(Nombre = "Marco", Fecha_ingreso = '09-07-15', Department = 103)
    }

    empleados_dictionary[1003] = dict(nombre = "Milagros", fecha_ingreso = '11-11-15', department = 104)

    del empleados_dictionary[1003]#empleados[1003] = {}

    for key, value in empleados_dictionary.items():
        print(f"Persona ID: {key}", end = "\n")
        for k, v in value.items():
            print(f"{k} {v}.", end="\n")

if __name__ == "__main__":
    main()

"""
En la decada de los 90, UML lenguaje unificado de modelos

Instlancion significa crear un objeto.
"""