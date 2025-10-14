=====
Usage
=====

Mock directives
===============

Consider we have an undefined ``foo`` directive in document:

.. example::
   :style: grid

   Here is a ``foo`` directive:

   .. foo::
      :opt1: val1
      :opt2: val2
      :flag1:

The directive can't be seen because it is mocked in :download:`conf.py`:

.. literalinclude:: conf.py
   :start-at: mock_directives
   :end-at: ]
   :emphasize-lines: 3

Mock Mode
=========

You can see directive ``bar`` is mocked too, but in ``literal`` mode.

.. literalinclude:: conf.py
   :start-at: mock_directives
   :end-at: ]
   :emphasize-lines: 4

Consider we also have ``bar`` directive in document:

.. example::
   :style: grid

   Here is a ``bar`` directive:

   .. bar::
      :opt1: val1
      :opt2: val2
      :flag1:

What happens if we don't mock undefined directives?

.. example::
   :style: grid

   Here is a ``baz`` directive:

   .. baz::
      :opt1: val1
      :opt2: val2
      :flag1:
