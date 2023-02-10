The current theme (Furo__) supports secondary sidebar for showing page table
of contents, so the ``.. contents::`` directive is no longer needed.

So we can hide it with this extension, added directive name "contents" to the
``mock_directives`` :doc:`conf` item:

.. literalinclude:: conf.py
   :lines: 36-40
   :emphasize-lines: 2

You can see there is a ``contents`` directive in the source code of this pages,

.. contents::

but it doesn't render anything.

.. literalinclude:: usage_for_quickstart.rst
   :language: rst
   :lines: 11-15
   :emphasize-lines: 3

__ https://pradyunsg.me/furo/
