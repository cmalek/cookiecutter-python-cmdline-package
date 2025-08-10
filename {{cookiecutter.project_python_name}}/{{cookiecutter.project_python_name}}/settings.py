"""
Settings management for {{cookiecutter.project_python_name}}.
"""

import os
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings with cascading configuration support.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        env_prefix="tfmate_",
    )

    # Application settings
    app_name: str = Field(
        default="{{cookiecutter.project_python_name}}", description="Application name"
    )
    app_version: str = Field(default="0.1.0", description="Application version")

    # Output settings
    default_output_format: Literal["table", "json", "text"] = Field(
        default="table", description="Default output format"
    )
    enable_colors: bool = Field(default=True, description="Enable colored output")
    quiet_mode: bool = Field(default=False, description="Enable quiet mode")

    # Logging settings
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", description="Logging level"
    )
    log_file: str | None = Field(default=None, description="Log file path")

    @classmethod
    def from_file(cls, config_file: str | None = None) -> "Settings":
        """
        Load settings from file with cascading configuration.

        Args:
            config_file: Optional path to configuration file

        Returns:
            Loaded settings instance

        """
        # Define configuration file paths in order of precedence
        config_paths = []

        # Global configuration
        if os.name == "nt":  # Windows
            global_config = (
                Path(os.environ.get("PROGRAMDATA", "C:/ProgramData"))
                / "{{cookiecutter.project_python_name}}"
                / "config.toml"
            )
        else:  # Unix-like
            global_config = Path(
                "/etc/{{cookiecutter.project_python_name}}/config.toml"
            )

        if global_config.exists():
            config_paths.append(global_config)

        # User home configuration
        user_config = (
            Path.home()
            / ".config"
            / "{{cookiecutter.project_python_name}}"
            / "config.toml"
        )
        if user_config.exists():
            config_paths.append(user_config)

        # Local configuration
        local_config = Path.cwd() / "{{cookiecutter.project_python_name}}.toml"
        if local_config.exists():
            config_paths.append(local_config)

        # Explicit configuration file (highest precedence)
        if config_file:
            explicit_config = Path(config_file)
            if explicit_config.exists():
                config_paths.append(explicit_config)

        # Load settings with file configuration
        if config_paths:
            # Use the last (highest precedence) config file
            config_file_path = config_paths[-1]
            return cls(_env_file=config_file_path, _env_file_encoding="utf-8")

        # Fall back to environment variables and defaults
        return cls()

    def get_config_paths(self) -> list[Path]:
        """
        Get list of configuration file paths that were loaded.

        Returns:
            List of configuration file paths

        """
        paths = []

        # Global configuration
        if os.name == "nt":  # Windows
            global_config = (
                Path(os.environ.get("PROGRAMDATA", "C:/ProgramData"))
                / "{{cookiecutter.project_python_name}}"
                / "config.toml"
            )
        else:  # Unix-like
            global_config = Path(
                "/etc/{{cookiecutter.project_python_name}}/config.toml"
            )

        if global_config.exists():
            paths.append(global_config)

        # User home configuration
        user_config = Path.home() / ".{{cookiecutter.project_python_name}}.toml"
        if user_config.exists():
            paths.append(user_config)

        # Local configuration
        local_config = Path.cwd() / ".{{cookiecutter.project_python_name}}.toml"
        if local_config.exists():
            paths.append(local_config)

        return paths
