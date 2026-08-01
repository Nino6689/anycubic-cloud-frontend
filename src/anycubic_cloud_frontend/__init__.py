"""Anycubic Cloud Frontend.

Ships the built sidebar panel for the Home Assistant `anycubic_cloud`
integration. Home Assistant core does not accept bundled frontend assets
inside an integration, so the panel lives here instead -- the same approach
knx-frontend takes for KNX.
"""

from typing import Final

from .constants import FILE_HASH


def locate_dir() -> str:
    """Return the directory holding the built frontend files."""
    return __path__[0]


# Filename of the entrypoint to import the panel.
entrypoint_js: Final = f"entrypoint.{FILE_HASH}.js"

# The web component name that loads the panel.
webcomponent_name: Final = "anycubic-cloud-panel"

is_dev_build: Final = FILE_HASH == "dev"
is_prod_build: Final = not is_dev_build
