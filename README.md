# anycubic-cloud-frontend

The built sidebar panel for the Home Assistant
[Anycubic Cloud integration](https://github.com/Nino6689/hass-anycubic_cloud).

Home Assistant core does not accept bundled frontend assets inside an
integration, so the panel is published here instead — the same approach
[`knx-frontend`](https://pypi.org/project/knx-frontend/) takes for KNX.

## Use

```python
import anycubic_cloud_frontend

path = anycubic_cloud_frontend.locate_dir()          # directory of built files
entry = anycubic_cloud_frontend.entrypoint_js        # hashed entrypoint filename
name = anycubic_cloud_frontend.webcomponent_name     # custom element to register
```

The entrypoint filename embeds a content hash so browsers pick up new builds
rather than serving a stale cached panel.

## Licence

GPL-3.0-or-later.
