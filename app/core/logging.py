"""Logging module."""

import logging


def setup_logging():
    """Set basic logging configuration."""
    logging.basicConfig(
        level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s] %(message)s'
    )
