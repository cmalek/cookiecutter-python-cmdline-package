Using the Command Line Interface
================================

The ``{{cookiecutter.project_python_name}}`` command-line interface provides
supporting functionality for working with __FILL_ME_IN__. This guide covers all
available commands and options.

Getting Help
------------

Basic Help
^^^^^^^^^^

.. code-block:: bash

    # Show main help
    {{cookiecutter.project_python_name}} --help

    # Show help for specific command groups
    {{cookiecutter.project_python_name}} group1 --help

Command Structure
-----------------

The CLI follows a hierarchical command structure:

.. code-block:: bash

    {{cookiecutter.project_python_name}} [global-options] <command-group> <subcommand> [options]

Global Options
--------------

Common options available for all commands:

.. code-block:: bash

    # Enable verbose output
    {{cookiecutter.project_python_name}} --verbose command

    # Suppress all output except errors
    {{cookiecutter.project_python_name}} --quiet command

    # Specify custom configuration file
    {{cookiecutter.project_python_name}} --config-file /path/to/config.yaml command

    # Choose output format (json, table, text)
    {{cookiecutter.project_python_name}} --output json command
    {{cookiecutter.project_python_name}} --output table command
    {{cookiecutter.project_python_name}} --output text command

Group1 Commands
---------------

The ``group1`` command group provides tools for __FILL_ME_IN__.

Feature 1 Usage
^^^^^^^^^^^^^^^

Analyze __FILL_ME_IN__ to understand the setup:

.. code-block:: bash

    # Description of feature 1
    {{cookiecutter.project_python_name}} group1 feature1

    # Use arguments
    {{cookiecutter.project_python_name}} group1 feature1 --arg "foo" --arg "bar"

    # Use JSON output
    {{cookiecutter.project_python_name}} --output json group1 feature1

Example output:

.. code-block:: json

    {
      "arg1": "foo",
      "arg2": "bar",
    }


Group2 Commands
---------------

The ``group2`` command group provides tools for __FILL_ME_IN__.

Feature 2 Usage
^^^^^^^^^^^^^^^

List all available AWS services from botocore definitions:

.. code-block:: bash

    # Basic usage
    {{cookiecutter.project_python_name}} group2 feature2

    # Use arguments
    {{cookiecutter.project_python_name}} group2 feature2 --arg "foo" --arg "bar"

    # Use JSON output
    {{cookiecutter.project_python_name}} --output json group2 feature2

Example output:

.. code-block:: json

    [
      {
        "arg1": "foo",
        "arg2": "bar",
      },
      {
        "arg1": "foo",
        "arg2": "bar",
      }
    ]


Show Settings
^^^^^^^^^^^^^

    # Use JSON output
    {{cookiecutter.project_python_name}} --output json settings show

Example output:

.. code-block:: json

    {
      "app_name": "{{cookiecutter.project_python_name}}",
      "app_version": "1.2.3",
      "default_output_format": "table",
      "enable_colors": true,
      "quiet_mode": false,
      "log_level": "INFO",
      "log_file": null
    }

Output Formats
--------------

JSON Format
^^^^^^^^^^^

.. code-block:: bash

    # JSON output for scripting and automation
    {{cookiecutter.project_python_name}} --output json group1 feature1 > config.json

    # JSON output for settings
    {{cookiecutter.project_python_name}} --output json settings show > settings.json

Table Format (Default)
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Table output for better readability
    {{cookiecutter.project_python_name}} group1 feature1

    # Table output for AWS services
    {{cookiecutter.project_python_name}} group2 feature2

    # Table output for settings
    {{cookiecutter.project_python_name}} settings show

Text Format
^^^^^^^^^^^

.. code-block:: bash

    # Simple text output
    {{cookiecutter.project_python_name}} --output text group1 feature1

    # Text output for settings
    {{cookiecutter.project_python_name}} --output text settings show

Configuration
-------------

See :doc:`/overview/configuration` for details on how to configure
``{{cookiecutter.project_python_name}}`` for your specific environment.

Examples
--------

Basic Usage Examples
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Sample usage 1
    {{cookiecutter.project_python_name}} group1 feature1 --arg1 "foo" --arg2 "bar"

    # Sample usage 2
    {{cookiecutter.project_python_name}} group2 feature2 --arg1 "foo" --arg2 "bar"

    # Show current settings
    {{cookiecutter.project_python_name}} settings show

Advanced Usage Examples
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Advanced usage 1
    {{cookiecutter.project_python_name}} group1 feature1 --arg1 "foo" --arg2 "bar"

    # Advanced usage 2
    {{cookiecutter.project_python_name}} group2 feature2 --arg1 "foo" --arg2 "bar"

Scripting Examples
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    #!/bin/bash

    echo "Doing something..."

    # Analyze something
    echo "Analysis:"
    {{cookiecutter.project_python_name}} --output table group1 feature1

    echo "Analysis complete."

Error Handling
--------------

Common Error Scenarios
^^^^^^^^^^^^^^^^^^^^^^

**Error 1**

    .. code-block:: bash

        # Error: No __FILL_ME_IN__ found
        {{cookiecutter.project_python_name}} group1 feature1
        # Error: No __FILL_ME_IN__ found

        # Solution: Ensure you're in the right directory
        ls *.tf

Troubleshooting
---------------

Debugging Commands
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # Enable verbose output for debugging
    {{cookiecutter.project_python_name}} --verbose group1 feature1

    # Do something to check if it's working
    bash command here

Common Issues
~~~~~~~~~~~~~

**__FILL_ME_IN__**
    - Ensure that ..
    - Verify file permissions

**Output Format Issues**
    - Use `--output json` for machine-readable output
    - Use `--output table` for human-readable output
    - Use `--output text` for simple text output


Best Practices
--------------

Output Format Selection
~~~~~~~~~~~~~~~~~~~~~~~

Choose appropriate output formats:

.. code-block:: bash

    # Use JSON for scripting and automation
    {{cookiecutter.project_python_name}} --output json group1 feature1 > config.json

    # Use table for human reading
    {{cookiecutter.project_python_name}} --output table group1 feature1

    # Use text for simple lists
    {{cookiecutter.project_python_name}} --output text group1 feature1 --names-only

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

Use configuration files when necessary:

.. code-block:: bash

    # Use custom configuration file
    {{cookiecutter.project_python_name}} --config-file ./{{cookiecutter.project_python_name}}.toml group1 feature1

    # Set environment variables
    export {{cookiecutter.project_python_name}}_CONFIG_FILE=./{{cookiecutter.project_python_name}}.toml
    {{cookiecutter.project_python_name}} group1 feature1