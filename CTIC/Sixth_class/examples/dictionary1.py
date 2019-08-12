def my_decorator(function):
    def welcome():
        print("La creación de la base de datos gerencias.")
        function()
        print("Base de datos de la gerencia.")
    return welcome

@my_decorator
def main():
    my_dic = dict()
    my_dic[101] = "RRHH"
    my_dic[102] = "FINANZAS"
    my_dic[103] = "CONTABILIDAD"
    my_dic[104] = "VENTAS"
    my_dic[105] = "INGENIERIA"
    my_dic[106] = "SOPORTE"

    for key, value in my_dic.items():
        print(f"{key} \t {value}")


if __name__ == "__main__":
    main()