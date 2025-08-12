from __future__ import annotations


class {{cookiecutter.project_python_name|capitalize|replace("_", "")}}Error(Exception):
    """Base exception for all {{cookiecutter.project_python_name}} errors."""


class ConfigurationError({{cookiecutter.project_python_name|capitalize|replace("_", "")}}Error):
    """Raised when settings or configuration fails."""


class FileError({{cookiecutter.project_python_name|capitalize|replace("_", "")}}Error):
    """Raised when file I/O operations fail."""
