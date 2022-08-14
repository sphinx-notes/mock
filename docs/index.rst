=======================
|logo| sphinxnotes.mock
=======================

.. |logo| image:: /_images/sphinx-notes.png
   :width: 10%

:version: |version|
:copyright: Copyright ©2021 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

Sphinx extension for mocking directives and roles without modifying documents.
(Only supports directives for now).

It is useful when you want to hide directive/role or your current environment does not support such directive/role.

For example, The current theme of this site theme (sphinx_book_theme__) supports  secondary sidebar for showing page table of contents, so the ``.. contents::`` directive is no longer needed. but I don't want to remove the directive bacause it can also show ToC on github__, that I can use this extension to hide it.

__ https://sphinx-book-theme.readthedocs.io/en/stable/
__ https://github.com/sphinx-notes/mock/blob/master/docs/index.rst

.. contents::
   :local:
   :backlinks: none

Installation
============

Download it from official Python Package Index:

.. code-block:: console

   $ pip install sphinxnotes-mock

Add extension to :file:`conf.py` in your sphinx project:

.. code-block:: python

    extensions = [
              # …
              'sphinxnotes.mock',
              # …
              ]

.. _Configuration:

Configuration
=============

The extension provides the following configuration:

:mock_directives: (Type: ``list[str|tuple[str,str]]``, Default: ``[]``)

                  Directive names in this list will be mocked by extension.

                  When a tuple given, the first field is the directive name and the second field is the custom mock mode (see ``mock_default_mode``),

                  For example, ``['toctree', ('contents', 'hide')]`` means that:

                  - mock ``toctree`` directive in default mode
                  - mock ``contents`` directive in ``hide`` mode

:mock_default_mode: (Type: ``str``, ''Default: ``'hide'``)

                    The default mode for mocking a directive/role.
                    Available values:

                    :hide: Hide the directive, it will not be seen on the document.
                    :literal_block: Show the raw text of directive in a `literal block`__

__ https://docutils.sourceforge.io/docs/user/rst/quickref.html#literal-blocks

Examples
========

Consider we have an undefined ``foo`` directive in document:

.. literalinclude:: foo.txt
   :language: rst

It will be rendered as:

.. admonition:: Example

   .. include:: foo.txt

The directive can't be seen because it is mocked in :download:`conf.py`:

.. literalinclude:: conf.py
   :lines: 40-45
   :emphasize-lines: 3-4

You can see we have another undefined ``bar`` directive is mocked, but in ``literal`` mode.

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

Change Log
==========

2022-08-14 1.0.0
----------------

- Add confval ``mock_default_mode``
- Support ``literal`` mock mode

2022-02-01 1.0.0a0
------------------

Add support for mocking directives.
