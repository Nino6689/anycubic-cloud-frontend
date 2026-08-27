"""Build constants for the Anycubic Cloud frontend package."""

from typing import Final

# Content hash of the built panel bundle, used to cache-bust the served
# entrypoint (it is part of the entrypoint's filename).
FILE_HASH: Final = "ddc13e24"

# Content hash of the built card bundle. The card keeps a stable filename, so
# this rides on the URL instead. It is tracked separately from FILE_HASH
# because a change confined to the card leaves the panel bundle untouched, and
# reusing the panel's hash would leave browsers on the previous card.
CARD_HASH: Final = "1bff1207"
