#!/usr/bin/env python3
"""Copy the built frontend bundles into this package and stamp their hashes.

Run from the repo root after `npm run build && npm run build_card` in
hass-anycubic/custom_components/anycubic_cloud/frontend_panel:

    python3 tools/sync_bundles.py ../hass-anycubic/custom_components/anycubic_cloud/frontend_panel/dist

Doing this by hand means keeping two hashes, two filenames and a constants file
in agreement, and a mismatch either 404s the panel or leaves every browser on
the previous card.
"""

from __future__ import annotations

import hashlib
import pathlib
import shutil
import sys

PACKAGE_DIR = pathlib.Path(__file__).resolve().parent.parent / "src" / "anycubic_cloud_frontend"
PANEL_BUNDLE = "anycubic-cloud-panel.js"
CARD_BUNDLE = "anycubic-card.js"


def content_hash(path: pathlib.Path) -> str:
    """First 8 hex characters of the file's SHA-256, the convention here."""
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    dist = pathlib.Path(sys.argv[1]).resolve()
    panel_src = dist / PANEL_BUNDLE
    card_src = dist / CARD_BUNDLE

    for src in (panel_src, card_src):
        if not src.is_file():
            print(f"missing built bundle: {src}", file=sys.stderr)
            return 1

    panel_hash = content_hash(panel_src)
    card_hash = content_hash(card_src)

    # The entrypoint carries its hash in the filename, so stale ones would
    # otherwise pile up and ship inside the wheel.
    for old in PACKAGE_DIR.glob("entrypoint.*.js"):
        old.unlink()

    shutil.copyfile(panel_src, PACKAGE_DIR / f"entrypoint.{panel_hash}.js")
    shutil.copyfile(card_src, PACKAGE_DIR / CARD_BUNDLE)

    (PACKAGE_DIR / "constants.py").write_text(
        '"""Build constants for the Anycubic Cloud frontend package."""\n'
        "\n"
        "from typing import Final\n"
        "\n"
        "# Content hash of the built panel bundle, used to cache-bust the served\n"
        "# entrypoint (it is part of the entrypoint's filename).\n"
        f'FILE_HASH: Final = "{panel_hash}"\n'
        "\n"
        "# Content hash of the built card bundle. The card keeps a stable filename, so\n"
        "# this rides on the URL instead. It is tracked separately from FILE_HASH\n"
        "# because a change confined to the card leaves the panel bundle untouched, and\n"
        "# reusing the panel's hash would leave browsers on the previous card.\n"
        f'CARD_HASH: Final = "{card_hash}"\n'
    )

    print(f"panel entrypoint.{panel_hash}.js   card {CARD_BUNDLE} v={card_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
