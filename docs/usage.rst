=====
Usage
=====

Mock directives
===============

Consider we have an undefined ``foo`` directive in document:

.. literalinclude:: foo.txt
   :language: rst

It will be rendered as:

.. admonition:: Example

   .. include:: foo.txt

The directive can't be seen because it is mocked in :download:`conf.py`:

.. literalinclude:: conf.py
   :lines: 36-40
   :emphasize-lines: 3

Mock Mode
=========

You can see directive ``bar`` is mocked too, but in ``literal`` mode.

.. literalinclude:: conf.py
   :lines: 36-40
   :emphasize-lines: 4

Consider we also have ``bar`` directive in document:

.. literalinclude:: bar.txt
   :language: rst

It will be rendered as:

.. admonition:: Example

   .. include:: bar.txt

What happens if we don't mock undefined directives?

.. literalinclude:: baz.txt
   :language: rst

It will be rendered as:

.. admonition:: Example

   .. include:: baz.txt

