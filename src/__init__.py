from __future__ import annotations

import json

from anki.cards import Card
from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer
from aqt.webview import WebContent

try:
    from aqt.browser.previewer import Previewer
except ImportError:
    from aqt.previewer import Previewer  # type: ignore

from aqt.clayout import CardLayout

web_base = f"/_addons/{mw.addonManager.addonFromModule(__name__)}/web"
mw.addonManager.setWebExports(__name__, "web/.*")
config = mw.addonManager.getConfig(__name__)


def on_webview_will_set_content(
    web_content: WebContent, context: object | None
) -> None:
    if not isinstance(context, (Reviewer, Previewer, CardLayout)):
        return
    web_content.js.append(f"{web_base}/randomize.js")
    web_content.body += (
        "<script>globalThis.RSingleStyles = %s; globalThis.RMultiStyles = %s;</script>"
        % (
            json.dumps(config["single"]),
            json.dumps(config["multi"]),
        )
    )


def on_card_will_show(text: str, card: Card, kind: str) -> str:
    text += f"<script>randomizeStyles({json.dumps(kind.endswith('Answer'))})</script>"
    return text


gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
gui_hooks.card_will_show.append(on_card_will_show)
