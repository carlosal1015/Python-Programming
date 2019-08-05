===============================
Programación en |Python|
===============================

.. |Python| image:: images/python.png
   :align: top
   :width: 200

Descarga Python `aquí <http://www.python.org/>`_  o instálalo vía

.. code-block:: bash

    # pacman -Sy python

############
Cronograma
############

====== ============ ===================================
Clase	Fecha		Temas
====== ============ ===================================
`1`_	24/07/2019	`Introducción, historia e instalación`_, `identificadores y asignación`_.
`2`_	31/07/2019	`Estructuras de control`_, `importación de módulos`_.
`3`_	02/08/2019	`Tabla ASCII`_, `cadenas`_ y `funciones`_.
`4`_	05/08/2019	`Listas`_, `diccionarios`_.
`5`_	07/08/2019	Orientado a objetos.
`6`_	09/08/2019	Archivos.
====== ============ ===================================

Tareas
=======

Las tareas

.. code:: python

  from datetime import datetime as dt

	hora_salida = ['08:00' ,'09:43', '11:19', '12:47', '14:00', '15:45', '19:00', '21:45']
	hora_llegada = ['10:16', '11:52', '13:31', '15:19', '16:08', '17:55', '21:20', '23:58']

	print("Ingrese la hora en formato de 24 horas:")

	hora_consultada = input("Hora: ")
	minuto_consultado = input("Minutos: ")

	consulta = dt.strptime(hora_consultada + ":" + minuto_consultado, "%H:%M")
	hora_cercana = min(hora_salida, key=lambda t: abs(dt.strptime(t, "%H:%M") - consulta))

	index = hora_salida.index(hora_cercana)
	print(f"Tiempo de partida más cercano es {hora_cercana}, llegada a las {hora_llegada[index]}")

Subsection
----------

SubSubSections
^^^^^^^^^^^^^^

Paragraph
"""""""""

* Bulleted
* List

1. Numbered
2. List

.. be careful! Comment will reset counter for auto numbered lists

#. Auto numbered
#. List

9000. Vegeta! What does the
		scouter say about this power level?

#. It's over 9000!

Grid table:

+--------+-----------+----------------+
| Word   | Decimal   | Rome notation  |
+========+===========+================+
| one    | 1         | I              |
+--------+-----------+----------------+

*********
Temario
*********
.. _Introducción, historia e instalación: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/First_class/slides/S11_Introduccion%20a%20la%20Programaci%C3%B3n%20en%20Python%20CTIC-UNI.pdf
.. _identificadores y asignación: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/First_class/slides/S12_Elementos%20del%20Lenguaje%20de%20Programacion%20Python%20CTIC-UNI.pdf
.. _Estructuras de control: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Second_class/slides/EstructurasdeControlPythonCTIC-UNI.pdf
.. _importación de módulos: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Second_class/slides/Modulos%20Random%20Math%20en%20Python.pdf
.. _Tabla ASCII: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/tabla_caracteres-ASCII.pdf
.. _cadenas: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/Sesion%2003a%20Strings%20en%20Python%20CTIC-UNI.pdf
.. _funciones: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/Sesion%2003b%20Funciones%20en%20Python%20CTIC-UNI.pdf
.. _Listas: 
.. _diccionarios: 


.. _1: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/First_class
.. _2: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Second_class
.. _3: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Third_class
.. _4: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Fourth_class
.. _5: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Fifth_class
.. _6: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Sixth_class