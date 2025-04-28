from __future__ import annotations
import re
import time
from pathlib import Path
from textwrap import dedent
from behave.model import Scenario, Step
from src.drivers.webdriver_factory import WebDriverFactory

SCREENSHOT_DIR = Path("reports/screenshots")
_INVALID = re.compile(r"[^A-Za-z0-9._-]")


def _safe(text: str) -> str:
    return _INVALID.sub("_", text)


def before_scenario(context, scenario: Scenario):
    context._page_cache = {}
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    context.driver = WebDriverFactory.get_driver()

    context.embed = next(
        (fmt.embed for fmt in context._runner.formatters
         if getattr(fmt, "name", "") == "html-pretty"),
        lambda *_, **__: None,
    )

    context.scenario = scenario


def after_step(context, step: Step):
    if step.status.name.lower() in {"skipped", "untested"}:
        return

    ts = int(time.time() * 1_000)
    filename = (
        f"{_safe(context.scenario.name)}__"
        f"{_safe(step.name)}__"
        f"{step.status.name.lower()}__{ts}.png"
    )
    filepath = SCREENSHOT_DIR / filename
    context.driver.save_screenshot(str(filepath))

    context.embed("image/png", str(filepath),
                  f"Screenshot: {step.keyword} {step.name}")

    details = dedent(f"""
    **Step**   : {step.keyword}{step.name}
    **Status** : {step.status.name.lower()}
    **URL**    : {context.driver.current_url}
    **Title**  : {context.driver.title}
    """).strip()

    context.embed("text/markdown", details, "Step details")


def after_scenario(context, scenario: Scenario):
    context.driver.quit()
