========
{{cookiecutter.project_python_name}}
========

.. toctree::
   :caption: Overview
   :hidden:

   overview/quickstart
   overview/installation
   overview/configuration
   overview/usage
   overview/faq

.. toctree::
   :caption: Runbook
   :hidden:

   runbook/contributing
   runbook/coding_standards

.. toctree::
   :caption: Reference
   :hidden:

   changelog
   api/models


This is the ``{{cookiecutter.project_python_name}}`` project, an command line project that implements __FILL_THIS__IN__.

Overview
--------

This project provides a `click <https://click.palletsprojects.com/en/8.0.x/>`_
command line interface named ``{{cookiecutter.project_python_name}}`` that is the home of various bits of helper code that help us __FILL_THIS__IN__.

Installation
------------

First, you will need to install `uv <https://docs.astral.sh/uv/>`_:

.. code-block:: bash

   $ sh -c "$(curl -fsSL https://astral.sh/uv/install)"

Ensure you have a system python installed that is at least version 3.11, though we prefer 3.13.  You
can do this via ``uv``.

.. code-block:: bash

   $ uv python install 3.13

Then you can install the script like so:

.. code-block:: bash

   $ uv tool install --python 3.13 {{cookiecutter.project_python_name}}/{{cookiecutter.project_python_name}}

This will install the ``{{cookiecutter.project_python_name}}`` command line tool in your path.

If you want to work on this codebase, see :doc:`/runbook/contributing` for more
information.