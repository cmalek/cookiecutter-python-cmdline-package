Quickstart Guide
================

This guide will get you up and running with ``{{cookiecutter.project_python_name}}`` quickly, showing both
the Python client and command-line interface.

Prerequisites
-------------

- Python 3.10 or higher
- Follow the :doc:`/overview/installation` instructions to install ``{{cookiecutter.project_python_name}}``
- Other prerequisites here

Configuration
-------------

Typically the defaults that ship with ``{{cookiecutter.project_python_name}}``
will work. If you need to change those defaults, you can create a configuration
file at ``~/.{{cookiecutter.project_python_name}}.conf``:

You can configure ``{{cookiecutter.project_python_name}}`` using configuration
files or environment variables. See :doc:`/overview/configuration` for more
details.

Basic Usage
-----------

Get Help
^^^^^^^^

.. code-block:: bash

    # Show main help
    {{cookiecutter.project_python_name}} --help

    # Show help for specific command groups
    {{cookiecutter.project_python_name}} group1 --help
    {{cookiecutter.project_python_name}} group2 --help
    {{cookiecutter.project_python_name}} group3 --help
    {{cookiecutter.project_python_name}} settings --help

Feature 1 Usage
^^^^^^^^^^^^^^^

.. code-block:: bash

    # List all features
    {{cookiecutter.project_python_name}} group1 feature1

    # Filter services by pattern
    {{cookiecutter.project_python_name}} group1 feature1 --arg "foo" --arg "bar"


Feature 2 Usage
^^^^^^^^^^^^^^^

.. code-block:: bash

    # List all features
    {{cookiecutter.project_python_name}} group2 feature2

    # Filter services by pattern
    {{cookiecutter.project_python_name}} group2 feature2 --arg "foo" --arg "bar"

Output Formats
^^^^^^^^^^^^^^

.. code-block:: bash

    # Use table format (default) for human reading
    {{cookiecutter.project_python_name}} group1 feature1 --output table

    # Use JSON format for scripting
    {{cookiecutter.project_python_name}} group1 feature1 --output json

    # Use text format for simple output
    {{cookiecutter.project_python_name}} group1 feature1 --output text

    # Use text format for settings
    {{cookiecutter.project_python_name}} group1 feature1 --output text settings

Next Steps
----------

Now that you have the basics working:

1. **Usage**: See :doc:`/overview/usage` for more advanced features and detailed examples.
2. **Configuration**: See :doc:`/overview/configuration` for configuration options.
3. **Troubleshooting**: See the troubleshooting sections in each guide for common issues.

Getting Help
------------

- Check the full documentation for detailed examples
- Review the troubleshooting sections in each guide
- Report issues on the GitHub repository