.. class:: no-web

    .. image:: https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.gif
        :alt: HTTPie in action
        :width: 100%
        :align: center


    .. image:: https://raw.githubusercontent.com/jakubroztocil/httpie/master/httpie.png
        :alt: HTTPie compared to cURL
        :width: 100%
        :align: center

.. contents::

.. section-numbering::

Main features
=============

* Expressive and intuitive syntax
* Formatted and colorized terminal output
* Built-in JSON support
* Forms and file uploads
* HTTPS, proxies, and authentication
* Arbitrary request data
* Custom headers
* Persistent sessions
* Wget-like downloads
* Python 2.7 and 3.x support
* Linux, macOS and Windows support
* Plugins
* Documentation
* Test coverage


Installation
============


macOS
-----


On macOS, HTTPie can be installed via `Homebrew <http://brew.sh/>`_
(recommended):

.. code-block:: bash

    $ brew install httpie


A MacPorts *port* is also available:

.. code-block:: bash

    $ port install httpie

Linux
-----

Most Linux distributions provide a package that can be installed using the
system package manager, for example:

.. code-block:: bash

    # Debian, Ubuntu, etc.
    $ apt-get install httpie

.. code-block:: bash

    # Fedora
    $ dnf install httpie

.. code-block:: bash

    # CentOS, RHEL, ...
    $ yum install httpie

.. code-block:: bash

    # Arch Linux
    $ pacman -S httpie


Windows, etc.
-------------

A universal installation method (that works on Windows, Mac OS X, Linux, …,
and always provides the latest version) is to use `pip`_:


.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools

    $ pip install --upgrade httpie


(If ``pip`` installation fails for some reason, you can try
``easy_install httpie`` as a fallback.)


Python version
--------------

Although Python 2.7 is supported as well, it is strongly recommended to
install HTTPie against the latest Python 3.x whenever possible. That will
ensure that some of the newer HTTP features, such as
`SNI (Server Name Indication)`_, work out of the box.
Python 3 is the default for Homebrew installations starting with version 0.9.4.
To see which version HTTPie uses, run ``http --debug``.


Unstable version
----------------

You can also install the latest unreleased development version directly from
the ``master`` branch on GitHub.  It is a work-in-progress of a future stable
release so the experience might be not as smooth.


.. class:: no-pdf

|unix_build|


On macOS you can install it with Homebrew:

.. code-block:: bash

    $ brew install httpie --HEAD


Otherwise with ``pip``:

.. code-block:: bash

    $ pip install --upgrade https://github.com/jakubroztocil/httpie/archive/master.tar.gz


Verify that now we have the
`current development version identifier <https://github.com/jakubroztocil/httpie/blob/0af6ae1be444588bbc4747124e073423151178a0/httpie/__init__.py#L5>`_
with the ``-dev`` suffix, for example:

.. code-block:: bash

    $ http --version
    1.0.0-dev


Usage
=====


Programación en |Python|
########################

.. |Python| image:: images/python.png
   :align: top
   :width: 200

Descarga Python `aquí <http://www.python.org/>`_  o instálalo vía

.. code-block:: bash

    # pacman -Sy python

============
Cronograma
============

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


.. code:: python

	from money import Money

	factory = Money(amount = eval(input("Ingrese el saldo de la empresa:")), currency = 'USD')
	computo = Money(5000, 'USD')
	mobiliario = Money(2000, 'USD')

	if factory.amount < 0:
			loan = Money(10000, 'USD') - factory
			factory = Money(10000, 'USD')
	elif factory.amount <= 20000:
			loan = Money(20000, 'USD') - factory
			factory = Money(20000, 'USD')

	resto = factory - (computo + mobiliario)
	insumos = incentivos = Money(amount = resto.amount/2, currency = 'USD')

	print(f"Se destinará {insumos.amount} {insumos.currency} para la compra de insumos.")
	print(f"Se destinará {incentivos.amount} {incentivos.currency} para los incentivos del personal.")
	print(f"Pedirá un préstamo de {loan.amount} {loan.currency}.")

.. code:: python

	from math import sqrt, sin, cos, pi
	from random import random as rd

	RADIUS = 10
	x, y = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] # [0]*4 no funciona!
	# x, y son objetos diferentes para que genere valores aleatorios distintos!

	for i in range(5):
		theta = 2*pi*rd() # \theta \in [0, 2\pi).
		radius = RADIUS*rd() # r \in \in [0, 10).
		x[i], y[i] = radius*cos(theta), radius*sin(theta)
		print(f"\t{x[i]} \t {y[i]}")

	distances = [sqrt((x[0] - x[i+1])**2 + (y[0] - y[i+1])**2) for i in range(4)]
	print(distances)

	index = distances.index(min(distances))
	print(index)
	print(f"El punto N°{index+1} es el más cercano al primer punto.")

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