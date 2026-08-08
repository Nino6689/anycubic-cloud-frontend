"""Anycubic Cloud Frontend.

Ships the built sidebar panel for the Home Assistant `anycubic_cloud`
integration. Home Assistant core does not accept bundled frontend assets
inside an integration, so the panel lives here instead -- the same approach
knx-frontend takes for KNX.
"""

from typing import Final

from .constants import CARD_HASH, FILE_HASH


def locate_dir() -> str:
    """Return the directory holding the built frontend files."""
    return __path__[0]


# Filename of the entrypoint to import the panel.
entrypoint_js: Final = f"entrypoint.{FILE_HASH}.js"

# Filename of the Lovelace card bundle. Unlike the panel entrypoint this keeps a
# stable name, so anyone who added it as a dashboard resource by hand keeps
# working across updates; `card_js_url` carries the hash instead.
card_js: Final = "anycubic-card.js"

# Query the card should be requested with. Home Assistant serves this directory
# without a Cache-Control header, so without a changing URL a browser holds on
# to the copy it fetched first and users keep seeing the previous card.
card_js_url: Final = f"{card_js}?v={CARD_HASH}"

# The web component name that loads the panel.
webcomponent_name: Final = "anycubic-cloud-panel"

is_dev_build: Final = FILE_HASH == "dev"
is_prod_build: Final = not is_dev_build
