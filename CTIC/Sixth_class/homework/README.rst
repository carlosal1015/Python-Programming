=======
Tarea 6
=======
1. Escribir una clase `Fraccion` para representar números racionales como 1/2 y -3/8.
Las fracciones deberían siempre ser almacenadas en forma reducida; por ejemplo, almacenar
4/12 como 1/3 y 6/-9 como -2/3.
Sugerencia: Una función MCD (máximo común dividor) puede ayudar.

Definir los métodos `sumar` y `multiplicar` que acepten otra `Fraccion` como un parámetro y
modifique la `Fraccion` existente por la suma/multiplicación por este parámetro.

Defina los operadores `+`, `*`, `==`, y `<`.

2. Ordenar en forma descendente la base de datos de empleados del ejercicio 1 con respecto
al nombre de los empleados.

3. Defina una clase `Empleado` que represente a un empleado de una empresa. Cada empleado
tiene los siguientes atributos, código, nombre, género, ciudad y salario.

a) Defina un constructor que no reciba parámetros, sin embargo, inicialice las variables
de instancia solicitando datos del teclado.
b) Defina un método de instancia que permita visualizar todos los atributos del objeto.
c) Defina un método de instancia que permita modificar todos los atributos del objeto.
d) Agregue a la clase variable una *variable de clase*, aquel que es accesible por todos
por todos los objetos de la clase, es decir, es compartido por todas las instacias de la
clase. A esta variable se puede acceder tanto desde fuera de la clase como desde dentro
de la clase. Esta variable aumentará en 1 cada vez que se crea una instancia de la clase.