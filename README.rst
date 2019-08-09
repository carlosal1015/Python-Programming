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

Installation
============

macOS
-----

On macOS, HTTPie can be installed via `Homebrew <http://brew.sh/>`_
(recommended):

.. code-block:: bash

    $ brew install httpie

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

Las tareas lo puede encontrar en su respecto fólder.

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

Temario
=======
.. _Introducción, historia e instalación: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/First_class/slides/S11_Introduccion%20a%20la%20Programaci%C3%B3n%20en%20Python%20CTIC-UNI.pdf
.. _identificadores y asignación: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/First_class/slides/S12_Elementos%20del%20Lenguaje%20de%20Programacion%20Python%20CTIC-UNI.pdf
.. _Estructuras de control: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Second_class/slides/EstructurasdeControlPythonCTIC-UNI.pdf
.. _importación de módulos: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Second_class/slides/Modulos%20Random%20Math%20en%20Python.pdf
.. _Tabla ASCII: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/tabla_caracteres-ASCII.pdf
.. _cadenas: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/Sesion%2003a%20Strings%20en%20Python%20CTIC-UNI.pdf
.. _funciones: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Third_class/slides/Sesion%2003b%20Funciones%20en%20Python%20CTIC-UNI.pdf
.. _Listas: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Fifth_class/slides/Sesion05-Diccionarios%20CTIC-UNI.pdf
.. _diccionarios: https://github.com/carlosal1015/Python-Programming/blob/master/CTIC/Fifth_class/slides/Sesion05-Diccionarios%20CTIC-UNI.pdf

.. _1: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/First_class
.. _2: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Second_class
.. _3: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Third_class
.. _4: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Fourth_class
.. _5: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Fifth_class
.. _6: https://github.com/carlosal1015/Python-Programming/tree/master/CTIC/Sixth_class