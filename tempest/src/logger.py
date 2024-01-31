"""Utility to log values"""
import logging
import argparse


def parse_args():
    """Gets the argv args"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--log-level", default="info", help="logging level, either debug or info"
    )
    return parser.parse_args()


class ColoredLogger:
    """A colored output logger"""

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        # Set a default level based on settings.toml
        args = parse_args()
        self.logger.setLevel(args.log_level.upper())
        self.formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
        )

        # Create console handler and set level to debug
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(self.formatter)

        self.logger.addHandler(self.ch)

    def log(self, level, message):
        """Define the colors"""
        color_code = {
            "DEBUG": "\033[94m",  # Blue for DEBUG
            "INFO": "\033[92m",  # Green for INFO
            "WARNING": "\033[93m",  # Yellow for WARNING
            "ERROR": "\033[91m",  # Red for ERROR
            "CRITICAL": "\033[95m",  # Magenta for CRITICAL
        }.get(
            level, "\033[0m"
        )  # Reset to default color if not found

        colored_message = (
            f"{color_code}{message}\033[0m"  # Append reset code after the message
        )
        getattr(self.logger, level.lower())(colored_message)

    def debug(self, message: str):
        """Only used for intellisense"""

    def info(self, message: str):
        """Only used for intellisense"""

    def warning(self, message: str):
        """Only used for intellisense"""

    def error(self, message: str):
        """Only used for intellisense"""

    def critical(self, message: str):
        """Only used for intellisense"""


for lvl in ["debug", "info", "warning", "error", "critical"]:
    setattr(
        ColoredLogger,
        lvl,
        lambda self, message, level=lvl: self.log(level.upper(), message),
    )
