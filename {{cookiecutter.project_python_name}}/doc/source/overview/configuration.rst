Configuration: Command Line Tool
================================

This guide covers all configuration options for the
``{{cookiecutter.project_python_name}}`` command line tool, including
configuration files, environment variables, and command-line options.

``{{cookiecutter.project_python_name}}`` is a __FILL_ME_IN__.  The default
configuration should work for most use cases, but you can customize behavior
through various configuration methods.

Configuration Methods
---------------------

The ``{{cookiecutter.project_python_name}}`` command line tool supports multiple configuration methods,
loaded in order of priority:

1. **Command-line options** (highest priority)
2. **Environment variables** in the shell environment
3. **Configuration files**: a cascade of TOML files, most specific wins.
4. **Default values** (lowest priority)

Configuration Files
-------------------

File Locations
^^^^^^^^^^^^^^

Configuration files are searched in this order:

1. **Global configuration**: ``/etc/{{cookiecutter.project_python_name}}.toml`` (Unix/Linux) or ``C:/ProgramData/{{cookiecutter.project_python_name}}.toml`` (Windows)
2. **User configuration**: ``~/.cookiecutter.project_python_name}}/config.toml``
3. **Local configuration**: ``./{{cookiecutter.project_python_name}}.toml`` (current directory)
4. **Environment variables**: via the ``{{cookiecutter.project_python_name|upper}}_CONFIG_FILE`` environment variable
5. **Explicit configuration**: Path specified with ``--config-file`` option

File Format
^^^^^^^^^^^

Configuration files use TOML format:

.. code-block:: toml

    # Output settings
    default_output_format = "table"
    enable_colors = true
    quiet_mode = false

    # Logging settings
    log_level = "INFO"
    log_file = "/var/log/tfmate.log"

Configuration Options
^^^^^^^^^^^^^^^^^^^^^

**Application Settings**
    - **app_name**: Application name (default: ``{{cookiecutter.project_python_name}}``)
    - **app_version**: Application version (default: ``0.1.0``)

**Output Settings**
    - **default_output_format**: Default output format - ``table``, ``json``, or ``text`` (default: ``table``)
    - **enable_colors**: Enable colored output (default: ``true``)
    - **quiet_mode**: Enable quiet mode (default: ``false``)

**Logging Settings**
    - **log_level**: Logging level - ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR`` (default: ``INFO``)
    - **log_file**: Log file path (default: ``None``)

Environment Variables
---------------------

You can set configuration using environment variables. Environment variables
follow the pattern ``{{cookiecutter.project_python_name|upper}}_<SETTING_NAME>``:

.. code-block:: bash

    # Set output format
    export {{cookiecutter.project_python_name|upper}}_DEFAULT_OUTPUT_FORMAT="json"

    # Set log level
    export {{cookiecutter.project_python_name|upper}}_LOG_LEVEL="DEBUG"

Environment Variable Mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``{{cookiecutter.project_python_name|upper}}_DEFAULT_OUTPUT_FORMAT`` → ``default_output_format``
- ``{{cookiecutter.project_python_name|upper}}_ENABLE_COLORS`` → ``enable_colors``
- ``{{cookiecutter.project_python_name|upper}}_QUIET_MODE`` → ``quiet_mode``
- ``{{cookiecutter.project_python_name|upper}}_LOG_LEVEL`` → ``log_level``
- ``{{cookiecutter.project_python_name|upper}}_LOG_FILE`` → ``log_file``

Command-Line Options
--------------------

Global Options
^^^^^^^^^^^^^^

All commands support these global options:

.. code-block:: bash

    # Enable verbose output
    {{cookiecutter.project_python_name}} --verbose command

    # Suppress all output except errors
    {{cookiecutter.project_python_name}} --quiet command

    # Specify custom configuration file
    {{cookiecutter.project_python_name}} --config-file /path/to/config.toml command

    # Choose output format
    {{cookiecutter.project_python_name}} --output json command
    {{cookiecutter.project_python_name}} --output table command
    {{cookiecutter.project_python_name}} --output text command

Option Reference
^^^^^^^^^^^^^^^^

**--verbose, -v**
    Enable verbose output with detailed logging.

    Example:
    .. code-block:: bash

        {{cookiecutter.project_python_name}} --verbose group command

**--quiet, -q**
    Suppress all output except errors.

    Example:
    .. code-block:: bash

        {{cookiecutter.project_python_name}} --quiet group command

**--config-file**
    Specify a custom configuration file path.

    Example:
    .. code-block:: bash

        {{cookiecutter.project_python_name}} --config-file ./custom-config.toml group command

**--output**
    Choose output format: ``json``, ``table``, or ``text``.

    Default: ``table``

    Example:
    .. code-block:: bash

        {{cookiecutter.project_python_name}} --output json group command

Configuration Examples
----------------------

Basic Setup
^^^^^^^^^^^

For basic usage with defaults:

.. code-block:: toml

    # ~/.{{cookiecutter.project_python_name}}.toml
    # No configuration file needed - defaults work for most cases

Development Environment
^^^^^^^^^^^^^^^^^^^^^^^

For development and testing:

.. code-block:: toml

    # ~/.{{cookiecutter.project_python_name}}.toml
    default_output_format = "json"
    enable_colors = true
    log_level = "DEBUG"

Production Environment
^^^^^^^^^^^^^^^^^^^^^^

For production systems:

.. code-block:: toml

    # /etc/{{cookiecutter.project_python_name}}.toml
    default_output_format = "table"
    enable_colors = false
    log_level = "WARNING"
    log_file = "/var/log/{{cookiecutter.project_python_name}}.log"

AWS-Specific Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

For AWS-focused workflows:

.. code-block:: toml

    # ~/.config/tfmate/config.toml
    aws_default_region = "us-west-2"
    aws_default_profile = "production"
    terraform_timeout = 45
    terraform_max_retries = 3

Scripting Configuration
^^^^^^^^^^^^^^^^^^^^^^^

For automation and scripting:

.. code-block:: toml

    # ~/.{{cookiecutter.project_python_name}}.toml
    default_output_format = "json"
    enable_colors = false
    quiet_mode = true
    log_level = "ERROR"

Security Considerations
-----------------------

Configuration File Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Protect your configuration files:

.. code-block:: bash

    # Set proper permissions for user configuration
    chmod 600 ~/.{{cookiecutter.project_python_name}}.toml

    # For system-wide configuration
    chmod 640 /etc/{{cookiecutter.project_python_name}}.toml
    chown root:root /etc/{{cookiecutter.project_python_name}}.toml

Environment Variable Security
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Secure environment variable usage:

.. code-block:: bash

    from {{cookiecutter.project_python_name}}.settings import Settings

    # Load and display configuration
    settings = Settings()
    print(f"Output format: {settings.default_output_format}")
    print(f"Timeout: {settings.terraform_timeout}")
    print(f"AWS region: {settings.aws_default_region}")

Common Issues
^^^^^^^^^^^^^

**Configuration Not Loaded**
    - Check file permissions
    - Verify file format (TOML syntax)
    - Ensure file is in correct location
    - Check for syntax errors in TOML file

**Configuration Not Valid**
    - Verify TOML syntax is correct
    - Check that setting names match expected values
    - Ensure boolean values are ``true``/``false``, not ``True``/``False``

**Environment Variables Not Recognized**
    - Check variable names (must start with ``{{cookiecutter.project_python_name|upper}}_``)
    - Restart terminal session
    - Verify variable values

**Command-Line Options Override**
    - Command-line options take highest priority
    - Check for conflicting options
    - Use ``--help`` to see current options

Configuration Validation
------------------------

Validation Rules
^^^^^^^^^^^^^^^^

The library validates configuration:

- **default_output_format**: Must be one of ``table``, ``json``, or ``text``
- **log_level**: Must be one of ``DEBUG``, ``INFO``, ``WARNING``, or ``ERROR``
- **enable_colors**: Must be a boolean value
- **quiet_mode**: Must be a boolean value

Error Messages
^^^^^^^^^^^^^^

Common validation errors:

.. code-block:: bash

    # Invalid output format
    Error: Invalid default_output_format value

    # Invalid log level
    Error: log_level must be one of DEBUG, INFO, WARNING, ERROR

Best Practices
--------------

Configuration Management
^^^^^^^^^^^^^^^^^^^^^^^^^

1. **Use configuration files for defaults**

   - Set common settings in ``~/.{{cookiecutter.project_python_name}}.toml``
   - Use environment variables for overrides
   - Use command-line options for one-time changes

2. **Separate environments**

   - Use different config files for different environments
   - Use environment variables for sensitive data
   - Document configuration requirements

3. **Version control**

   - Don't commit sensitive configuration
   - Use templates for configuration files
   - Document configuration changes

4. **Security**

   - Protect configuration files with proper permissions
   - Use environment variables for credentials
   - Clear sensitive environment variables

5. **Testing**

   - Test timeout settings for your environment
   - Verify output formats work for your use case
   - Test logging configuration

Configuration Templates
-----------------------

Basic Template
^^^^^^^^^^^^^^

.. code-block:: toml

    # config.toml.template
    # Application settings
    [{{cookiecutter.project_python_name}}]
    # Output settings
    default_output_format = "table"
    enable_colors = true
    quiet_mode = false

    # Logging settings
    log_level = "INFO"
    log_file = null

Production Template
^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    # production.toml
    # Application settings
    [{{cookiecutter.project_python_name}}]

    # Output settings
    default_output_format = "table"
    enable_colors = false
    quiet_mode = false

    # Logging settings
    log_level = "WARNING"
    log_file = "/var/log/{{cookiecutter.project_python_name}}.log"

Development Template
^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    # development.toml
    # Application settings
    [tfmate]
    # Output settings
    default_output_format = "json"
    enable_colors = true
    quiet_mode = false

    # Logging settings
    log_level = "DEBUG"
    log_file = null

Scripting Template
^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    # scripting.toml
    # Application settings
    [{{cookiecutter.project_python_name}}]

    # Output settings
    default_output_format = "json"
    enable_colors = false
    quiet_mode = true

    # Logging settings
    log_level = "ERROR"
    log_file = "/dev/stdout"