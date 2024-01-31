"""Interactions between settings toml files and the program.
"""
import tomllib
import os
from typing import Any
import toml

from .logger import ColoredLogger

logger = ColoredLogger("settings_loader")

logger.debug("checking for settings file")
if not os.path.isfile("settings.toml"):
    logger.debug("settings file not found, creating one")
    with open("settings.toml", "w", encoding="utf-8") as file:
        file.write(
            "# WARNING!!! This file was generated using the program, if you are developing don't edit this file. Permanent changes to default settings should be done in `./src/default.toml`\n"
        )
        with open("src/default.toml", "r", encoding="utf-8") as default_file:
            file.write(default_file.read())
    logger.debug("settings file created")


logger.debug("opening settings file")
with open("settings.toml", "rb") as file:
    settings = tomllib.load(file)


def get_setting(name: str) -> Any:
    """Base on dot separated key returns a setting

    Args:
        name (str): a dot separated key, ex: debug.enabled

    Returns:
        any: a value read from the file
    """
    logger.debug(f"getting setting {name}")

    keys = name.split(".")
    current = settings
    for key in keys:
        current = current[key]
    return current


def change_setting(name: str, value: any):
    """Changes a setting in the settings file

    Args:
        name (str): a dot separated key, ex: debug.enabled
        value (any): the value to change the setting to
    """
    logger.debug(f"changing setting {name} to {value}")

    keys = name.split(".")
    current = settings
    for key in keys[:-1]:
        current = current[key]
    current[keys[-1]] = value

    with open("settings.toml", "w", encoding="utf-8") as f:
        toml.dump(settings, f)


def reset_defaults():
    """Restores the default settings"""
    logger.debug("resetting settings to defaults")
    with open("src/default.toml", "r", encoding="utf-8") as f:
        settings_str = f"# WARNING!!! This file was generated using the program, if you are developing don't edit this file. Permanent changes to default settings should be done in `./src/default.toml`\n{f.read()}\n"
    with open("settings.toml", "w", encoding="utf-8") as f:
        f.write(settings_str)
