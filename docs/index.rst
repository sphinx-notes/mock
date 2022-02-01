====================================================================
sphinxnotes.mock - Sphinx extension for mocking directives and roles
====================================================================

.. image:: https://img.shields.io/github/stars/sphinx-notes/mock.svg?style=social&label=Star&maxAge=2592000
   :target: https://github.com/sphinx-notes/mock

:version: |version|
:copyright: Copyright ©2021 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

Sphinx extension for mocking directives and roles.
(Only supports directives for now).

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

:mock_directives: (Type: ``list[str]``, Default: ``[]``)
   Directives in this list will be overrides with mock directives which do nothing.
   In other words, the directives are hidden from the documentation.

Examples
========

Consider we have an undefined ``foo`` directive in document:

.. literalinclude:: foo.txt
   :language: rst

It will be rendered as:

.. topic:: Example

   .. include:: foo.txt

The directive can't be been because it is mocked in :download:`conf.py`:

.. literalinclude:: conf.py
   :lines: 32-41
   :emphasize-lines: 9

Consider we have another undefined ``bar`` directive in document:

.. literalinclude:: bar.txt
   :language: rst

It will be rendered as:

.. topic:: Example

   .. include:: bar.txt

We will also get warning messages like::

   bar.txt:3: ERROR: Unknown directive type "bar"

   .. bar::
      :opt1: val
      :opt2: val2
      :flag1:

when building documentation.

Change Log
==========

2022-02-01 1.0.0a0
------------------

Add support for mocking directives.
