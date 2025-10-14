.. This file is generated from sphinx-notes/cookiecutter.
   You need to consider modifying the TEMPLATE or modifying THIS FILE.

================
sphinxnotes-mock
================

.. |docs| image:: https://img.shields.io/github/deployments/sphinx-notes/mock/github-pages?label=docs
   :target: https://sphinx.silverrainz.me/mock
   :alt: Documentation Status
.. |license| image:: https://img.shields.io/github/license/sphinx-notes/mock
   :target: https://github.com/sphinx-notes/mock/blob/master/LICENSE
   :alt: Open Source License
.. |pypi| image:: https://img.shields.io/pypi/v/sphinxnotes-mock.svg
   :target: https://pypi.python.org/pypi/sphinxnotes-mock
   :alt: PyPI Package
.. |download| image:: https://img.shields.io/pypi/dm/sphinxnotes-mock
   :target: https://pypi.python.org/pypi/sphinxnotes-mock
   :alt: PyPI Package Downloads
.. |github| image:: https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white/
   :target: https://github.com/sphinx-notes/mock
   :alt: GitHub Repository

|docs| |license| |pypi| |download| |github|

Introduction
============

.. INTRODUCTION START

Sphinx extension for masking unsupported directives and roles without modifying
documents.

.. note:: For now, only directive is supported

It is especially useful when a certain directive/role is provided
by an incompatible extension, or the directive/roles is incompatible with your
current buidler or theme.

.. INTRODUCTION END

Getting Started
===============

.. note::

   We assume you already have a Sphinx documentation,
   if not, see `Getting Started with Sphinx`_.


First, downloading extension from PyPI:

.. code-block:: console

   $ pip install sphinxnotes-mock


Then, add the extension name to ``extensions`` configuration item in your
:parsed_literal:`conf.py_`:

.. code-block:: python

   extensions = [
             # …
             'sphinxnotes.mock',
             # …
             ]

.. _Getting Started with Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _conf.py: https://www.sphinx-doc.org/en/master/usage/configuration.html

.. ADDITIONAL CONTENT START

The current theme (`furo <https://pradyunsg.me/furo/>`_) supports secondary
sidebar for showing local table of contents, the :rst:dir:`contents`
directive is no longer needed.

So we can hide it with this extension, added directive name "contents" to the
``mock_directives`` :doc:`conf` item:

.. literalinclude:: conf.py
   :start-at: mock_directives
   :end-at: ]
   :emphasize-lines: 2

You can see there is a ``contents`` directive in the source code of this pages,

.. example::
   :style: grid

   .. contents::

.. ADDITIONAL CONTENT END

Contents
========

.. toctree::
   :caption: Contents

   usage
   conf
   changelog

The Sphinx Notes Project
========================

The project is developed by `Shengyu Zhang`__,
as part of **The Sphinx Notes Project**.

.. toctree::
   :caption: The Sphinx Notes Project

   Home <https://sphinx.silverrainz.me/>
   Blog <https://silverrainz.me/blog/category/sphinx.html>
   PyPI <https://pypi.org/search/?q=sphinxnotes>

__ https://github.com/SilverRainZ
