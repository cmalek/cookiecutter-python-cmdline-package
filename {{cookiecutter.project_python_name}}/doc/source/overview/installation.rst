Installation
============

This guide covers how to install the ``{{cookiecutter.project_python_name}}`` package and its dependencies.

Prerequisites
-------------

Before installing ``{{cookiecutter.project_python_name}}``, ensure you have:

- Python 3.10 or higher
- `uv <https://docs.astral.sh/uv/>`_, `pip <https://pip.pypa.io/en/stable/>`_, or `pipx <https://pipx.pypa.io/stable/>`_

Installation Methods
--------------------

From PyPI with ``pip``
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install {{cookiecutter.project_python_name}}
    {{cookiecutter.project_python_name}} --help


From PyPI with ``uv``
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    sh -c "$(curl -fsSL https://astral.sh/uv/install)"
    uv tool install {{cookiecutter.project_python_name}}
    # Ensure you have ./local/bin in your PATH, since that's where uv puts the
    # executable
    {{cookiecutter.project_python_name}} --help

From PyPI with ``pipx``
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pipx install {{cookiecutter.project_python_name}}
    {{cookiecutter.project_python_name}} --help


From Source
~~~~~~~~~~~

If you want to install from the latest development version:

.. code-block:: bash

    git clone https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_python_name}}.git
    sh -c "$(curl -fsSL https://astral.sh/uv/install)"
    cd {{cookiecutter.project_python_name}}
    uv tool install .

Verification
------------

After installation, verify that ``{{cookiecutter.project_python_name}}`` is properly installed:

.. code-block:: shell

    {{cookiecutter.project_python_name}} --help


Configuration
-------------

After installation, you may want to configure ``{{cookiecutter.project_python_name}}`` for your specific
environment.  See :doc:`configuration` for detailed configuration options.

Getting Help
------------

If you encounter issues during installation:

1. Check the `GitHub issues <https://github.com/{{cookiecutter.github_organization}}/{{cookiecutter.project_python_name}}/issues>`_
2. Review the troubleshooting section above
3. Ensure your Python environment meets the prerequisites
4. Try installing in a virtual environment to isolate dependencies